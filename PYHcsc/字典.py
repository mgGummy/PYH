#-*- codeing = utf-8 -*-
#@Time : 2021/3/3 9:31
#@Author : cscnb
#@File : 字典.py
#@Software : PyCharm
'''字典的创建方式'''
#{}
l={'张三':40,'大哥':70,'csc':66}
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

#获取所有的key
keys=l.keys()
print(keys)
print(type(keys))
#values
va=l.values()
print(va)

#所有的键值对
items=l.items()
print(items)

#字典元素的遍历
for item in l:
    print(item,l[item],l.get(item))