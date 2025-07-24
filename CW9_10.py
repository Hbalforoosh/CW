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
def test(n):
    return n * 2


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


# def gen_fibo(n):
#     for i in range(n):
#         yield fibo(i)


# for j in gen_fibo(5):
#     print(j, end=",")


@time_decorator
def fibo_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for item in fibo_generator(10):
    print(item)


print(list(fibo_generator(10)))

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
def test(n):
    return n * 2


print(test(10))
