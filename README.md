# Silvergram

Silvergram is a powerful Python library designed to enhance the functionality of the popular Telegram bot framework, [Aiogram](https://github.com/aiogram/aiogram). It serves as a comprehensive wrapper, providing additional features and simplifying the development process for creating sophisticated Telegram bots

## Features

- **Enhanced Functionality**: Silvergram extends the capabilities of Aiogram, offering additional features such as advanced message sending, phrases and keyboards management, and more
- **Simplified Development**: With Silvergram, developers can write cleaner and more concise code
- **Built-in Utilities**: The library includes various built-in utilities for common bot tasks, such as sending messages, managing user interactions, handling callbacks, and working with inline queries
- **Flexibility**: Silvergram is designed to be highly flexible, allowing developers to easily integrate it into existing Aiogram projects or use it as the foundation for new bot developments

## Installation

You can install Silvergram via pip:

```bash
pip install silvergram
```

## Quick Start

Here's a simple [quick start example](https://github.com/SilverBullet-Technologies/silvergram/blob/main/examples/quick_start.py) of how to use Silvergram to create a basic bot:

```python
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
```

For more detailed usage instructions and examples, please see [docs](https://github.com/SilverBullet-Technologies/silvergram/blob/main/docs) and [examples](https://github.com/SilverBullet-Technologies/silvergram/blob/main/examples) folders

## Adding Configuration File

You can create a [config.py](https://github.com/SilverBullet-Technologies/silvergram/blob/main/examples/config.py) file using the following command:

```bash
python -m silvergram addconfig [-t, --type TYPE] [-p, --path PATH]
```

**Arguments:**

`-t, --type TYPE [en, ru, empty]`

Specify the type of generating. Possible values: 'en' for English comments, 'ru' for Russian comments, 'empty' for adding only the necessary functionality. Default none, which means creating a regular file without comments

`-p, --path PATH`

Specify the path where the configuration file will be saved. If not provided, the file will be saved in the current working directory

## Contributing

Contributions to Silvergram are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub

## License

This project is licensed under the MIT License - see the LICENSE file for details