text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
marks = ['.', ',', '?', '!', ';', ':', '-', '...']
list_text = text.split()
new_text = ''
for word in list_text:
    if word[-1] in marks:
        baza = word[:-1]
        mark = word[-1]
        new_text = new_text + baza + 'ing' + mark + ' '
    else:
        new_text = new_text + word + 'ing' + ' '
print(new_text)
