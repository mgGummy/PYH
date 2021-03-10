#-*- codeing = utf-8 -*-
#@Time : 2021/3/10 9:21
#@Author : cscnb
#@File : demoLeiHeDuiXiang.py
#@Software : PyCharm

#类
class Student:

    native_name='吉林' #直接写在类里的变量，称为类属性

    def __init__(self,name,age):
        self.name=name  #self.name称为实体属性，进行了一个赋值操作，将局部变量的name赋值给实体变量
        self.age=age

    def eat(self):
        print('ccc')
    #静态方法
    @staticmethod
    def method():
        print('我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法')

#对象的创建
syu1=Student('张三',20)
print(id(syu1))
print(type(syu1))
print(syu1)
#下面两个代码意思相同
syu1.eat()
Student.eat(syu1)

#类属性的使用方式
print(Student.native_name)
stu1=Student('csc',18)
stu2=Student('FBI',19)
print(stu1.native_name)
print(stu2.native_name)
Student.native_name='北京'
print(stu1.native_name)
print(stu2.native_name)
stu1.native_name='上海'
print(stu1.native_name)
print(stu2.native_name)

print('------类方法的使用方式------')
Student.cm()
print('------静态方法的使用方式------')
Student.method()