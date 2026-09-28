"""
    Модуль показывает информацию в консоль
"""
from view import show_message
from utils import check_confirm


def create_task(tasl_list):
    name_task = input("Введите имя задачи для добавления")
    if name_task != '' and name_task is not tasl_list and name_task is not None:
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


