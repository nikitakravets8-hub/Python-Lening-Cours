"""
    Точка входа в приложение Task Manager
    version 0.0.1
    ---description---
    -[x] создать репозиторий проекта
    -[x] релеазовать цикл приложения
    -[] реализовать хранилище задач
"""


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
           print("=" * 45)
           for i,j in enumerate(collection):
               print(i + 1 , j)
           print("=" * 45)
           input("Нажмите Enter  для продолжения: ")
       case "2":
           add_task = input("Ввидите имя задачи: ")
           collection.append(add_task)
       case "3":
           print("=" * 45)
           for i,j in enumerate(collection):
               print(i + 1 , j)
           print("=" * 45)
           select_task = int(input("Введите номер задачи для редактирования: "))
           edit_task = input("Укажите новое имя задачи: ")
           collection[select_task - 1] = edit_task
       case "4":
            print("=" * 45)
            for key, item in enumerate(collection):
                print(key + 1, item)
            print("=" * 45)
            delete_edit = int(input("Введите номер задачи для удаления: "))
            collection.pop(delete_edit -1)
       case "5":
           is_running = False
           print("До свидания!")
       case _:
           print("Такого пункта нет!")

   print(collection)






































































































































































































#if __name__=="__main__":
#    print("ghbdtn")