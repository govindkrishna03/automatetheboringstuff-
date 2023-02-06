import PyPDF2
import os
import sys
from PyPDF2.utils import PdfReadError as err


def deleteOriginalPDF(savedPDF):
    pdfFile = open(f'{foldername}\{savedPDF}', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.isEncrypted:
        pdfReader.decrypt(password)
    if pdfReader.getPage(0):
        pdfFile.close()
        os.unlink(f'{foldername}\{originalPDF}')
        print(f'{originalPDF} has been deleted')
    else:
        print(f'{savedPDF} is invald \nso {originalPDF} hasn\'t deleted ')
   
def encryptOrDecryptPDF():
    pdfFile = open(f'{foldername}\{originalPDF}', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    if pdfReader.isEncrypted:
        pdfReader.decrypt(password)
        savedPDF = f'{originalPDF[:-14]}.pdf'
        print(f'{originalPDF} has been decrypted as {savedPDF}')
    else:
        savedPDF = f'{originalPDF[:-4]}_encrypted.pdf'
        print(f'{originalPDF} has been encrypted as {savedPDF}')
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    if not pdfReader.isEncrypted:
        pdfWriter.encrypt(password)
    resultPdf = open(f'{foldername}\{savedPDF}', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    pdfFile.close()
    deleteOriginalPDF(savedPDF)


if len(sys.argv) == 3 and sys.argv[2]:    
    folderPath, password = sys.argv[1], sys.argv[2]
    if os.path.isdir(folderPath):
        for foldername, _, filenames in os.walk(folderPath):
            for originalPDF in filenames:
                if originalPDF.endswith('.pdf'):
                    try:
                        encryptOrDecryptPDF()
                    except err:
                        print(f'Password for {originalPDF} is incorrect')
                        continue    
    else:
        print('Invalid folderPath')                
else:
    print('Please enter arguments as example:\
        \nfolderPath password')