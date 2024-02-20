import sys

CONFIG_EN = """\
from silvergram.types import InheritedStep

TOKEN = "1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  # Insert the bot token here

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",      # Describe your steps and phrases here
    "how": "How are you?",                                # There can be any number of phrases and order doesn't matter
    "end": "Goodbye, see you later!"                      # The steps are used to navigate and send messages
}

INLINE_KEYBOARDS = {                                      
    "how": [["Go to next message"]],                      # Describe your steps and inline keyboards here
    "end": InheritedStep("how")                           # You can use InheritedStep for inheritance
}

REPLY_KEYBOARDS = {                                       # Describe your steps and reply keyboards here
    "start": [["Go to next message"]]                     # The syntax is identical to inline keyboards
}
"""

CONFIG_RU = """\
from silvergram.types import InheritedStep

TOKEN = "1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  # Вставьте сюда токен бота

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",      # Здесь опишите свои шаги и фразы
    "how": "How are you?",                                # Может быть сколько угодно фраз и их порядок не важен
    "end": "Goodbye, see you later!"                      # Шаги используются для навигации и отправки сообщений
}

INLINE_KEYBOARDS = {                                      
    "how": [["Go to next message"]],                      # Здесь опишите свои шаги и inline-клавиатуры
    "end": InheritedStep("how")                           # Можно использовать InheritedStep для наследования
}

REPLY_KEYBOARDS = {                                       # Здесь опишите свои шаги и reply-клавиатуры
    "start": [["Go to next message"]]                     # Синтаксис такой же, как и у inline-клавиатур
}
"""

CONFIG_EMPTY = """\
TOKEN = ""

PHRASES = {
    
}

INLINE_KEYBOARDS = {
    
}

REPLY_KEYBOARDS = {
    
}
"""

CONFIG = """\
from silvergram.types import InheritedStep

TOKEN = "1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",
    "how": "How are you?",
    "end": "Goodbye, see you later!"
}

INLINE_KEYBOARDS = {
    "how": [["Go to next message"]],
    "end": InheritedStep("how")
}

REPLY_KEYBOARDS = {
    "start": [["Go to next message"]]
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
        if "-t" in args or "--type" in args:
            if "-t" in args:
                option = args[args.index("-t") + 1]
            else:
                option = args[args.index("--type") + 1]
        if "-p" in args or "--path" in args:
            if "-p" in args:
                path = args[args.index("-p") + 1]
            else:
                path = args[args.index("--path") + 1]
        create_config(option, path)
