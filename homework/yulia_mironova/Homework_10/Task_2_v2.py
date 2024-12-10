def repeat_me(count):
    def decorator(func):
        def wrapper(text_1):
            for i in range(count):
                func(text_1)
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
