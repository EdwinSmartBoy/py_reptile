# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  pq_css_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/21 1:22
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/21 1:22
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from pyquery import PyQuery as pq

html = '''
    <div class="wrap">   
        <div id="container">
            <ul class="list">
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
            </ul>
        </div>
    </div>   
'''

doc = pq(html)


# 基本的css选择器 id选择器使用# class选择器使用. 标签选择器使用标签名
def parse_css_selector():
    print(doc('#container .list li'))


# 1 查找元素
# 1.1 查找子元素
def query_children_item():
    items = doc('.list')
    print(type(items))
    print(items)
    # 查找当前标签下的所有相关的元素
    lis = items.find('li')
    print(type(lis))
    print(lis)

    # 查找所有的直接子元素 children不指定CSS选择器
    li = items.children()
    print(type(li))
    print(li)
    # 查找所有的直接子元素 children指定CSS选择器
    l = items.children('.active')
    print(type(l))
    print(l)


# 1.2 查找父元素
def query_parents_item():
    items = doc('.list')
    # 查找当前标签的直接父类元素 parent不指定CSS选择器 获取所有直接父类元素
    # container = items.parent()
    # print(type(container))
    # print(container)
    # 查找当前标签的所有父类元素 parents不指定CSS选择器 获取所有父类元素
    # parents = items.parents()
    # print(type(parents))
    # print(parents)
    # 查找当前标签的所有父类元素 parents指定CSS选择器 获取所有父类元素中与设置的CSS选择器相同的元素
    parent = items.parents('.wrap')
    print(type(parent))
    print(parent)


# 1.3 兄弟元素
def query_brother_item():
    # .item-0.active 表示.active与.item-0 并列
    # siblings()可以指定CSS选择器 如不指定,则获取所有相关的数据
    li = doc('.list .item-0.active')
    print(li.siblings())
    # siblings()可以指定CSS选择器 指定获取指定CSS选择器的数据
    print(li.siblings('.active'))


# 2 遍历
# 2.1 遍历整个字符串,获取单个元素
def ergodic_single_item():
    li = doc('.item-0.active')
    print(li)


# 2.2遍历整个字符串,获取所有li标签的列表
def ergodic_items():
    # 返回了 generator类型的数据
    lis = doc('li').items()
    print(type(lis))
    for item in lis:
        print(item)


# 3 获取属性信息
# 3.1 获取属性
def get_attr():
    a = doc('.item-0.active a')
    print(a)
    print(a.attr('href'))
    print(a.attr.href)


# 3.2 获取文本
def get_text():
    a = doc('.item-0.active a')
    print(a)
    print(a.text())


# 3.3 获取html
def get_html():
    a = doc('.item-0.active')
    print(a)
    print(a.html())


# 4 DOM操作
# 4.1 addClass/removeClass
def operator_class():
    li = doc('.item-0.active')
    print(li)
    li.removeClass('active')
    print(li)
    li.addClass('active')
    print(li)


# 4.2 attr/css
def operator_attr_css():
    li = doc('.item-0.active')
    print(li)
    # 给li标签中添加name属性
    li.attr('name', 'link')
    print(li)
    # 给li标签添加css
    li.css('font-size', '14px')
    print(li)


# 4.3 remove
def operator_remove():
    html = '''
    <div class="wrap">
        Hello, World
        <p>This is a paragraph</p>
    </div>
'''
    doc = pq(html)
    wrap = doc('.wrap')
    # 获取到所有的文本数据 Hello, World    This is a paragraph
    print(wrap.text())
    wrap.find('p').remove()
    # 移除p标签以后的文本
    print(wrap.text())


# 5 伪类选择器
def Pseudo_Classes():
    # 获取li标签下的第一个元素
    # li = doc('li:first-child')
    # print(li)
    # 获取li标签下最后一个元素
    # li = doc('li:last-child')
    # print(li)
    # 获取li下的第二个元素
    # li = doc('li:nth-child(2)')
    # print(li)
    # 获取li下index大于2的元素
    # li = doc('li:gt(2)')
    # print(li)
    # 获取li下index为偶数的元素
    # li = doc('li:nth-child(2n)')
    # print(li)
    # 获取li标签下文本中包含second的元素
    li = doc('li:contains(second)')
    print(li)


if __name__ == '__main__':
    Pseudo_Classes()
