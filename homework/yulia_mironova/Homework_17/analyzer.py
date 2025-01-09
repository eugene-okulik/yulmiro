import argparse
import os

parser = argparse.ArgumentParser(description='Find logs')
parser.add_argument("path", help="Input path")
parser.add_argument("--text", help="Error text")
args = parser.parse_args()


def five_words(active_line, word):
    list_line = active_line.split(' ')
    index = list_line.index(word)
    if (index - 5) >= 0 and (index + 5) <= len(list_line):
        result = list_line[index - 5:index + 6]
    elif (index - 5) < 0 and (index + 5) <= len(list_line):
        result = list_line[0:index + 6]
    elif (index - 5) >= 0 and (index + 5) > len(list_line):
        result = list_line[index - 5:]
    else:
        result = list_line

    return ' '.join(result)


def read_files():
    for file_name in os.listdir(args.path):
        line_number = 0
        file_path = os.path.join(args.path, file_name)
        with open(file_path, 'r') as file_data:
            for line in file_data:
                line_number+=1
                yield line, file_name, line_number


for file_line, name, number in read_files():
    if args.text in file_line:
        print(f'Название файла: {name}, номер строки: {number}, ошибка: {five_words(file_line, args.text)}')
