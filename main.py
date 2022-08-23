debug_mode=0

from time import sleep,ctime
from refresh import refresh_ip
import sys,os
import requests
my_address=""
is_error=0
while True:
    try:
        current_address=str(requests.get(url="https://myip.wtf/text").text)
        is_error=0
    except:
        is_error=1
        if debug_mode:
            sys.stdout.write(ctime()+":[Disconnect]Network Error  ")
    if not my_address:
        if debug_mode:
            sys.stdout.write(ctime()+":[New_Process]current_address:"+current_address+"\n")
        my_address = current_address
        refresh_ip()
    elif my_address!=current_address:
        if debug_mode:
            sys.stdout.write(ctime()+":[New_IP]old_address: "+my_address+"\n")
            sys.stdout.write(ctime()+":[New_IP]current_address: "+current_address+"\n")
        refresh_ip()
        my_address = current_address
    elif is_error:
        if debug_mode:
            sys.stdout.write("waiting for connected......\n")
    elif my_address == current_address:
        if debug_mode:
            sys.stdout.write(ctime()+":[Normal]Status Normal,IP not change.\n")
    sleep(60)
