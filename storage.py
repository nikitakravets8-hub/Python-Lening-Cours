
"""
    Модуль показывает информацию в консоль
"""

def load_collection(file_name):
    task_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            task_list.append(line.strip())
        return task_list



def save_collection(file_name, task_list):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.writelines(f"{task}\n")

