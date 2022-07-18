from time_of_func import time_of_func


@time_of_func
def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        num = array[0]
        less_then_num = [i for i in array[1:] if i <= num]
        greater_then_num = [i for i in array[1:] if i > num]
        return quick_sort(less_then_num) + [num] + quick_sort(greater_then_num)
