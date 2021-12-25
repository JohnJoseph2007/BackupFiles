import time, os, shutil

path = input("Enter Path: ")
days = time.asctime()

if os.path.exists(path):
    contents = os.listdir(path)
else:
    print("Path does not exist")