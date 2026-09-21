"""
    Точка входа в приложение Task Manager
    version 0.0.1
    ---description---
    -[x] создать репозиторий проекта
    -[x] релеазовать цикл приложения
    -[] реализовать хранилище задач
"""

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

def show_message(message= None ,mes_action= None):
    if message is not None:
        print(f"Новая задача {message} успешно {mes_action}")
    input("Нажмите Enter  для продолжения:")

def check_confirm(action: str):
    confirm = input("Да/Нет")
    if (confirm.startswith('y')
            or confirm.startswith('Y')):
        return True
    else:
        return False

def create_task(tasl_list):
    name_task = input("Введите имя задачи для добавления")
    if name_task != '' and name_task is not tasl_list and name_task is not  None:
        content_task = input("Введите содержимое задачи для добавления")
        tasl_list.append(f"{name_task}|{content_task}")
    return tasl_list

def edited_task(task_list):
    select_task = int(input("Введите номер задачи для редактирования: "))
    edit_task = input("Укажите новое имя задачи: ")
    task_list[select_task - 1] = edit_task
    show_message(edit_task, "отредоктированна")


def deleted_task(task_list):
    delete_edit = int(input("Введите номер задачи для удаления: "))
    if check_confirm("Удаление прошло успешно"):
        task_list.pop(delete_edit - 1)
        show_message(delete_edit, " удалена")

def load_collection(file_name):
    task_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            task_list.append(line.strip())
        return task_list

def save_collection(file_name, task_list):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.writelines(f"{task}\n`")

def main():
    is_running = True
    name_file = "saves.txt"
    collection = load_collection(name_file)

    while is_running:
       print("1  посмотреть задачи |\n"
             " 2 добавить задачу|\n"
             " 3 редактирование задачи|\n"
             " 4 удаление задачи|\n"
             " 5 выход\n")
       choice_user = input("Ввидите свой выбор: ")
       match str(choice_user):
           case "1":
               show_collection(task_list=collection)
               show_message()
           case "2":
               collection = create_task(collection)
               save_collection(name_file,task_list=collection)
               show_message(" Задача успешно добавленна")
           case "3":
               show_collection(task_list=collection)
               edited_task(collection)
               save_collection(name_file, task_list=collection)
           case "4":
                show_collection(task_list=collection)
                deleted_task(collection)
                save_collection(name_file,task_list=collection)
           case "5":
                is_running = not check_confirm ("До свидание")
           case _:
               print("Такого пункта нет!")

       print(collection)

if __name__ == "__main__":
    print("Добро пожаловать!")
    main()


































































































































































































#if __name__=="__main__":
#    print("ghbdtn")