import time

def time_of_func(func):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        with open(f"{func.__name__}", "a") as file:
            file.write(f"{time.perf_counter_ns() - start_time} \n")
        return res
    return wrapped
