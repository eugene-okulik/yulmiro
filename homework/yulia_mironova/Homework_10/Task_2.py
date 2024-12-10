def repeat_me(func):
    def wrapper(text_1, count):
        for i in range(count):
            func(text_1)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
