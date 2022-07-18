from example import is_even
from my_code import my_is_even
from statistics import mean

if __name__ == '__main__':
    for i in range(1000):
        is_even(3)
        my_is_even(3)

    for i in range(1000):
        my_is_even(3)
        is_even(3)

    result: list = []
    with open("is_even", "r") as file1, open("my_is_even", "r") as file2:
        for i, j in zip(file1.readlines(), file2.readlines()):
            result.append(int(i.strip()) / int(j.strip()))

    print(f"побитовое & быстрее деления в {mean(result):.4f} раз")
