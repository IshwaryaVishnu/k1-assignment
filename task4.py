def fib(n):
    fib_array = [0, 1]
    any(map(lambda _: fib_array.append(sum(fib_array[-2:])),
            range(2, n)))
    return fib_array[:n]
print(fib(20))