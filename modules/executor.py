#!/usr/bin/python
# by nu11secur1ty
import requests
import os
import time
from colorama import init, Fore, Back, Style
init(convert=True)


target=input(Fore.MAGENTA +"Give the URL target + path\n")
print(Style.RESET_ALL)
payload = open('modules/payload.txt').read().splitlines()

remove_from_urls = []

for url in payload:
    remove_url = requests.get(url)
    print(Fore.YELLOW +"Scanning, please wait...\n")
    print(target,remove_url.status_code)
    print(Style.RESET_ALL)
    if remove_url.status_code == 404:
        remove_from_urls.append(url)
        continue
        
payload = [url for url in payload if url not in remove_from_urls]
print("The scanning is done, please check your output.txt file...\n")

# Save
with open('output.txt', 'w+') as file:
    for item in payload:
        file.write(item + '\n')
