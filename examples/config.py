# You can use the following command to create this file
# >>> silvergram addconfig

from silvergram.types import InheritedStep

TOKEN = "1111111111:AAHXMKlOlvnoeg8AHcWV6zJHL3YW4bZZDQs"  # Insert the bot token here

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",      # Describe your steps and phrases here
    "how": "How are you?",                                # There can be any number of phrases and order doesn't matter
    "end": "Goodbye, see you later!"                      # The steps are used to navigate and send messages
}

INLINE_KEYBOARDS = {
    "start": [["Go to next message"]],                    # Describe your steps and message keyboards here
    "how": InheritedStep("start"),                        # To add a keyboard to a message, specify the same step
    "end": InheritedStep("start")                         # You can use InheritedStep for inheritance
}
