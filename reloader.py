import os
import sys
import time
import termcolor

script=open("main.py")
initial=script.readlines()
script.close()

while True:
    currentScript=open("main.py","r")
    current=currentScript.readlines()
    if current!=initial:
        #log("Reloading script, change detected.",4)
        os.execv("main.py",sys.argv)
    time.sleep(5)