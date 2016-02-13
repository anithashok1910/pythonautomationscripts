import os
import PyPDF2
import codecs

fileobj = open('PDF files list.txt','w')
fileobj1 = open('Unsupported Files.txt','w')
os.chdir('H:\\backup\\pdf')

files = os.listdir('H:\\backup\\pdf')


for file in files:
     try:
        pdfFileObj = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        line2 = pageObj.extractText()
        splitted = line2.split()
        length = len(splitted)
        Title = ""
        for i in range(0,length):
            Title =  Title + " " + splitted[i].encode("utf-8")
            if i > 3:
                break
        fullline = file + "   " + Title + "\n"
        fileobj.write(fullline)
     except:
         eline = file +  "\n"
         fileobj1.write(eline)
     pdfFileObj.close()


fileobj.close()
fileobj1.close()