#-*- codeing = utf-8 -*-
#@Time : 2021/3/30 14:55
#@Author : cscnb
#@File : text5.py
#@Software : PyCharm

#糗事百科
import requests
import re
import os
if __name__ == '__main__':
    #创建一个文件夹，保存图片
    if not os.path.exists('./qiutu'):
        os.mkdir('./qiutu')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.56'
    }
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for yema in range(1,2):
        new_url=format(url%yema)
        pa_text=requests.get(url=new_url,headers=headers).text
        ex='<div class="thumb">\n\n<a href=".*?" target="_blank">\n<img src="(.*?)" alt=".*?" class="illustration" width="100%" height="auto">\n</a>\n</div>'
        tupian = re.findall(ex,pa_text,re.S)
        # print(tupian)
        for src in tupian:
            tupian_url = 'https:' + src
            # print(tupian_url)
            img_data = requests.get(url=tupian_url,headers=headers).content
            # print(img_data)
            img_name = src.split('/')[-1]
            imgPath = './qiutu/'+img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print('over！！')

        