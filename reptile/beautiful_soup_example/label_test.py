# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  beautiful_soup_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/12 23:30
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/12 23:30
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from bs4 import BeautifulSoup

html = """
<html><head><title>The dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href=" http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tille" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p >
"""

html1 = """
    <html>
        <head>
            <title>The dormouse's story</title>
        </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href=" http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tille" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
    <p class="story">...</p >
    """


# bs4的基本使用
def bs_demo():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(soup.prettify())
    print(soup.title.string)


# bs4 标签选择器  选择元素
def bs_demo1():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.head.title.string)
    print(soup.p.b.string)


# bs4 标签选择器 获取名称
def bs_demo2():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(soup.title.name)
    print(soup.head.title.string)


# bs4 标签选择器 获取属性值
def bs_demo3():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.attrs['name'])
    print(soup.p['name'])


# bs4 标签选择器 获取内容
def bs_demo4():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.string)


# bs4 标签选择器 嵌套选择
def bs_demo5():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.head.title.string)


# bs4 标签选择器 子节点
def bs_demo6():
    soup = BeautifulSoup(html1, 'lxml')
    print(soup.p.contents)


# bs4 标签选择器 子节点
def bs_demo7():
    soup = BeautifulSoup(html1, 'lxml')
    print(soup.p.children)
    for i, child in enumerate(soup.p.children):
        print(i, child)


# bs4 标签选择器  子孙节点
def bs_demo8():
    soup = BeautifulSoup(html1, 'lxml')
    print(soup.p.descendants)
    for i, child in enumerate(soup.p.descendants):
        print(i, child)


# bs4 标签选择器 父节点
def bs_demo9():
    soup = BeautifulSoup(html1, 'lxml')
    print(soup.a.parent)


# bs4 标签选择器 获取所有祖先节点
def bs_demo10():
    soup = BeautifulSoup(html1, 'lxml')
    print(list(enumerate(soup.a.parents)));


# bs4 标签选择器 获取兄弟节点
def bs_demo11():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.a.previous_sibling)
    print(list(enumerate(soup.a.previous_siblings)))
    print(soup.a.next_sibling)
    print(list(enumerate(soup.a.next_siblings)))


if __name__ == '__main__':
    bs_demo11()
