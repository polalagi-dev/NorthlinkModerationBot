import requests
import os
import time

initial=requests.get("https://raw.githubusercontent.com/polalagi-dev/NorthlinkModerationBot/master/main.py").text

os.system("pm2 start main.py --name job1 --interpreter python3 --restart-delay 10000")
time.sleep(1)

while True:
    current=requests.get("https://raw.githubusercontent.com/polalagi-dev/NorthlinkModerationBot/master/main.py").text
    #if current!=initial:
    os.system("pm2 kill")
    time.sleep(1)
    os.system("curl https://raw.githubusercontent.com/polalagi-dev/NorthlinkModerationBot/master/main.py -o main.py")
    #main=open("main.py","w")
    #main.truncate(0)
    #main.write(current)
    initial=current
    #main.close()
    print("Updated main.py")
    time.sleep(1000)
    os.system("pm2 start main.py --name job1 --interpreter python3 --restart-delay 10000")
    print("PM2 restarted")
    time.sleep(300000)