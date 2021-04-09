#-*- codeing = utf-8 -*-
#@Time : 2021/4/8 22:18
#@Author : cscnb
#@File : text9.py
#@Software : PyCharm

#代理ip
import requests
proxies = {
    "https":"120.42.167.160:8080"
}
res = requests.get("https://www.baidu.com/",proxies=proxies)
res.encoding = "utf-8"
print(res.text)
