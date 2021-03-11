#-*- codeing = utf-8 -*-
#@Time : 2021/3/10 9:21
#@Author : cscnb
#@File : demoLeiHeDuiXiang.py
#@Software : PyCharm

#类
# class Student:
#
#     native_name='吉林' #直接写在类里的变量，称为类属性
#
#     def __init__(self,name,age):
#         self.name=name  #self.name称为实体属性，进行了一个赋值操作，将局部变量的name赋值给实体变量
#         self.age=age
#
#     def eat(self):
#         print('ccc')
#     #静态方法
#     @staticmethod
#     def method():
#         print('我是静态方法')
#
#     #类方法
#     @classmethod
#     def cm(cls):
#         print('我是类方法')
#
# #对象的创建
# syu1=Student('张三',20)
# print(id(syu1))
# print(type(syu1))
# print(syu1)
# #下面两个代码意思相同
# syu1.eat()
# Student.eat(syu1)
#
# #类属性的使用方式
# print(Student.native_name)
# stu1=Student('csc',18)
# stu2=Student('FBI',19)
# print(stu1.native_name)
# print(stu2.native_name)
# Student.native_name='北京'
# print(stu1.native_name)
# print(stu2.native_name)
# stu1.native_name='上海'
# print(stu1.native_name)
# print(stu2.native_name)
#
# print('------类方法的使用方式------')
# Student.cm()
# print('------静态方法的使用方式------')
# Student.method()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print(self.name + '在吃饭')
#
# stu1=Student('张三',20)
# stu2=Student('李四',30)
# print('---为stu1动态绑定性别属性---')
# stu1.gender='女'
# print(stu1.name,stu1.age,stu1.gender)
# print(stu2.name,stu2.age)
#
# def show():
#     print('定义在类之外的，称函数')
# stu1.show=show
# stu1.show()
# #stu2.show()这个无法运行

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #age不希望在类的外部使用，所以加了__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',12)
stu.show()
#print(stu.__age)  加了__无法在类的外部使用
#print(dir(stu))
print(stu._Student__age)#在外部还是可以靠这种方法访问

#继承
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self,name,age,xuehao):
#         super().__init__(name,age)
#         self.xuehao=xuehao
#
# class Teacher(Person):
#     def __init__(self,name,age,jiaonian):
#         super().__init__(name,age)
#         self.jiaonian=jiaonian

#多继承
class A(object):
    pass
class B():
    pass
class C(A,B):
    pass


#方法重写
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,xuehao):
        super().__init__(name,age)
        self.xuehao=xuehao
    def info(self):
        super().info()
        print(self.xuehao)


class Teacher(Person):
    def __init__(self,name,age,jiaonian):
        super().__init__(name,age)
        self.jiaonian=jiaonian
    def info(self):
        super().info()
        print(self.jiaonian)

stu=Student('张三',20,'1101')
stu.info()