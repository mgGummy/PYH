#-*- codeing = utf-8 -*-
#@Time : 2021/3/16 15:24
#@Author : cscnb
#@File : demoOSmokuai.py
#@Software : PyCharm
#os模块与操作系统相关的模块
import os
# os.system('notepad.exe')
# os.system('calc.exe')
#直接调用可执行文件
# os.startfile('')

# print(os.getcwd())
# lst=os.listdir('../PYHcsc')
# print(lst)

# os.mkdir('')#创建目录
# os.makedirs('A/B/C')#创建多级目录
# os.rmdir('')#删除目录
# os.removedirs('')#移除多级目录
# os.chdir('')


#os.path模块的常用方法
# import os.path
# print(os.path.abspath('yuanzu.py'))#获取绝对路径
# print(os.path.exists('yuanzu.py'))


path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
