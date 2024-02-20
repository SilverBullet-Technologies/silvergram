# You can use the following command to create this file
# >>> python -m silvergram addconfig [-t, --type TYPE] [-p, --path PATH]

from silvergram.types import InheritedStep

TOKEN = "1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  # Insert the bot token here

PHRASES = {
    "start": "Hello! I am a simple SilverGram bot!",      # Describe your steps and phrases here
    "how": "How are you?",                                # There can be any number of phrases and order doesn't matter
    "end": "Goodbye, see you later!"                      # The steps are used to navigate and send messages
}

INLINE_KEYBOARDS = {                                      # Describe your steps and inline keyboards here
    "how": [["Go to next message"]],                      # To add a keyboard to a message, specify the same step
    "end": InheritedStep("how")                           # You can use InheritedStep for inheritance
}

REPLY_KEYBOARDS = {                                       # Describe your steps and reply keyboards here
    "start": [["Go to next message"]]                     # The syntax is identical to inline keyboards
}
