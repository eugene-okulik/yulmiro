PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
all_list = PRICE_LIST.split()
first_list = [all_list[i] for i in range(0, len(all_list), 2)]
second_list = [int((all_list[i])[:-1]) for i in range(1, len(all_list), 2)]
final_dict = dict(zip(first_list, second_list))
print(final_dict)
