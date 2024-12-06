import random

salary = int(input('enter salary: '))
bonus = random.choice([True, False])
if bonus:
    new_salary = salary + random.randint(1000, 10000)
else:
    new_salary = salary
print(f'{salary}, {bonus} - "${new_salary}"')
