#-*- codeing = utf-8 -*-
#@Time : 2021/3/27 15:31
#@Author : cscnb
#@File : text2.py
#@Software : PyCharm
import requests
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    # 进行UA伪装
    param = {
        'type':'24',
        'interval_id': '100:90',
        'action':'',
        'start': '20',
        'limit': '20'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.56'
    }

    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()
    print(list_data)