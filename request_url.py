# -*- coding:'utf8' -*-
#encoding=utf-8

import requests
#访问http
headers = {

}

data = {

}

url ='http://www.zhihu.com'

httpSession = requests.Session()

resp = httpSession.post(url, data=data, headers=headers)
cookies = resp.cookies
headers = resp.headers

#将获取的headers和cookies放在下一次的http访问中