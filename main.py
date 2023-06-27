debug_mode=1

from time import sleep,ctime
import sys,os
import requests
my_address=""
is_error=0

def refresh_ip():
    import requests
    import json
    debug=0
    url="https://dnsapi.cn/Record.Ddns"
    parm={
        "login_token":"你的DNSPod API令牌",
        "format":"json",
        "domain_id":"你的DNSPod域名ID",
        "record_id":"你的DNSPod域名下那条解析的ID",
        "sub_domain":"自定义主机名",
        "record_line":"默认",
    }
    json_recv=requests.post(url=url,data=parm).content.decode()
    result=json.loads(json_recv)
    if debug_mode:print(json.dumps(result))

while True:
    try:
        requests.packages.urllib3.util.connection.HAS_IPV6 = False
        current_address=str(requests.get(url="https://wtfismyip.com/text").text)
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
    sleep(3600)
