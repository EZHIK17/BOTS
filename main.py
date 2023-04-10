HELP = "help - о программе. show - список городов. msk - Москва. spb - Санкт-Петербург"

run = True

var = 'Москва, Санкт-Петербург'

while run:
    command = input('Команда:')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(var)
        gor = input('Выбери город ')
        if gor == 'msk':
            print('Москва')
        elif gor == 'spb':
            print('Санкт-Петербург')
    else:
        print('Такого города нет ')
        break
