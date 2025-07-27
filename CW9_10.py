import time


def time_decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"duration = {end_time - start_time}")
        return result

    return wrapper


@time_decorator
def fibo_list(n):
    result = []
    for i in range(n + 1):
        result.append(fibo(i))
    return result


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo_list(5))
