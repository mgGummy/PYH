#-*- codeing = utf-8 -*-
#@Time : 2021/3/30 14:55
#@Author : cscnb
#@File : text5.py
#@Software : PyCharm

#糗事百科
import requests
import re
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.56'
    }
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for yema in range(1,2):
        new_url=format(url%yema)
        pa_text=requests.get(url=new_url,headers=headers).text
        ex='<img src="(.*?)" alt=".*?" class="illustration" width="100%" height="auto">'
        tupian = re.findall(ex,pa_text,re.S)
        print(tupian)