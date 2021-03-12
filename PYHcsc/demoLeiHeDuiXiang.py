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

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age  #age不希望在类的外部使用，所以加了__
#     def show(self):
#         print(self.name,self.__age)
#
# stu=Student('张三',12)
# stu.show()
# #print(stu.__age)  加了__无法在类的外部使用
# #print(dir(stu))
# print(stu._Student__age)#在外部还是可以靠这种方法访问

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
# class A(object):
#     pass
# class B():
#     pass
# class C(A,B):
#     pass
#
#
# #方法重写
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
#     def info(self):
#         super().info()
#         print(self.xuehao)
#
#
# class Teacher(Person):
#     def __init__(self,name,age,jiaonian):
#         super().__init__(name,age)
#         self.jiaonian=jiaonian
#     def info(self):
#         super().info()
#         print(self.jiaonian)
#
# stu=Student('张三',20,'1101')
# stu.info()

# #多态的实现
# class Animal():
#     def eat(self):
#         print('动物会吃')
#
# class Dog(Animal):
#     def eat(self):
#         print('狗吃屎')
#
# class Cat(Animal):
#     def eat(self):
#         print('猫薄荷')
#
# class Person():
#     def eat(self):
#         print('人吃五谷杂粮')
#
# #定义一个函数
# def fun(obj):
#     obj.eat()
#
# fun(Cat())
# fun(Dog())
# fun(Animal())
# fun(Person())

# #特殊属性
# class A():
#     pass
# class B():
#     pass
# class C(A,B):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# #创建类C的对象
# x=C('jack',20)
# print(x.__dict__)#实例对象的属性字典
# print(C.__dict__)
#
# print(x.__class__)#<class '__main__.C'>输出了对象所属的类
# print(C.__bases__)#C类的父类
# print(C.__base__)
# print(C.__mro__)#类的层次结构
# print(A.__subclasses__())#看子类

# #特殊方法
# class Student():
#     def __init__(self,name):
#         self.name=name
#     def __add__(self, other):
#         return self.name+other.name
#     def __len__(self):
#         return len(self.name)
#
# stu1=Student('张三')
# stu2=Student('李四')
# print(stu1+stu2)
# s=stu1.__add__(stu2)
# print(s)


#__new__与__init_
class Person():
    def __new__(cls, *args, **kwargs):
        print('__new__被调用,cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建对象的id为:{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age
print("object这个类的对象id为{0}".format(id(object)))
print('Person这个类的对象id为{0}'.format(id(Person)))

p1=Person('张三',20)
print('p1这个实例对象id{0}'.format(id(p1)))