from fifo_first import FirstFifo
from fifo_second import SecondFifo


if __name__ == '__main__':
    length: int = 10
    first_queue = FirstFifo(length)
    second_queue = SecondFifo(length)
    for i in range(length):
        first_queue.push(i + i)
        second_queue.push(i + i)
