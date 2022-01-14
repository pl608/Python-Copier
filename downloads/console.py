import os, sys

path = sys.argv[1]

dirs = []
files = []

os.chdir(path)
def dirsearch(dir: str):
    global dirs
    for x in os.listdir(dir):
        dirs.append(x)
        dirsearch(os.path.join(path,x))
print(os.listdir(path))
for x in os.listdir(path):
    if os.path.isdir(x):
        dirs.append(x)
        dirsearch(x)
    elif os.path.isfile(x) == True:
        files.append(x)

print(files)
print("#####################")
print(dirs)
