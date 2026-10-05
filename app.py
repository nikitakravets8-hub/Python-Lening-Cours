from view import show_collection , show_message
from utils import check_confirm , get_base_dir , insure_save_file
from core import  create_task , deleted_task , edited_task
from storage import save_collection, load_collection
import os.path


def app():
    is_running = True
    name_file = os.path.join(get_base_dir(), 'saves.txt')
    insure_save_file(name_file)
    collection = load_collection(name_file)


    while is_running:
       print(" 1 посмотреть задачи |\n"
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