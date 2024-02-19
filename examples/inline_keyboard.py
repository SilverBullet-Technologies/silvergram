from silvergram import Bot
from config import *

bot = Bot(TOKEN, phrases=PHRASES, inline_keyboards=INLINE_KEYBOARDS)


@bot.on_inline_button()
async def on_inline_button(callback):
    chat_id = callback.message.chat.id
    steps = {
        "start": "how",
        "how": "end",
        "end": "start"
    }
    await bot.send_and_next_step_multi(chat_id, steps)


@bot.on_message(step="start")
async def on_message_start(message):
    chat_id = message.chat.id
    await bot.send_and_next_step(chat_id, "how")


@bot.on_message(step="how")
async def on_message_how(message):
    chat_id = message.chat.id
    await bot.send_and_next_step(chat_id, "end")


@bot.on_message(step="end")
async def on_message_end(message):
    chat_id = message.chat.id
    await bot.send_and_next_step(chat_id, "start")


bot.run()
