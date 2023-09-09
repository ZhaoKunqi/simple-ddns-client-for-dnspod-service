# 适用于DNSPod API的简易DDNS客户端

## Friendly reminder:

Using this Python script it's not recommend if your Homelab(or any other use case) server is out side china(ccp china).

If you are outside mainland china(ccp china) for example taiwan(Republic of China), it's better to use CloudFlare API for your application.

![ddns_example_01](https://user-images.githubusercontent.com/110202952/186743035-5257c06f-03ea-453e-9fed-5608509d3330.jpg)

通过检查公开的IP查询API或者自建API来获取，而不是定时向DNS提交更改，以此减少DNS API的调用次数同时提高了在线率。

## 场景

在我的场景中使用了一个X86的节能NAS作为执行DDNS脚本的服务器，和我对外提供服务的服务器处于同一个公网IP下。

这台小电脑使用的是CentOS Stream 9作业系统，以及其系统内置的Python 3(3.9或3.11)

绝大部分CPU架构的机器都可以，比如树莓派(Raspberry Pi)或者香橙派，你也可以运行在虚拟机内等等方式

## 下载脚本文件和Systemd Service文件

你需要下载的文件取决于你的部署方式，如果你不想用Systemd，也可以用其他你喜欢的任何方法。

在这个帮助文件中我会使用Systemd的Service Unit来运行这个脚本

```
[root@server07 ~]# sudo useradd -m ddns  //首先我们创建一个单独的用户'ddns'
[root@server07 ~]# su - ddns  //进入ddns用户
[ddns@server07 ~]$ mkdir dnspod-ddns
[ddns@server07 ~]$ cd dnspod-ddns
[ddns@server07 dnspod-ddns]$ wget https://raw.githubusercontent.com/ZhaoKunqi/simple-ddns-client-for-dnspod-service/main/main.py
[ddns@server07 dnspod-ddns]$ vim main.py //编辑这个文件
//编辑这个文件以下部分，需要更改的地方已经标注
    parm={
        "login_token":"你的DNSPod API令牌",        //在DNSPod的API令牌管理界面可以找到，格式为ID和密钥，实际使用时这里大概是这样子:"114514,114514xjpwinniethepoohqingfengbz"
        "format":"json",        //这条不要改
        "domain_id":"你的DNSPod域名ID",        //通过查询可以查到，一般来说是一个8位数的int整数
        "record_id":"你的DNSPod域名下那条解析的ID",        //通过查询可以查到，一般来说是一个9位数的int整数
        "sub_domain":"自定义主机名",        //主机名，这里一般填写的是一个字符串。比如你的域名是'example.com',然后在自定义主机名这里写'server01',那在这条解析记录添加成功以后就可以通过server01.example.com访问你的服务器
        "record_line":"默认",
    }
//更改完后保存退出

[ddns@server07 dnspod-ddns]$ exit //返回到root用户

//下载Systemd Service文件到指定目录
[root@server07 ~]# wget -O /etc/systemd/system/dnspod-ddns.service https://raw.githubusercontent.com/ZhaoKunqi/simple-ddns-client-for-dnspod-service/main/dnspod-ddns.service
[root@server07 ~]# systemctl enable --now dnspod-ddns.service
//在运行完后，请使用systemctl status dnspod-ddns 来检查一下服务是否正常运行，如果没有报错的话那就说明服务已经开始运行并且设置为了开机自启
```

## 注:如果你是付费用户，不像普通用户一样DNS API调取次数限制的很严格，你是可以直接定时调用DNS API的，这个脚本是提供给免费DNSPod用户方便使用的，并不一定适合付费版DNSPod用户。
