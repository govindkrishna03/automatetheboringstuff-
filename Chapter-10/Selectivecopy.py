import os, shutil

def moveFileType(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        for subfolder in subfolders:
            for filename in filenames:
                if filename.endswith('.jpg'):
                    shutil.copy(folder + filename, '/home/govind/automatetheboringstuff/Chapter-10')

moveFileType('/home/govind/automatetheboringstuff/Chapter-10')