def G_x(n):
    output = 1
    i = 1
    while i <= n:
        output *= i
        yield output
        i += 1
for i in G_x(4):
    print(i)
