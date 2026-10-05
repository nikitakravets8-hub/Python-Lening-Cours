"""
    Модуль показывает информацию в консоль
"""
import os
import sys



def check_confirm(action: str):
    confirm = input("у/n")
    if (confirm.startswith('y')
            or confirm.startswith('д')):
        return True
    else:
        return False




def get_base_dir():
    if getattr(sys, 'frozen', False):
        return  os.path.dirname(sys.executable)
    else:
        return  os.path.dirname(os.path.abspath(__file__))

def insure_save_file(name_file):
    if not os.path.exists(name_file):
        with open(name_file, 'w') as f:
            f.write("")