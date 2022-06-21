def func(a):
    if a < 4:
        b = a / (a - 3)
    print("value of b + ", b)


if __name__ == '__main__':
    try:
        func(3)
        func(5)
    except ZeroDivisionError:
        print("value cannot divisible by zero")
    except NameError:
        print("Name error occurred")
