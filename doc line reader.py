import os
"""
Script to read word (.doc) files and its inner contents n store its first line in a text file

"""

fout = open('doc first lines.txt','w')

files = os.listdir('H:\\backup\\doc')

os.chdir('H:\\backup\\doc')
for file in files:
    fout2 = open(file)
    line1 = fout2.readline(10)
    line = file + "           " + line1 + "\n"
    fout.write(line)
    fout2.close()

fout.close()