import os
import io

path = r"/home/andrew/Documents/code/python/python-remove-empty-directories/test"

def deletesFolders(empty_dirs):
    for folder in empty_dirs:
        os.removedirs(folder)

def getFolders(folder):
    empty_dirs = []

    for root, dirs, files in os.walk(path):
        if len(dirs) == 0 and len(files) == 0:
            empty_dirs.append(root)

    return empty_dirs

def main(path):
    empty_dirs = getFolders(path)
    deletesFolders(empty_dirs)

if __name__ == "__main__":
    main(path)
