class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.index] = item
        if self.index == self.capacity - 1:
            self.index = 0
        else:
            self.index += 1

    def get(self):
        return [item for item in self.storage if item]