from silvergram import Bot

TOKEN = "YOUR_TOKEN"
PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!"
}

bot = Bot(TOKEN, phrases=PHRASES)


@bot.on_message()
async def on_message_start(message):
    chat_id = message.chat.id
    await bot.send_current_message(chat_id)


if __name__ == "__main__":
    bot.run()
