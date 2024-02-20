from silvergram import Bot
from silvergram.types import Message

TOKEN = "YOUR_TOKEN"
PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!"
}

bot = Bot(TOKEN, phrases=PHRASES)


@bot.on_message()
async def on_message_start(message: Message):
    chat_id = message.chat.id
    await bot.send_current_message(chat_id)


if __name__ == "__main__":
    bot.run()
