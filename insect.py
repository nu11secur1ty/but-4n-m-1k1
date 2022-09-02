#!/usr/bin/python
# Author nu11secur1ty
import os
import time
from datetime import datetime
timestamp = datetime.now().strftime("%H:%M:%S")

os.system('python modules/payload-generator.py > payload.txt')
time.sleep(3)
os.system('python modules/executor.py')
