#-*- codeing = utf-8 -*-
#@Time : 2021/3/4 9:25
#@Author : cscnb
#@File : yuanzu.py
#@Software : PyCharm
#元组创建方式
#1
# t=('python','word',98)
# print(t)
# print(type(t))
# #省略小括号,当只有一个元素时后面需要加逗号或者小括号，例如：t=(10,)
# t='python','word',98
# print(t)
# print(type(t))
# #2用内置函数
# t1=tuple(('python','word',98))
# print(t1)
# print(type(t1))

# t=(10,[20,30],9)
# print(t)
# print(type(t))
# print(t[0],type(t[0]),id(t[0]))
# print(t[1],type(t[1]),id(t[1]))
# print(t[2],type(t[2]),id(t[2]))
# '''尝试修改'''
# # t[1]=100  不可以修改，元组不允许修改元素
# t[1].append(100)
# print(t[1],type(t[1]),id(t[1]))

'''元组的遍历'''
t=('py','world',98)
for item in t:
    print(item)
