from time_of_func import time_of_func


@time_of_func
def my_is_even(value: int) -> bool: return value & 1 == 0
