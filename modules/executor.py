#!/usr/bin/python
# by nu11secur1ty
import requests
import os

payload = open('payload.txt').read().splitlines()

remove_from_urls = []

for url in payload:
    remove_url = requests.get(url)
    print(remove_url.status_code)
    if remove_url.status_code == 404:
        remove_from_urls.append(url)
        continue
        
payload = [url for url in payload if url not in remove_from_urls]
print("Seraching STATUS:",payload)

# Save urls example
with open('output.txt', 'w+') as file:
    for item in payload:
        file.write(item + '\n')
