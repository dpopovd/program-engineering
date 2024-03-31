def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(str(a) + "\n")
            yield a
            a, b = b, a + b

if __name__ == "__main__":
    fibonacci = fib(200)
    for _ in range(200):
        next(fibonacci)
