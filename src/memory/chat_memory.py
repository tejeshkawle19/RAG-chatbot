from collections import deque


class ChatMemory:

    def __init__(self, max_messages=6):
        self.history = deque(maxlen=max_messages)

    def add_user(self, message):
        self.history.append(("User", message))

    def add_assistant(self, message):
        self.history.append(("Assistant", message))

    def get_history(self):

        conversation = ""

        for role, msg in self.history:
            conversation += f"{role}: {msg}\n"

        return conversation

    def clear(self):
        self.history.clear()