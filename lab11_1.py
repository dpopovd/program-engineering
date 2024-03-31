def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    fibonacci = fib(200)
    for _ in range(200):
        print(next(fibonacci))
