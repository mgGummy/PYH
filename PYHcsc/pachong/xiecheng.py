#-*- codeing = utf-8 -*-
#@Time : 2021/4/17 20:44
#@Author : cscnb
#@File : xiecheng.py
#@Software : PyCharm

import asyncio
import time
#python协程
async def fun1():
    print("我是")
    # time.sleep(1)
    await asyncio.sleep(3)
    print("我是")

async def fun2():
    print("你是")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("你是")

async def fun3():
    print("她是")
    # time.sleep(3)
    await asyncio.sleep(1)
    print("她是")

# if __name__ == '__main__':
#     f1=fun1()
#     f2=fun2()
#     f3=fun3()
#     tasks={
#         f1,f2,f3
#     }

#     #一次性启动多个任务协程
#     asyncio.run(asyncio.wait(tasks))
#     t1=time.time()
#     t2 = time.time()
#     print(t2-t1)

async def main():#协程函数
    #第一种写法
    #f1 = fun1()
    #await f1  #一般await挂起操作放在协程对象前面
    #(推荐)第二种写法
    task = {
        fun3(),
        fun2(),
        fun1()
    }
    await asyncio.wait(task)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2-t1)
