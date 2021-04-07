#-*- codeing = utf-8 -*-
#@Time : 2021/4/6 16:58
#@Author : cscnb
#@File : text7.py
#@Software : PyCharm

#猪八戒网
import requests
from lxml import etree
url = 'https://zhuhai.zbj.com/search/f/?type=new&kw=saas'
zhubajieyuanma = requests.get(url)
tree = etree.HTML(zhubajieyuanma.text)
fangkuang = tree.xpath("/html/body/div[6]/div/div/div[2]/div[6]/div[1]/div")
# print(fangkuang)
for gebufen in fangkuang:
    jiage = gebufen.xpath("./div/div[2]/div[2]/i/text()")
    mingchen = 'saas'.join(gebufen.xpath("./div/div[2]/div[3]/a/text()"))
    