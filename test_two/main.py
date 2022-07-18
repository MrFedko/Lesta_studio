from fifo_first import FirstFifo
from fifo_second import SecondFifo


if __name__ == '__main__':
    length: int = 10
    first_queue = FirstFifo(length)
    second_queue = SecondFifo(length)
    for i in range(length):
        first_queue.push(i + i)
        second_queue.push(i + i)

    print(f"""first 
{first_queue}""")

    for i in range(5):
        first_queue.pop()
        first_queue.push(i + 100)
        print(first_queue)

    print("""
    
    --------------
    
    """)

    print(f"""second 
{second_queue}""")

    for i in range(5):
        second_queue.pop()
        second_queue.push(i + 100)
        print(second_queue)
