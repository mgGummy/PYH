#-*- codeing = utf-8 -*-
#@Time : 2021/3/8 21:09
#@Author : cscnb
#@File : demohanshu.py
#@Software : PyCharm
def fun(a,b):
    print('a',a)
    print('b',b)
    a=100
    b.append(10)
    print('a',a)
    print('b',b)
n1=11
n2=[22,20]
print(n1)
print(n2)
fun(n1,n2)
print(n1)
print(n2)
'''在函数调用过程中，进行参数的传递
    如果是不可变对象，在函数体的修改不会影响实参的值
    如果是可变对象，在函数体的修改会影响实参的值
'''