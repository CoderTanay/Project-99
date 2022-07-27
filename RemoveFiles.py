import os
import shutil
import time

def main():
    path = input("Enter File Path Here: ")
    days = 30
    seconds = time.time() - (days * 60 * 60 * 24)

    if os.path.exists(path):
        for subfolders, folders, files in os.walk(path):
            if seconds >= age(subfolders):
                folderGone(subfolders)
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(subfolders, folder)
                    if seconds >= age(folderPath):
                        folderGone(folderPath)
                for file in files:
                    filePath = os.path.join(subfolders, file)
                    if seconds >= age(filePath):
                        fileGone(filePath)
        else:
            if seconds >= age(path):
                fileGone(path)
    else:
        print('The file path is invalid')
    print("Files and folders were deleted")

def folderGone(path):
    if not shutil.rmtree(path):
        print("The file path is removed successfully")
    else:
        print("File path is not there")

def fileGone(path):
    if not os.remove(path):
        print("The file path is removed successfully")
    else:
        print("File path is not there")

def age(path):
    ctime = os.stat(path).st_ctime
    return ctime

main()