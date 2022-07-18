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
