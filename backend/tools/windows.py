import subprocess
import shutil

def openApplication(command):
    application=command.split()[1]
    path=shutil.which(application)
    if(path!=None):
        subprocess.Popen(path)
    else:
        print("None")

openApplication("open code")