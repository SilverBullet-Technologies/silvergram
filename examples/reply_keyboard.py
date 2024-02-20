from silvergram import Bot
from silvergram.types import Message
from config import *

bot = Bot(TOKEN, phrases=PHRASES, reply_keyboards=REPLY_KEYBOARDS)


@bot.on_reply_button()
async def on_inline_button(message: Message):
    chat_id = message.chat.id
    steps = {
        "start": "how",
        "how": "end",
        "end": "start"
    }
    await bot.send_and_next_step_multi(chat_id, steps)


@bot.on_message(step="start")
async def on_message_start(message: Message):
    chat_id = message.chat.id
    await bot.send_and_next_step(chat_id, "how")


@bot.on_message(step="how")
async def on_message_how(message: Message):
    chat_id = message.chat.id
    await bot.send_and_next_step(chat_id, "end")


@bot.on_message(step="end")
async def on_message_end(message: Message):
    chat_id = message.chat.id
    await bot.send_and_next_step(chat_id, "start")


bot.run()
