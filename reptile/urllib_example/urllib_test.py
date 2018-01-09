# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  urllib_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/9 21:45
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/9 21:45
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import http.cookiejar as cookie_jar
import urllib.error as error
import urllib.parse as parse
import urllib.request as req
import socket


def requests():
    response = req.urlopen('http://www.baidu.com')
    print(response.read().decode('utf-8'))


def requests1():
    data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
    response = req.urlopen('http://httpbin.org/post', data=data, timeout=5)
    print(response.read())


def request2():
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    dicts = {'name': 'Edwin', "age": 20}
    data = bytes(parse.urlencode(dicts), encoding='utf-8')
    request = req.Request(url=url, headers=headers, data=data, method='POST')
    response = req.urlopen(request)
    print(response.read().decode('utf-8'))


def response():
    response = req.urlopen('https://www.python.org')
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))


def cookies():
    cookie = cookie_jar.CookieJar()
    handler = req.HTTPCookieProcessor(cookie)
    opener = req.build_opener(handler)
    opener.open('http://www.baidu.com')
    for item in cookie:
        print('key = %s, value = %s' % (item.name, item.value))


def save_cookie():
    filename = 'cookie.txt'
    cookie = cookie_jar.MozillaCookieJar(filename)
    handler = req.HTTPCookieProcessor(cookie)
    opener = req.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


def save_cookie1():
    # MozillaCookieJar与LWPCookieJar这两个类对应的标准不同而已
    filename = 'cookies.txt'
    cookie = cookie_jar.LWPCookieJar(filename)
    handler = req.HTTPCookieProcessor(cookie)
    opener = req.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


def read_cookie():
    cookie = cookie_jar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    handler = req.HTTPCookieProcessor(cookie)
    opener = req.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))


def error1():
    try:
        response = req.urlopen('http//www.baodu.com')
    except error.URLError as e:
        print(e.reason)


def error2():
    try:
        response = req.urlopen('http://www.baodu.com')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print("Request Successfully")


def error3():
    # 设置超时时长为0.01秒 为了测试超时异常情况
    try:
        response = req.urlopen('http://www.baidu.com', timeout=0.01)
    except error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT!')


if __name__ == '__main__':
    error3()
