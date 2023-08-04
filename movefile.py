import os
import shutil

from_dir = "C:/Users/IPSHITA/Downloads"              
to_dir = "C:/Users/IPSHITA/Desktop/document"

list_of_files = os.listdir(from_dir)
print("list of files in the source location: " , list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    print("NAME of FILE: ",name)
    print("EXTENSION of FILE: ",extension)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:

        path1 = from_dir + '/' + file_name                             
        path2 = to_dir + '/' + "Document_Files"                           
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   
        print("path1:  " ,path1)
        print("path2:  ", path2)
        print("path3:  ", path3)

        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

         
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)  