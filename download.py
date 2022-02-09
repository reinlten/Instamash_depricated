import os.path

import wget

f = open("srces.txt", "r")
images = f.readlines()
f.close()

path = os.getcwd()
path = os.path.join(path, "website\static\img")

print(path)
print(images[0])

for i in range(round(len(images)/2)):
    wget.download(images[2*i+1], os.path.join(path, images[2*i].rstrip("\n") + ".jpg"))


