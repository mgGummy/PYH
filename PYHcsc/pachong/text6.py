#-*- codeing = utf-8 -*-
#@Time : 2021/4/2 11:58
#@Author : cscnb
#@File : text6.py
#@Software : PyCharm
from bs4 import BeautifulSoup
import requests

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)

#解析数据
page = BeautifulSoup(resp.text,"html.parser")#指定html解析器
#从bs里查找数据
# table = page.find("table",class_="hq_table")
table = page.find("table",attrs={"class":"hq_table"})#15.16行上下一个含义
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    data = tds[6].text
    print(name,low,avg,high,gui,kind,data)
