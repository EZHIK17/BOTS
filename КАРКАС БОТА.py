import random

HELP = """help - о программе.
add - добавить задачу в список.
show - напечатать все задачи.
random - добавлять случайную задачу на дату Сегодняю"""

random_tasks = ['Убраться дома', 'Сходить в магазин', 'Накормить тигра']
tasks = {

}

run = True


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
        print("Задача ", task, ' добавлена на время ', date)


while run:
    command = input('Введи команду: ')
    if command == 'help':
        print(HELP)
    elif command == "show":
        date = input('Введи дату для отображения списка задач ')
        if date in tasks:
            for tasks in tasks[date]:
                print('- ', tasks)
        else:
            print('Такой даты нет')
    elif command == 'add':
        date = input('Введи дату для задачи: ')
        task = input("Введи задачу")
        add_todo(date, task)
    elif command == 'random':
        task = random.choice(random_tasks)

        add_todo('Сегодня', task)
    else:
        print('Неизвестная команда.')
        break
print('Пока')
