#!/usr/bin/python
# Author nu11secur1ty
import os
import time
from colorama import init, Fore, Back, Style
init(convert=True)

# Version
VERSION = "1.4"

BANNER = f"""
  ooooo                                              .   
`888'                                            .o8   
 888  ooo. .oo.    .oooo.o  .ooooo.   .ooooo.  .o888oo 
 888  `888P"Y88b  d88(  "8 d88' `88b d88' `"Y8   888   
 888   888   888  `"Y88b.  888ooo888 888         888   
 888   888   888  o.  )88b 888    .o 888   .o8   888 . 
o888o o888o o888o 8""888P' `Y8bod8P' `Y8bod8P'   "888" 
"""
print(Style.RESET_ALL)
print(Fore.GREEN +"Wlcome to Insect",VERSION, "please wait to load the proglam...\n",BANNER)
print(Style.RESET_ALL)

# Modules:
os.system('python modules/payload-generator.py > modules/payload.txt')
time.sleep(1)
os.system('python modules/executor.py')

print("\n")
print(Fore.RED +"Please check the output.txt file, there you can find what you were searching for.\n")
print(Style.RESET_ALL)
