from PIL import Image
from os import listdir, mkdir, getcwd, sep, path
from shutil import move
from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed
from sys import stdout

def picture_resolution_finder():
    print("===Resolution Finder===\n")
    errors = []
    pwd = getcwd() + sep
    source = pwd + "seprate" + sep

    if "seprate" not in listdir("."):
        mkdir("seprate")

    print("First Checking:")
    files = [i for i in listdir(".") if i != "picture_resolution.py" and path.isfile(i)]
    file_found = 0
    file_search = 0
    print("All files : {}".format(len(files)))

    for file in files:
        try:
            image = Image.open(file)
            width, height = image.size
            image.close()

            if width < 100 or height < 100:
                move(file, source + file)
                file_found += 1

        except Exception as e:
            errors.append("{0} ==> {1}".format(file, e))

        file_search += 1
        stdout.write('\r' + str("Files searched : {0} , Files found : {1}".format(file_search, str(file_found))))

    print("\n\nErrors found: ")
    for i in errors:
        print(i)

picture_resolution_finder()
input()
