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
    for i,j in enumerate(task_list):
        print(i + 1, j)
    print("=" * 45)

def show_message(message= None ,mes_action= None):
    if message is not None:
        print(f"Новая задача {message} успешно {mes_action}")
    input("Нажмите Enter  для продолжения:")

is_running = True
collection = ["task1,task2"] #list

print("Добро пожаловать!")

while is_running:
   print("1 - посмотреть задачи |\n"
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
           add_task = input("Ввидите имя задачи: ")
           collection.append(add_task)
           show_message(add_task , "добавленна")
       case "3":
           show_collection(task_list=collection)
           select_task = int(input("Введите номер задачи для редактирования: "))
           edit_task = input("Укажите новое имя задачи: ")
           collection[select_task - 1] = edit_task
           show_message(edit_task , "отредоктированна")
       case "4":
            show_collection(task_list=collection)
            delete_edit = int(input("Введите номер задачи для удаления: "))
            collection.pop(delete_edit -1)
            show_message(delete_edit , " удалена")

       case "5":
           confirm = input("Вы дейтивельно хотите выйти из приложения? Да/Нет")
           if (confirm == "нет"
               or confirm == "н"
               or confirm == "д"
               or confirm == "n"
               or confirm == "y"
               or confirm == "l"):
            is_running = False
           print("До свидания!")
       case _:
           print("Такого пункта нет!")

   print(collection)




































































































































































































#if __name__=="__main__":
#    print("ghbdtn")