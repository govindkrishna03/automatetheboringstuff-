import PyPDF2

pdfFile = open('', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for i in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(i))
password = input('Please enter one word as a password: ')
pdfWriter.encrypt('password')
resultPdf = open('combinedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
print(pdfReader.isEncrypted)
dict = open('dictionary.txt')
dict_x= dict.read().splitlines()

lstDict = []
for word in dict_x:
    lstDict.extend(word.split())

PdfFile2 = open('encrypted.pdf', 'rb')
pdfReader2 = PyPDF2.PdfFileReader(PdfFile2)
print(pdfReader2.isEncrypted)

for word in lstDict:
    if pdfReader2.decrypt(word) == 1:
        break
        print(word)
    elif pdfReader2.decrypt(word.lower()) == 1:
        break
        print(word)