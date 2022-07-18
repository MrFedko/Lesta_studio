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
