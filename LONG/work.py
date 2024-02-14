import glob
import os

def check(str) :
    return str.replace("a.",".").replace("png","jpg")

names = ["blueboy", "dressage", "rat"]

for name in names :
  
    path = "JPEGImages/480p/" + name + "/*.jpg"

    image_files = glob.glob(path)
    image_files.sort()
    print(image_files)

    for p in image_files :
        if len(p.replace("a.", ".")) != len(p) :
            os.rename(p, p.replace("a.", "."))
        else :
            os.remove(p)



    