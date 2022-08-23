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
    if debug:print(json.dumps(result))
