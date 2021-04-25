import psutil
from pypresence import Presence
import time

client_id = 'Your Client id here' #to find your client id go to application and copy client id
RPC = Presence(client_id,pipe=0)
RPC.connect()

while True:
    cpu_per = round(psutil.cpu_percent(),1)
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    RPC.update(state="RAM: "+str(mem_per)+"%", details="CPU: "+str(cpu_per)+"%",large_image='Your image asset name',large_text='CPU = Your cpu name',buttons=[{"label": "Check My CPU!","url": "your cpu web"},{"label": "Check My RAM!", "url": "your ram web"}])
    print(f"CPU: {cpu_per}% RAM: {mem_per}%")#image asset name is name of presence asset at application
    time.sleep(0.1)
