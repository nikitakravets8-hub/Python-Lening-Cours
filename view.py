"""
    Модуль показывает информацию в консоль
"""


"""  выводит список в консоль"""


def show_collection(task_list):
    print("=" * 45)
    for numbers,name in enumerate(task_list):
        word = ''
        for literal in name:
            if literal != "|":
                word += literal
            else:
                print(numbers + 1, word)
    print("=" * 45)

"""def show_collection(task_list):
    print("=" * 45)
    full_task_list = []
    for numbers,task in enumerate(task_list):
        task_temp = task.split(" | ")
        print(numbers +1 , task_temp[0])
        full_task_list.append(task_temp[1])
    selected_task = input("<UNK> <UNK> <UNK> <UNK> <UNK>: ")
    if selected_task.isdigit():
        print("~" * 45)
        print(full_task_list[int(selected_task)-1])
        print("~" * 45)
    else:
        if selected_task == "":
            print("=" * 45)
        else:
            print(" Неправкельный ввод")
    print("=" * 45)"""


"""показывает список и ждёт """


def show_message(message= None ,mes_action= None):
    if message is not None:
        print(f"Новая задача {message} успешно {mes_action}")
    input("Нажмите Enter  для продолжения:")

