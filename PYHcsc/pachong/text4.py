#-*- codeing = utf-8 -*-
#@Time : 2021/3/28 23:08
#@Author : cscnb
#@File : text4.py
#@Software : PyCharm

#图片数据pa
import requests
if __name__ == '__main__':
    url = 'https://wallroom.io/img/1920x1200/bg-627da7f.jpg'
    #content返回的是二进制形式的图片数据
    img_data = requests.get(url).content
    print(img_data)