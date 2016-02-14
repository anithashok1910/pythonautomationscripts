"""

File mover.py is a python script which is used to move the files from one location to another.
The name of files that are to be moved from one location to another is specified in a text
file called 'Unsupported Files.txt' and the files that are meant to be moved are unsupported
pdf files from the yesterday's work.
The program should be executed once only after the successful execution as it will give error
if the files and folders already exists or are moved to the location.

"""

import os
import shutil

fileobj = open('Unsupported Files.txt','r')
contents = fileobj.read()

contentlist = contents.split('\n')

os.chdir('H:\\backup\\pdf')

for file in contentlist:
    shutil.move(file,'H:\\backup\\Unsupported pdf\\')
fileobj.close()