#!/usr/bin/python
# by nu11secur1ty
import requests
import os
import time


target=input("Give the URL target + path\n")
payload = open('payload.txt').read().splitlines()

remove_from_urls = []

for url in payload:
    remove_url = requests.get(url)
    print(target,remove_url.status_code)
    if remove_url.status_code == 404:
        remove_from_urls.append(url)
        continue
        
payload = [url for url in payload if url not in remove_from_urls]
print("Seraching STATUS:\n",payload)

# Save
with open('output.txt', 'w+') as file:
    for item in payload:
        file.write(item + '\n')
