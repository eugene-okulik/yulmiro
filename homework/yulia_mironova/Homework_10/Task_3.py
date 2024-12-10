number_1 = int(input('Введите 1 число: '))
number_2 = int(input('Введите 2 число: '))


def do_operation(func):
    def wrapper(x, y):
        result = 0
        if x == y:
            result = func(x, y, '+')
        elif ((x < 0) and (y > 0)) or ((x > 0) and (y < 0)):
            result = func(x, y, '*')
        elif x < y:
            result = func(x, y, '/')
        elif x > y:
            result = func(x, y, '-')
        return result
    return wrapper


@do_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return second * first


print(calc(number_1, number_2))
