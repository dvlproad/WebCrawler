#-*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

import importlib,sys 
importlib.reload(sys)

# 函数
def  printPlistCode():
    #1.得到这个网页的 html 代码 #
    html = urllib.request.urlopen("http://movie.douban.com/chart").read()

    #2.转换 一种格式，方便查找
    #soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html,'lxml')
    print(soup.prettify())
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)
    print(soup.title.parent.name)
    print(soup.p)
    print(soup.p["class"])
    print(soup.a)
    print(soup.find_all('a'))
    print(soup.find(id='link3'))
    print("\n")
    print("\n")
    print("\n")

    #3.  得到 找到的所有 包含 a 属性是class = nbg 的代码块,数组
    liResutl = soup.findAll('a', attrs = {"class" : "nbg"})
    #4.用于拼接每个字典的字符串
    tmpDictM = ''

    #5. 遍历这个代码块  数组
    for li in liResutl:

        #5.1 找到 img 标签的代码块 数组
        imageEntityArray = li.findAll('img')

        #5.2 得到每个image 标签
        for image in imageEntityArray:
            #5.3 得到src 这个属性的 value  后面也一样 类似 key value
            link = image.get('src')
            imageName = image.get('alt')
            #拼接 由于 py中 {} 是一种数据处理格式，类似占位符
            tmpDict = '''@{0}@\"name\" : @\"{1}\", @\"imageUrl\" : @\"{2}\"{3},'''

            tmpDict =  tmpDict.format('{',imageName,link,'}')

            tmpDictM = tmpDictM + tmpDict

    #6.去掉最后一个 , 
    tmpDictM = tmpDictM[0:len(tmpDictM) - 1] #为了能输出原生中文不要进行.encode('utf8')


    #7 拼接全部
    restultStr = '@[{0}];'.format(tmpDictM)

    print(restultStr)


if __name__ == '__main__':
    printPlistCode()