import time
from datetime import datetime as dt

host_path="C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com","youtube.com","www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10 )< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working Hours!")
        with open(host_path,'r+') as file:
            content=file.read()
            for w in websites:
                if w in content:
                    pass
                else:
                    file.write(redirect+" "+w+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for l in content:
                if not any(w in l for w in websites):
                    file.write(l)
            file.truncate()

        print("Free Hours..")
    time.sleep(10)

