def finish_me(func):
    def wrapper(text_1):
        func(text_1)
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
