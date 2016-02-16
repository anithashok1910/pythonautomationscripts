"""

File renamer.py is a python script which is used to move the files from one location to another.
The name of files that are to be moved from one location to another is specified in a text
file called 'Unsupported Files.txt' and the files that are meant to be moved are unsupported
pdf files from the yesterday's work.
The program should be executed once only after the successful execution as it will give error
if the files and folders already exists or are moved to the location.


INCOMPLETE FILE
WORK IS YET TO BE DONE

first check whether the pdf 's content name is null or not call for function name creater
 to get a proper name without any problems in the name if it is not null then only check
 whether the file name contain the term 'sector' in it, if so then only rename it



"""

import os
import shutil

fileobj = open('Unsupported Files.txt','r')
contents = fileobj.read()

contentlist = contents.split('\n')

os.chdir('H:\\backup\\pdf')

for file in contentlist:
    shutil.rename(file,'H:\\backup\\Unsupported pdf\\')
fileobj.close()