#-*- codeing = utf-8 -*-
#@Time : 2021/4/17 0:31
#@Author : cscnb
#@File : xianchrngchi_he_jinchengchi.py
#@Software : PyCharm
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def fun(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(50):
            t.submit(fun,name=f"线程{i}")
    print("123")