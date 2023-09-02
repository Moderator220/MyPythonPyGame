word = input('введите слово: ')
arrow = []

while word != 'stop':
    arrow.append(word)
    word = input('введите слово: ')
print(arrow)
