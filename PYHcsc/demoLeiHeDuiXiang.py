#-*- codeing = utf-8 -*-
#@Time : 2021/3/10 9:21
#@Author : cscnb
#@File : demoLeiHeDuiXiang.py
#@Software : PyCharm
class Student:

    native_name='吉林'

    def __init__(self,name,age):
        self.name=name  #self.name称为实体属性，进行了一个赋值操作，将局部变量的name赋值给实体变量
        self.age=age

    def eat(self):
        print('ccc')
    #静态方法
    @staticmethod
    def method():
        print('')

    #类方法
    @classmethod
    def cm(cls):
        print('')