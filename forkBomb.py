import subprocess
import sys
import os 
import platform

system = platform.system()
i = 0

def windows(i):
    subprocess.Popen([sys.executable,sys.argv[0]],creationflags=subprocess.CREATE_NEW_CONSOLE)
    while i != 6:
        i+=1
        subprocess.Popen([sys.executable,sys.argv[0]],creationflags=subprocess.CREATE_NEW_CONSOLE)
        if i == 6:
            break

def unix(i):
    os.fork()
    while i != 6:
        i += 6
        os.fork()
        if i == 6:
            break

if __name__ == "__main__":
    if system == "Windows":
        windows(i)
    elif system == "Linux" or system == "Darwin":
        unix(i)