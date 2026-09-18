"""Скрипт для демонстрации процессов"""

import os
import subprocess
import multiprocessing as mp
import time

from pyexpat.errors import messages


def start():
    print("start!")
    #print(f"{os.getppid().__str__()}")
    process = mp.Process(target=welcome("welcome!"), args=())
    #process.start()
    print(os.getpid())
    process.join()
    print(process.name)
    time.sleep(10)
    
    #process.kill()
    print(process.is_alive())

def welcome(message):
    print(message)
    print(os.getpid())
    work()

def work():
    print("work!")
    finish()

def finish():
    print("finish!")

start()


