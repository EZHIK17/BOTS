HELP = "help - о программе. show - список городов. msk - Москва. spb - Санкт-Петербург"

run = True

while run:
    command = input('Команда:')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print('Москва,Санкт-Петербург')
    else:
        print('Такого города нет')
        break
print('Пока')
