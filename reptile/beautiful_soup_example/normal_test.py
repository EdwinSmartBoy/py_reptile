# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  normal_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/14 0:36
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/14 0:36
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from bs4 import BeautifulSoup

html = """
 <div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
 </div>
 """


# find_all 查找指定的标签的所有列 以标签名来查询
def find_all_():
    soup = BeautifulSoup(html, 'lxml')
    print(list(enumerate(soup.find_all('ul'))))
    print(type(soup.find_all('ul')[0]))


# find_all 查找某个标签下的某个字段的所有值 以标签名来查询
def find_all1():
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.find_all('ul'):
        print(ul.find_all('li'))


# find_all 通过属性值来查找所有相关数据
def find_all2():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(id='list-1'))
    print(soup.find_all(class_='element'))


# find_all 通过标签的值来查找相关数据
def find_all3():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(text='Foo'))


# find使用方法与find_all类似 不同点: find返回单个标签 find_all返回所有元素
def find1():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find('ul'))
    print(type(soup.find('ul')))
    print(soup.find('page'))


# BeautifulSoup 其他方法
# 1. find_parents() 返回所有祖先节点, find_parent() 返回直接父节点
# 2. find_next_siblings() 返回后面所有兄弟节点, find_next_sibling() 返回后面第一个兄弟节点
# 3. find_previous_siblings() 返回前面所有兄弟节点, find_next_sibling() 返回前面第一个兄弟节点
# 4. find_all_next() 返回节点后所有符合条件的节点, find_next() 返回第一个符合条件的节点
# 5. find_all_previous 返回节点前所有符合条件的节点, find_previous() 返回第一个符合条件的节点


# css选择器 通过select()直接传入css选择器即可完成选择
def select1():
    soup = BeautifulSoup(html, 'lxml')
    print(soup.select('.panel .panel-heading'))
    print(soup.select('ul li'))
    print(soup.select('#list-2 .element'))
    print(type(soup.select('ul')[0]))


# css选择器  嵌套选择
def select2():
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('ul'):
        print(ul.select('li'))


# css选择器  获取属性
def select3():
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('ul'):
        print(ul['id'])
        print(ul.attrs['id'])


# css选择器  获取属性
def select4():
    soup = BeautifulSoup(html, 'lxml')
    for li in soup.select('li'):
        print(li.text)
        print(li.getText())
        print(li.get_text())

if __name__ == '__main__':
    select4()
