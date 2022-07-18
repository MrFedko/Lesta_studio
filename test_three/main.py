from quick_sort import quick_sort
from random import randint


if __name__ == '__main__':
    array = [randint(1, 100) for i in range(randint(50,1000))]
    quick_sort(array)
