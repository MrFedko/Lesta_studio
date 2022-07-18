class FirstFifo:
    def __init__(self, size: int):
        self._items: list = [0 for i in range(size)]
        self._head: int = 0
        self._tail: int = 0

        self._count: int = 0
        self._size: int = size

    @property
    def _count(self) -> int:
        return self.__count

    @_count.setter
    def _count(self, value: int):
        self.__count = value

    @property
    def _size(self) -> int:
        return self.__size

    @_size.setter
    def _size(self, value: int):
        self.__size = value

    @staticmethod
    def _is_full(count: int, size: int) -> bool:
        return count == size

    @staticmethod
    def _is_empty(count: int) -> bool:
        return count == 0

    @staticmethod
    def _next_index(size: int, new_index: int) -> int:
        temp = new_index + 1
        if temp >= size:
            temp = 0
        return temp
