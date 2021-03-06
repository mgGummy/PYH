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
# s='hello,xxx'
# a=s.upper()
# print(a)
# print(s.lower())#小写,转换之后会产生一个新的字符串对象，虽然内容一样
# print(id(s))
# print(id(s.lower()))
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())

# #字符串内容对齐
# s='hello,wdnmd'
# #居中对齐
# print(s.center(20,'*'))
# #左对齐
# print(s.ljust(20,'*'))
# #右对齐
# print(s.rjust(20,'*'))
# #右对齐，使用0进行填充
# print(s.zfill(20))
# print('-4545'.zfill(8))
#
# #字符串的劈分
# s='hello word wdnmd'
# lst=s.split()
# print(lst)
# s1='hello|word|wdnmd'
# print(s1.split())
# print(s1.split(sep='|'))
# print(s1.split(sep='|',maxsplit=1))
# #rsplit 从右边开始劈分
# print(s.rsplit())
# print(s1.rsplit(sep='|',maxsplit=1))

#字符串判断的相关方法
# s='hello,python'
# print('1.',s.isidentifier())
# print('2.','hello'.isidentifier())
#
# print('\t'.isspace())
#
# print('abc'.isalpha())
# print('张三'.isalpha())
#
# print('123'.isdecimal())
#
# print('123'.isnumeric())
# print('123四'.isnumeric())
#
# print('abcd'.isalnum())
# print('abcd张三123'.isalnum())

#字符串的替换和合并
s='hello wdnmd'
print(s.replace('hello','你好'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))
lst=['hello','python','java']
print('|'.join(lst))
ls=('hello','wdnmd')
print('|'.join(ls))
print('*'.join('cscnb'))

#字符串的比较操作
print('apple'>'app')
print('apple'>'banana')
#函数ord可以获得原始值,ord函数对应chr函数
print(ord('a'),ord('b'))
print(chr(97))
