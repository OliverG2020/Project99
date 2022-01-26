import os
import shutil

source=input("entersourcefoldername")
destination=input("destination")
source=source+"/"
destination=destination+"/"

list_of_files = os.listdir(source)
for files in list_of_files:
    shutil.copy((source+files),destination)


