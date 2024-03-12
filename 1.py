# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open(r'C:\Users\ADMIN\Downloads\2.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# creating a page object
for i in range(0,len(pdfReader.pages)):
    pageObj = pdfReader.pages[i]
    file = open(r"C:\Users\ADMIN\Desktop\1.txt",'a',encoding='utf-8')

file.write(pageObj.extract_text())
pdfFileObj.close()
