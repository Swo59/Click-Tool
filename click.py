import pyautogui
from datetime import datetime
now = datetime.time(datetime.now())
nowsec = now.hour*60*60 + now.minute*60+ now.second
minutes = int(input("write the number of minutes for the loop"))

thensec = nowsec + minutes*60
isec = nowsec + 10
print(now.strftime("%H:%M:%S"))
while thensec>nowsec :
    now = datetime.time(datetime.now())
    nowsec = now.hour*60*60 + now.minute*60+ now.second
    #print(nowsec)
    if nowsec == isec :
        isec += 60
        print(now.strftime("%H:%M:%S"))
        print("nowclick")
        pyautogui.click(10,10)
