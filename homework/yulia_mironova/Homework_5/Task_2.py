str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 9'
number_1 = str_1.index(': ')
number_2 = str_2.index(': ')
number_3 = str_3.index(': ')
summa = int(str_1[number_1 + 2:]) + int(str_2[number_2 + 2:]) + int(str_3[number_3 + 2:]) + 10
print(summa)
