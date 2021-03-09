#-*- codeing = utf-8 -*-
#@Time : 2021/3/9 21:37
#@Author : cscnb
#@File : demobug.py
#@Software : PyCharm
# try:
#     a=int(input('第一个整数'))
#     b=int(input('第二个整数'))
#     result=a/b
#     print('结果为：',result)
# except ZeroDivisionError:
#     print('不能除以0')
# except ValueError:
#     print('请输入数字')
#
# print('程序结束')
#try...except..else
#没有错误就走else，有错误就走except
#try...except..else...finally
#finally有没有错误都会走
# try:
#     a=int(input('第一个整数'))
#     b=int(input('第二个整数'))
#     result=a/b
# except BaseException as e:
#     print('出错了：',e)
# else:
#     print('结果为;',result)
#
# print('程序结束')

#traceback模块
import traceback
try:
    print('.....')
    print(1/0)
except:
    traceback.print_exc()