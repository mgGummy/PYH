#-*- codeing = utf-8 -*-
#@Time : 2021/3/16 14:02
#@Author : cscnb
#@File : demowith.py
#@Software : PyCharm
# with open("a.txt",'r') as file: #with可以自动关闭文件，不用手动关闭文件
#     print(file.read())

class MyContenMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MyContenMgr() as file:
    file.show()
