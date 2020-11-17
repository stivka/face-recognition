import os
from os.path import join
import pathlib

path = "./img/known"

for root, dirs, files in os.walk(path):
  folder_name = os.path.basename(root)
  print("folder name: " + folder_name)
  
  count = 0

  for file in files:
    print("file name: " + file)
    
    count = count + 1
    
    extension = file.split(".")[-1]
    print("extension: " + extension)

    new_file_name = folder_name + str(count) + "." + extension
    
    print("new file name: " + os.path.join(root, new_file_name))
    print("\n")
    
    os.rename(os.path.join(root, file), os.path.join(root, new_file_name))
  
