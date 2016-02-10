
#  Script file to read all the files of the specified directory and
#  store it in a text file called "file content.txt" in the current
#  working directory

import os
# for functions os.listdir(), os.path.join() and os.path.getsize() functions

fout = open('file contents.txt','w')
# opens the text file or creates if not created of the name "file contents.txt"
# in the current working directory which can be accessed by fout object in
# writing mode

line1 = "File name                 Size \n"
# for giving the heading of the columns (File name and Size)

fout.write(line1)
# writes the above line in the file through its file object (fout)

files = os.listdir('H:\\backup\\docx')
# storing the names of all the files in the files variables in the form of list
# using the os.listdir() function

for file in files:
    # for loop for reading the list's each item and finding each file's size in
    # the directory
    location = os.path.join('H:\\backup\\docx\\',file)
    # stores the complete location in the location variable

    line = file +"     "+ str(os.path.getsize(location)) + "\n"
    # stores the filename along with its size in the variable line
    # os.path.getsize() returns a long value n must be converted
    # to string before writing it into the file

    fout.write(line)
    # the line variables content are written inside the file object (fout) and
    # hence to the the text file ("file contents.txt")

fout.close()
# closes the file object and the file which is opened through the file object
