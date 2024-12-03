def print_dict(y, x):
    for i in range(0, x):
        print(y, end='')
    print()


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for key, value in words.items():
    print_dict(key, value)
