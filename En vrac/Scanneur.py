import os
import time
import subprocess

now = time.time()

def supr(folder) :
    files = [os.path.join(folder, filename) for filename in os.listdir(folder)]
    for filename in files:
        if (now - os.stat(filename).st_mtime) > 604800:
            command = "del {0}".format(filename)
            subprocess.call(command, shell=True)

supr(r'C:\Users\yoann.wiss\Desktop\supr')