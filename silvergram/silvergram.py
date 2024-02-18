from asyncio import run
from aiogram import Bot as BotAiogram, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .types import InheritedStep
from typing import List, Dict, Union


class Bot(BotAiogram):
    def __init__(
        self,
        token: str,
        *,
        phrases: Dict[str, Union[str, InheritedStep]] = None,
        inline_keyboards: Dict[str, Union[List[List[str]], InheritedStep]] = None
    ):
        super(Bot, self).__init__(token)
        self.__dp = Dispatcher()
        self.__phrases = phrases or {}
        self.__inline_keyboards = {}
        if inline_keyboards is not None:
            for keyboard in inline_keyboards:
                kb = []
                if isinstance(inline_keyboards[keyboard], InheritedStep):
                    row_keyboard = inline_keyboards[inline_keyboards[keyboard].content]
                else:
                    row_keyboard = inline_keyboards[keyboard]
                for row in row_keyboard:
                    kb_row = []
                    for key in row:
                        kb_row.append(InlineKeyboardButton(text=key, callback_data=key))
                    kb.append(kb_row)
                self.__inline_keyboards[keyboard] = InlineKeyboardMarkup(inline_keyboard=kb)
        self.__step = {}
        self.__on_inline_button_handlers = []
        self.__on_message_handlers = []

    async def get_chat_instance(
        self,
        chat_id: Union[int, str]
    ):
        chat = str(chat_id)
        if chat not in self.__step:
            self.__step[chat] = {}
            self.__step[chat]["step"] = list(self.__phrases.keys())[0]
        return self.__step[chat]

    async def get_step(
        self,
        chat_id: Union[int, str],
    ):
        return (await self.get_chat_instance(chat_id))["step"]

    async def next_step(
        self,
        chat_id: Union[int, str],
        step: str
    ):
        (await self.get_chat_instance(chat_id))["step"] = step

    async def next_step_multi(
        self,
        chat_id: Union[int, str],
        steps: Dict[str, str]
    ):
        chat_instance = await self.get_chat_instance(chat_id)
        chat_instance["step"] = steps[chat_instance["step"]]

    async def send_current_message(
        self,
        chat_id: Union[int, str]
    ):
        step = await self.get_step(chat_id)
        reply_markup = None
        if step in self.__inline_keyboards:
            reply_markup = self.__inline_keyboards[step]
        await self.send_message(
            chat_id=chat_id,
            text=self.__phrases[step],
            reply_markup=reply_markup
        )

    async def send_and_next_step(
        self,
        chat_id: Union[int, str],
        step: str
    ):
        await self.send_current_message(chat_id)
        await self.next_step(chat_id, step)

    async def send_and_next_step_multi(
        self,
        chat_id: Union[int, str],
        steps: Dict[str, str]
    ):
        await self.send_current_message(chat_id)
        await self.next_step_multi(chat_id, steps)

    def on_inline_button(
        self,
        step: str = None
    ):
        def on_inline_button_decorator(function):
            self.__on_inline_button_handlers.append([function, step])
        return on_inline_button_decorator

    def on_message(
        self,
        step: str = None
    ):
        def on_message_decorator(function):
            self.__on_message_handlers.append([function, step])
        return on_message_decorator

    def run(self):
        @self.__dp.callback_query()
        async def on_inline_button_handler(callback):
            await callback.answer()
            message = callback.message
            current_step = await self.get_step(str(message.chat.id))
            for handler in self.__on_inline_button_handlers:
                if handler[1] == current_step or handler[1] is None:
                    await handler[0](callback)

        @self.__dp.message()
        async def on_message_handler(message):
            current_step = await self.get_step(str(message.chat.id))
            for handler in self.__on_message_handlers:
                if handler[1] == current_step or handler[1] is None:
                    await handler[0](message)

        run(self.__dp.start_polling(self))
