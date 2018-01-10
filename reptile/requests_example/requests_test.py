# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  requests_example
  Description  :
  Author       :  Edwin
  Date         :  2018/1/10 22:54
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/10 22:54
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import json
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectTimeout
from requests.exceptions import ConnectionError


def request_get():
    response = requests.get('http://www.baidu.com')
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)
    for item in response.cookies:
        print('key = %s, value = %s' % (item.name, item.value))


def request_get1():
    response = requests.get('http://httpbin.org/get')
    print(response.text)


def request_params():
    response = requests.get('http://httpbin.org/get?name=edwin&age=25')
    print(response.text)


def request_params1():
    data = {
        'name': 'Edwin',
        'age': 25
    }
    response = requests.get(url='http://httpbin.org/get', params=data)
    print(response.text)


# 解析json数据
def request_json():
    data = {
        'name': 'Edwin',
        'age': 25
    }
    response = requests.get(url='http://httpbin.org/get', params=data)
    print(type(response.json()))
    print(response.json())
    print(json.loads(response.text))


# 获取二进制数据
def request_bytes():
    response = requests.get('https://github.com/favicon.ico')
    print(type(response.text), type(response.content))
    print(response.text)
    print(response.content)


def request_bytes1():
    response = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(response.content)
        f.close()


def request_headers():
    response = requests.get(url='http://www.zhihu.com/expiore')
    print(response.text)


def request_headers1():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/'
                      '1.53.4295.400 QQBrowser/9.7.12661.400'
    }
    response = requests.get(url='http://www.zhihu.com/expiore', headers=headers)
    print(response.text)


def request_post():
    data = {
        'name': "Edwin",
        'age': 19
    }
    response = requests.post('http://httpbin.org/post', data=data)
    print(response.text)


def request_post1():
    data = {
        'name': "Edwin",
        'age': 19
    }
    response = requests.post('http://httpbin.org/post', data=data)
    print(response.json())


def response_():
    response = requests.get('http://www.jianshu.com')
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.history), response.history)
    print(type(response.url), response.url)


# 获取状态码
def response_status_code():
    response = requests.get('https://www.jiansh.com')
    exit() if not response.status_code == requests.codes.ok else print('Request Successfully!')


# 上传文件
def post_file():
    files = {
        'file': open('favicon.ico', 'rb')
    }
    response = requests.post('http://httpbin.org/post', files=files)
    print(response.text)


# 获取cookies
def request_cookies():
    response = requests.get('https://www.baidu.com')
    print(response.cookies)
    for item in response.cookies:
        print('name = %s, value = %s' % (item.name, item.value))


# 会话维持
def request_sessions():
    requests.get('http://httpbin.org/cookies/set/number/123456789')
    response = requests.get('http://httpbin.org/cookies')
    print(response.text)


# 会话维持
def request_sessions1():
    session = requests.session()
    session.get('http://httpbin.org/cookies/set/number/123456789')
    response = session.get('http://httpbin.org/cookies')
    print(response.text)


# 证书验证
def request_cert():
    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)


# 超时设置
def request_timeout():
    response = requests.get('http://www.taobao.com', timeout=0.01)
    print(response.status_code)


# 超时异常捕获
def request_timeout1():
    try:
        response = requests.get('http://www.taobao.com', timeout=0.01)
        print(response.status_code)
    except ReadTimeout:
        print('ReadTimeout')
    except ConnectTimeout:
        print('ConnectTimeout')
    except ConnectionError:
        print('ConnectionError')


def request_auth():
    response = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
    print(response.status_code)


def request_auth1():
    response = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
    print(response.status_code)


if __name__ == '__main__':
    request_auth1()
