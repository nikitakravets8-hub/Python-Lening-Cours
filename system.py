import os
import sys
import platform
from platform import processor

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
build = os_version[5:]
processor = platform.processor()
py_ver = platform.python_version()

list_task= [os_name,os_version,os_arch,build, processor,py_ver]

list_os= []

for task in range(len(list_task)):
    list_os.append(list_task[task])

sys.stdout.write(f"{list_os}")
out = sys.stdout.readline()

