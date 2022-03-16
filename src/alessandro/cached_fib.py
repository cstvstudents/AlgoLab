cache = {}

def fib(n):
    if cache.get(n, False):
        return cache[n]

    if n < 2:
        return 1
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

for i in range(50):
    print(f"{i} => {fib(i)}")
