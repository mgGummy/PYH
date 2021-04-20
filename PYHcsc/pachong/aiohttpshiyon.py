#-*- codeing = utf-8 -*-
#@Time : 2021/4/18 15:33
#@Author : cscnb
#@File : aiohttpshiyon.py
#@Software : PyCharm

import asyncio
import aiohttp

urls = {
    "https://wallroom.io/img/1920x1080/thumb/bg-cf54c1a.jpg",
    "https://wallroom.io/img/1920x1200/thumb/bg-5fa37c6.jpg"
    # "https://gimg2.baidu.com/image_search/src=http%3A%2F%2F1812.img.pp.sohu.com.cn%2Fimages%2Fblog%2F2009%2F11%2F18%2F18%2F8%2F125b6560a6ag214.jpg&refer=http%3A%2F%2F1812.img.pp.sohu.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1621328112&t=202e84fcfa0b467a55d82dd15bb5c859"
}

async def aiodown(url):
    # s=aiohttp.ClientSession #相当于原来的request模块
    name = url.split("/",6)[6]
    print(name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name,mode="wb") as f:
                f.write(await resp.content.read())   #读取内容是异步的，需要await挂起
    print(name,"搞定")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodown(url)))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())