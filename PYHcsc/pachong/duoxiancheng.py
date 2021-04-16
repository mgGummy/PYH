#-*- codeing = utf-8 -*-
#@Time : 2021/4/14 17:27
#@Author : cscnb
#@File : duoxiancheng.py
#@Software : PyCharm
from threading import Thread
def func():
    for i in range(20):
        print("func",i)
if __name__ == '__main__':
    t = Thread(target=func)
    t.start()

    for i in range(20):
        print("main",i)