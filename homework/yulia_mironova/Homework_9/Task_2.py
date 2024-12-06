temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33,
                31, 30, 32, 30, 28, 24, 23]


def hot(x):
    return x > 28


hot_days = list(filter(hot, temperatures))
print(hot_days)
print('Самая высокая: ', max(hot_days))
print('Самая низкая: ', min(hot_days))
print('Средняя: ', round(sum(hot_days) / len(hot_days)))
