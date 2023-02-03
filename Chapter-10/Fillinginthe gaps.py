import os, re, shutil
def fillGap(folder,prefix):



    fileRegex = re.compile(r'(%s)((\d)(\d)(\d))\.txt' % prefix)

    folder = os.path.abspath(folder)


    os.chdir(folder)  

    fileNames = list()
    for filename in os.listdir(folder):
        if re.search(fileRegex, filename):
            fileNames.append(filename)

    fileNames.sort()
    print(fileNames)
    for i in range(len(fileNames)):
        mo = re.search(fileRegex, fileNames[i])
        if int(mo.group(2)) == i + 1:
            continue
        if i + 1 < 10:
            shutil.copy
            newFileName =prefix + '00' + str(i + 1) + '.txt'
            shutil.copy(fileNames[i], newFileName)
            os.unlink(fileNames[i])
        elif i + 1 < 100:
            shutil.copy(fileNames[i], prefix + '0' + str(i+1) + '.txt')
            os.unlink(fileNames[i])
        else:
            shutil.copy(fileNames[i], prefix + str(i+1) + '.txt')
            os.unlink(fileNames[i])

folder = '/home/govind/automatetheboringstuff/Chapter-10'
prefix = 'spam'

fillGap(folder, prefix)