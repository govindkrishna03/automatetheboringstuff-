import os
from PIL import Image as img

for foldername, subfolders, filenames in os.walk('/home/govind/automatetheboringstuff/Chapter-19/'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        filename=os.path.join(foldername,filename)
        if not(filename.endswith('.jpg') or filename.endswith('.png')):
          numNonPhotoFiles+=1
          continue
        else:
            image=img.open(filename)
            width,height= image.size
            if not(width>500 and height >500):
                numNonPhotoFiles+=1
                continue
            else:
                numPhotoFiles+=1
    if numPhotoFiles>(numPhotoFiles+numNonPhotoFiles)/2:
        print(f"'{foldername}' is a folder with images!!")

