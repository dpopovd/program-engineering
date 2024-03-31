class ValueTooSmallError(Exception):
    def __init__(self, message="Значение слишком мало"):
        self.message = message
        super().__init__(self.message)


def check_value(x):
    if x < 10:
        raise ValueTooSmallError("Значение слишком мало")
    else:
        print("Значение допустимо")


if __name__ == "__main__":
    try:
        check_value(5)
    except ValueTooSmallError as e:
        print(e)

    try:
        check_value(15)
    except ValueTooSmallError as e:
        print(e)
