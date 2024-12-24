import os
import datetime


base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
homework_file_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')

my_dict = {}

with open(homework_file_path, 'r') as file_data:
    for line in file_data.readlines():
        my_dict[line[:1]] = line[3:29]


def str_to_date(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')


python_date1 = str_to_date(my_dict['1'])
python_date2 = str_to_date(my_dict['2'])
python_date3 = str_to_date(my_dict['3'])

print(python_date1 + datetime.timedelta(days=7))
print(python_date2.weekday())
print((datetime.datetime.now() - python_date3).days)
