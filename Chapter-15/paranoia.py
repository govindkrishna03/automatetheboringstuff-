import os
import PyPDF2 as pdf
import sys

password = sys.argv[-1]
print()
pdfList = []
for folderName, subFolder, filenames in os.walk('/home/govind/automatetheboringstuff/Chapter-15/'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfList.append(os.path.join(folderName,filename))

for pdfFile in pdfList:
    pdfPath = open(pdfFile,'rb')
    pdfReader = pdf.PdfFileReader(pdfPath)
    pdfWriter = pdf.PdfFileWriter()
    pdfName = os.path.basename(pdfFile)
    pdfName = pdfName.strip('.pdf')
    print(pdfName)

    if not pdfReader.isEncrypted:
        pdfWriter.encrypt(password)

        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))

        finalName = pdfName + '_encrypted.pdf'
        resultPdf = open(finalName,'wb')
        pdfWriter.write(resultPdf)
        pdfPath.close()
        resultPdf.close()