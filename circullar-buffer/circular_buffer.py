import queue


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.q = queue.Queue(capacity)

    def read(self):
        if self.q.empty():
            raise BufferEmptyException("Empty, Error!")
        return self.q.get()

    def write(self, data):
        if self.q.full():
            raise BufferFullException("Full, Error!")
        self.q.put(data)

    def overwrite(self, data):
        if self.q.full():
            self.q.get()
        self.q.put(data)

    def clear(self):
        while not self.q.empty():
            self.q.get()
