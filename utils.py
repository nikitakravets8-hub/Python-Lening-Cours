"""
    Модуль показывает информацию в консоль
"""

def check_confirm(action: str):
    confirm = input("у/n")
    if (confirm.startswith('y')
            or confirm.startswith('д')):
        return True
    else:
        return False
