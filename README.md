# 适用于DNSPod API的简易DDNS客户端
A simple DDNS client for DNSPod service based on Python 3.X
![ddns_example_01](https://user-images.githubusercontent.com/110202952/186743035-5257c06f-03ea-453e-9fed-5608509d3330.jpg)

## 通过检查共有API或者自建API来获取，而不是定时向DNS提交更改，以此减少DNS API的调用次数同时提高了在线率。

## 如何更改API密钥等等信息

编辑refresh.py中以下片段

```
    parm={
        "login_token":"你的DNSPod API令牌",       //比如
        "format":"json",
        "domain_id":"你的DNSPod域名ID",
        "record_id":"你的DNSPod域名下那条解析的ID",
        "sub_domain":"自定义主机名",
        "record_line":"默认",
    }
```

## 注:如果你是付费用户，不像普通用户一样DNS API调取次数限制的很严格，完全可以直接定时调用DNS API的。
