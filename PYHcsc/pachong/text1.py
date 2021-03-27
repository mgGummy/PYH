#-*- codeing = utf-8 -*-
#@Time : 2021/3/26 22:37
#@Author : cscnb
#@File : text1.py
#@Software : PyCharm

#百度翻译
import requests
if __name__ == '__main__':
    post_url='https://fanyi.baidu.com/sug'
    #进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.56'
    }
    #post请求参数处理（同get一致）
    word=input('enter a word')
    data = {
        'kw':word
    }

    response = requests.post(url=post_url,data=data,headers=headers)
    #获取响应数据：json()方法返回的是对象（需要确认响应的数据是json类型的，才可以使用json()）
    dic_obj=response.json()
    print(dic_obj)