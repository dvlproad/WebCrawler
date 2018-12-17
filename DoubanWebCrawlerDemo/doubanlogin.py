# _*_coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
import os

global session
session = requests.Session()

def loginin():
	url='https://www.douban.com/accounts/login'
	# name='你的用户名'
	# psw='密码'
	name='913168921@qq.com'
	psw='密码'
	headers={
	"Host":"www.douban.com",
	"User-Agent":"'Mozilla/5.0 (Windows NT 6.1; rv:53.0)Gecko/20100101 Firefox/53.0'",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding":"gzip,deflate",
	"Connection":"keep-alive"
	}
	data={
	'form_email':name,
	'form_password':psw,
	'source':'index_nav',
	'remember':'on'
	}

	captcha = session.get(url, headers = headers, timeout = 30)
	# r = session.get('http://httpbin.org/headers', headers={'x-test2': 'true'}) 
	soup=BeautifulSoup(captcha.content,'lxml')
	img=soup.find_all('img',id='captcha_image')
	print(img)

	if img:
		captcha_url=re.findall('src="(.*?)"',str(img))[0]
		print(u'验证码所在标签为：',captcha_url)
		a=captcha_url.split('&')[0]
		capid=a.split('=')[1]
		print(capid)
		cap=session.get(captcha_url,headers=headers).content
		with open('captcha.jpg','wb') as f:
			f.write(cap)
		f.close()
		im = Image.open('captcha.jpg')
		im.show()
		#print captcha.content
		capimg=input('请输入验证码：')
		newdata={
		'captcha-solution':capimg,
		'captcha-id':capid
		}
		data.update(newdata)
		print(data)
		os.remove('captcha.jpg')
	else:
		print('不存在验证码，请直接登陆')
		r=session.post(url,data=data,headers=headers,timeout=30)
		# print(r.content)
		# print(r.status_code)
		# #print r.cookies
		# html=session.get('https://movie.douban.com/')
		# print(html.status_code)
		# print(html.content)
		# print(html.cookies)


def get_myinfo(url,session):
    """获取个人主页信息"""
    resp=session.get(url)
    if resp.status_code==requests.codes.ok:
        html=resp.text
        # print(html)

        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
        print(soup.title)
        print(soup.title.name)
        print(soup.title.string)
        print(soup.title.parent.name)
        print(soup.p)
        # print(soup.p["class"])
        print(soup.a)
        print(soup.find_all('a'))
        print(soup.find(id='link3'))
        print("\n")
        print("\n")
        print("\n")


if __name__=='__main__':
	loginin()

	myinfo_url='https://www.douban.com/people/188795866/'
	get_myinfo(myinfo_url,session)