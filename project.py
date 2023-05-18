import os
import shutil

source = "C:/Users/Dell/Downloads"
destination = "D:/Python/class 102"

listOfFile = os.listdir(source)

for filename in listOfFile:
    name,extension = os.path.splitext(filename)
    if extension == '' :
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + filename
        path2 = destination + '/' + 'documentsfiles'
        path3 = destination + '/' + 'documentsfiles' + '/' + filename

        if os.path.exists(path2) :
            print("moving...." + filename)
            shutil.move(path1 , path3)
        else:
            os.makedirs(path2)
            print("moving ....." + filename)
        shutil.move(path1 , path3)


                
