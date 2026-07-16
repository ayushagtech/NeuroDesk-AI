import subprocess
import shutil
from pathlib import Path 
import os

def find_in_path(application):
    return shutil.which(application)

def search_common_locations(application):
    common_locations=[
        "C:\Program Files",
        "C:\Program Files (x86)",
        Path.home()/"AppData"/"Local"
    ]
    target=application+".exe"
    for location in common_locations:
        for root,dirs,files in os.walk(location):
            if(target in files):
                return Path(root)/target
    return None

def find_application(application):
    path=find_in_path(application)
    if path is not None:
        return path
    path=search_common_locations(application)
    if path is not None:
        return path
    return None

def open_application(command):
    application=" ".join(command.split()[1:])

    path=find_application(application)
    if path is not None:
        subprocess.Popen(path)
    else:
        print("Application Not Found")
            

open_application("open code")