# You can use the following command to create this file
# >>> silvergram addconfig

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
