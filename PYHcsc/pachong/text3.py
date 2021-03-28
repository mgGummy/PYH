#-*- codeing = utf-8 -*-
#@Time : 2021/3/28 10:54
#@Author : cscnb
#@File : text3.py
#@Software : PyCharm

#KFC地点
import requests
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname':'',
        'pid':'',
        'keyword': '深圳',
        'pageIndex': '1',
        'pageSize': '10'
    }

    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.56'
    }
    re=requests.post(url=url,data=data,headers=headers)
    re_text=re.text
    print(re_text)