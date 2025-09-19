import pyautogui
from datetime import datetime , timedelta
now = datetime.now()
nowsec = now.hour*60*60 + now.minute*60+ now.second
minutes = int(input("write the number of minutes for the loop"))
end_time = nowsec + minutes*60

end_time = now + timedelta(minutes=minutes)

print("time at end = ", end_time ) #.strftime("%H:%M:%S"))

thensec = nowsec + minutes*60
isec = nowsec + 10
print(now.strftime("%H:%M:%S"))
while thensec>nowsec :
    now = datetime.time(datetime.now())
    nowsec = now.hour*60*60 + now.minute*60+ now.second
    #print(nowsec)
    if nowsec == isec :
        isec += 30
        print(now.strftime("%H:%M:%S"))
        print("now click")
        pyautogui.click(10,10)


