import sys, os
from subprocess import run

def open_(path: str,mode="w", data = ''):
    f = open(path, mode)
    d = ""
    if "w" in mode:
        f.write(data)
        d = 0
    elif "r" in mode:
        d = f.read()
    f.close()
    return d
if __name__=="__main__":
    hasArgs = (len(sys.argv) > 1)
    
    conpath = os.getenv('APPDATA')+"/Python_Copier"+"/console.py"
    guipath = os.getenv('APPDATA')+"/Python_Copier"+"/tkinter.py"
    def download():
        try:
            open(conpath,"r").close()
            open(guipath, "r").close()
        except:
            from requests import get
            os.mkdir(os.getenv('APPDATA')+"/Python_Copier")
            r = get("https://raw.githubusercontent.com/pl608/Python-Copier/main/console.py")
            rr = get("https://raw.githubusercontent.com/pl608/Python-Copier/main/tkinter.py")
            open_(guipath,mode="w",data=rr.text)
            open_(conpath,mode="w",data=r.text)

    download()
    if hasArgs == True:
        os.system("python "+conpath+" "+sys.argv[1])
    else:
        os.system("python "+guipath)
