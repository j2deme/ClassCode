from collections import deque


class Cola:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def frente(self):
        return self.items[0] if self.items else None
