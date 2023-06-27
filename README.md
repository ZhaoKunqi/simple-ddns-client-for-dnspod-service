# 适用于DNSPod API的简易DDNS客户端
A simple DDNS client for DNSPod service based on Python 3.X
![ddns_example_01](https://user-images.githubusercontent.com/110202952/186743035-5257c06f-03ea-453e-9fed-5608509d3330.jpg)

## 通过检查共有API或者自建API来获取，而不是定时向DNS提交更改，以此减少DNS API的调用次数同时提高了在线率。

## 如何更改API密钥等等信息

编辑main.py中以下片段

```
    parm={
        "login_token":"你的DNSPod API令牌",        //在DNSPod的API令牌管理界面可以找到，格式为ID和密钥，实际使用时这里大概是这样子:"114514,114514xjpwinniethepoohqingfengbz"
        "format":"json",        //这条不要改
        "domain_id":"你的DNSPod域名ID",        //通过查询可以查到，一般来说是一个8位数的int整数
        "record_id":"你的DNSPod域名下那条解析的ID",        //通过查询可以查到，一般来说是一个9位数的int整数
        "sub_domain":"自定义主机名",        //主机名，这里一般填写的是一个字符串。比如你的域名是'example.com',然后在自定义主机名这里写'server01',那在这条解析记录添加成功以后就可以通过server01.example.com访问你的服务器
        "record_line":"默认",
    }
```

## 注:如果你是付费用户，不像普通用户一样DNS API调取次数限制的很严格，你是可以直接定时调用DNS API的，这个脚本是提供给免费DNSPod用户方便使用的，并不一定适合付费版DNSPod用户。
