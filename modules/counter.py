#!/usr/bin/python
import time
from colorama import init, Fore, Back, Style
init(convert=True)

x = 1
while True:
    print("Starting the attack", (x))
    time.sleep(1)
    x += 1

print(Fore.RED +"Happy hunting with nu11secur1ty =)")
print(Style.RESET_ALL)
