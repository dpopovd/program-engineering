import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Время выполнения {func.__name__}: {time.time() - start} секунд")
        return result
    return wrapper

@execution_time
def say_hello(name):
    time.sleep(1)
    print(f"Привет, {name}!")

@execution_time
def square_number(x):
    time.sleep(2)
    return x ** 2

if __name__ == "__main__":
    say_hello("Вова")
    result = square_number(5)
    print(f"Результат возведения числа в квадрат: {result}")
