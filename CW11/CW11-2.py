def fibo():
    n, m = 0, 1
    while True:
        yield n
        n, m = m, n + m


fibo_it = fibo()
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
print(next(fibo_it))
