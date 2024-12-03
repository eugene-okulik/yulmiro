def find_number(stroka):
    number = int(stroka.split()[-1])
    return number

str_1 = 'результат операции: 42'
str_2 = 'результат операции: 54'
str_3 = 'результат работы программы: 209'
str_4 = 'результат: 2'
print(find_number(str_1) + find_number(str_2) + find_number(str_3) + find_number(str_4) + 10)
