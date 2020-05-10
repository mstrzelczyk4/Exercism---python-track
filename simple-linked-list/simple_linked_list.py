class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self.index = 0
        self._head = None
        for elem in values:
            self.push(elem)

    def __len__(self):
        return self.index

    def head(self):
        if not self.index:
            raise EmptyListException("No elements!")
        return self._head

    def push(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node
        self.index += 1

    def pop(self):
        if self.index < 1:
            raise EmptyListException("Empty list!")
        node = self._head
        self._head = self._head._next
        self.index -= 1
        return node.value()

    def reversed(self):
        return LinkedList(list(self))

    def __iter__(self):
        while self.index > 0:
            yield self.pop()


class EmptyListException(Exception):
    pass
