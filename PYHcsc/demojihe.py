#-*- codeing = utf-8 -*-
#@Time : 2021/3/4 19:06
#@Author : cscnb
#@File : demojihe.py
#@Software : PyCharm
#集合的创建方式
#第一种用{}
# s={2,5,7,7}#集合中的元素不可重复
# print(s)
#第二种使用set（）函数
# s1=set(range(6))
# print(s1,type(s1))

#集合的相关操作
#集合元素的判断操作
# s={10,20,30,40}
# print(10 in s)
# print(100 in s)
# print(10 not in s)
#集合元素的新增操作,add一次添加一个元素，update至少添加一个元素
# s.add(80)
# print(s)
# s.update({200,400})
# print(s)
# s.update([500,700])
# s.update((5,7,9))
# print(s)
#集合元素的删除操作
# s.remove(200)
# s.discard(300)
# s.pop()
# print(s)
# s.clear()
# print(s)

#集合间的关系
# s={10,20,30,40}
# s2={30,40,20,10}
# print(s==s2)
# print(s!=s2)
'''一个集合是否是另一个集合的子集'''
