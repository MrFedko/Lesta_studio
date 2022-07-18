class Node:
    def __init__(self, next_element=None):
        self.data = 0
        self.next_element = next_element

    @property
    def next_element(self) -> int:
        return self._next_element

    @next_element.setter
    def next_element(self, value: int):
        self._next_element = value

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int):
        self._data = value

    def __repr__(self):
        return str(self.data)


class SecondFifo:
    def __init__(self, size: int):
        self._size = size
        self._count = 0
        temp = Node()
        first = temp

        for i in range(size - 1):
            temp = Node(temp)

        first.next_element = temp

        self._head = first
        self._tail = first

    @property
    def _size(self) -> int:
        return self.__size

    @_size.setter
    def _size(self, value: int):
        self.__size = value

    @property
    def _count(self) -> int:
        return self.__count

    @_count.setter
    def _count(self, value: int):
        self.__count = value

    @staticmethod
    def _is_empty(value: int) -> bool:
        return value == 0

    @staticmethod
    def _is_full(count: int, size: int) -> bool:
        return count == size
