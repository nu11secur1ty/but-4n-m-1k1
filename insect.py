#!/usr/bin/python
# Author nu11secur1ty
import os
import time
from colorama import init, Fore, Back, Style
init(convert=True)

os.system('python modules/payload-generator.py > payload.txt')
time.sleep(3)
os.system('python modules/executor.py')

print("\n")
print(Fore.RED"Please check the output.txt file, there you can find what you were searching for.\n")
print(Style.RESET_ALL)
