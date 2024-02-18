import sys

CONFIG_EN = """\
from silvergram.types import InheritedStep

TOKEN = ""                                             # Insert the bot token here

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",   # Describe your steps and phrases here
    "how": "How are you?",                             # There can be any number of phrases and order doesn't matter
    "end": "Goodbye, see you later!"                   # The steps are used to navigate and send messages
}

INLINE_KEYBOARDS = {
    "start": [["Go to next message"]],                 # Describe your steps and message keyboards here
    "how": InheritedStep("start"),                     # To add a keyboard to a message, specify the same step
    "end": InheritedStep("start")                      # You can use InheritedStep for inheritance
}
"""

CONFIG_RU = """\
from silvergram.types import InheritedStep

TOKEN = ""                                             # Вставьте сюда токен бота

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",   # Здесь опишите свои шаги и фразы
    "how": "How are you?",                             # Может быть сколько угодно фраз и их порядок не важен
    "end": "Goodbye, see you later!"                   # Шаги используются для навигации и отправки сообщений
}

INLINE_KEYBOARDS = {
    "start": [["Go to next message"]],                 # Здесь опишите свои шаги и клавиатуры для сообщений
    "how": InheritedStep("start"),                     # Чтобы добавить клавиатуру к сообщению, укажите тот же шаг
    "end": InheritedStep("start")                      # Можно использовать InheritedStep для наследования
}
"""

CONFIG_EMPTY = """\
TOKEN = ""

PHRASES = {
    
}

INLINE_KEYBOARDS = {
    
}
"""

CONFIG = """\
from silvergram.types import InheritedStep

TOKEN = ""

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",
    "how": "How are you?",
    "end": "Goodbye, see you later!"
}

INLINE_KEYBOARDS = {
    "start": [["Go to next message"]],
    "how": InheritedStep("start"),
    "end": InheritedStep("start")
}
"""


def create_config(opt, pth):
    code = None
    if opt == "en":
        code = CONFIG_EN
    elif opt == "ru":
        code = CONFIG_RU
    elif opt == "empty":
        code = CONFIG_EMPTY
    elif opt is None:
        code = CONFIG
    with open(pth, "w", encoding="utf-8") as f:
        f.write(code)


if __name__ == "__main__":
    args = sys.argv[1:]
    option = None
    path = "config.py"
    if "addconfig" in args:
        if "-t" in args or "-type" in args:
            if "-t" in args:
                option = args[args.index("-t") + 1]
            else:
                option = args[args.index("-type") + 1]
        if "-p" in args or "-path" in args:
            if "-p" in args:
                path = args[args.index("-p") + 1]
            else:
                path = args[args.index("-path") + 1]
        create_config(option, path)
