#-*- codeing = utf-8 -*-
#@Time : 2021/3/3 9:31
#@Author : cscnb
#@File : 字典.py
#@Software : PyCharm
'''字典的创建方式'''
#{}
l={'张三':40}
print(l)
#dict函数
li=dict(name='李四',age=50)
print(li)
'''获取字典的元素
'''
#第一种，使用[]
print(l['张三'])
#第二种，用get函数
print(l.get('张三'))
print(l.get('牛逼',99))#99是没有对应的value不存在的默认值

#in和 not in
print('张三' in l)
print('40' in l)