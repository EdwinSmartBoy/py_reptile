# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  pq_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/20 23:40
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/20 23:40
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from pyquery import PyQuery as pq

html = '''
    <div>
        <ul>
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
'''


# 字符串初始化
def get_attr():
    doc = pq(html)
    print(doc('li'))


# URL初始化
def parse_url():
    doc = pq(url='http://www.baidu.com')
    print(doc)
    print(doc('head'))


# 文件初始化
def parse_text():
    doc = pq(filename='demo.html')
    print(doc('li'))

if __name__ == '__main__':
    parse_text()
