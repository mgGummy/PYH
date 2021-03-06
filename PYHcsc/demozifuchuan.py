#-*- codeing = utf-8 -*-
#@Time : 2021/3/5 13:12
#@Author : cscnb
#@File : demozifuchuan.py
#@Software : PyCharm
#字符串的定义
# a='p'
# b="p"
# c='''p'''
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))

#字符串的查询
# s='hello,hello'
# print(s.index('lo'))
# print(s.find('lo'))
# print(s.rindex('lo'))
# print(s.rfind('lo'))

#字符串大小写转换的方法
s='hello,xxx'
a=s.upper()
print(a)
print(s.lower())#小写,转换之后会产生一个新的字符串对象，虽然内容一样
print(id(s))
print(id(s.lower()))
print(s.swapcase())
print(s.capitalize())
print(s.title())