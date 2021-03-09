#-*- codeing = utf-8 -*-
#@Time : 2021/3/8 21:09
#@Author : cscnb
#@File : demohanshu.py
#@Software : PyCharm
# def fun(a,b):
#     print('a',a)
#     print('b',b)
#     a=100
#     b.append(10)
#     print('a',a)
#     print('b',b)
# n1=11
# n2=[22,20]
# print(n1)
# print(n2)
# fun(n1,n2)
# print(n1)
# print(n2)
'''在函数调用过程中，进行参数的传递
    如果是不可变对象，在函数体的修改不会影响实参的值
    如果是可变对象，在函数体的修改会影响实参的值
'''
'''1.如果函数没有返回值，return可以省略不写
   2.函数返回值如果是一个，直接返回类型
   3.函数返回值如果是多个，返回的结果为元组 
    '''
# def fun(a,b=10):
#     print(a,b)
# #函数的调用
# fun(100)
# fun(20,30)

# def fun(*args):#可变的位置参数只能是一个
#     print(args)
#     print(args[0])
#
# fun(10)
# fun(10,30)
# fun(2,3,4,5)
#
# def fun1(**args):#个数可变的关键字参数在能是一个
#     print(args)
#
# fun1(a=10)
# fun1(a=50,b=70)

# def fun(a,b=10):
#     print(a)
#     print(b)
#
# def fun2(*args):
#     print(args)
#
# def fun3(**args2):
#     print(args2)
#
# def fun4(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)

# def fun(a,b):
#     c=a+b #c，就称为局部变量，因为c是在函数体内进行定义的变量，a，b为函数的形参，作用范围也是函数内部，相当于局部变量
#     print(c)
#
# name='csc' #name的作用范围为函数内部和外部都可以使用--》称为全局变量
# def fun2():
#     print(name)
# fun2()
#
# def fun3():
#     global  age #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
#     age=20
#     print(age)
# fun3()
# print(age)

#递归
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))