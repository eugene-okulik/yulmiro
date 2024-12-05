def fibonacci(limit = 1000):
    num_1 = 0
    num_2 = 1
    count = 2
    while count < limit:
        yield num_1 + num_2
        tmp = num_1
        num_1 = num_2
        num_2 = tmp + num_2
        count += 1


i = 3
for number in fibonacci(100002):
    if i == 5:
        print(number)
    elif i == 200:
        print(number)
    elif i == 1000:
        print(number)
    elif i == 100000:
        print(number)
    i += 1
