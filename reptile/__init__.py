# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  __init__.py
  Description  :
  Author       :  Edwin
  Date         :  2018/1/7 17:51
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/7 17:51
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import urllib.request


def requests(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    print(data)


if __name__ == '__main__':
    requests('http://www.baidu.com')
