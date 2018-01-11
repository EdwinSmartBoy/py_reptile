# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  re_demo
  Description  :  re模块的高级用法
  Author       :  Edwin
  Date         :  2018/1/11 23:07
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/11 23:07
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import re


# re.search 扫描整个字符串并返回第一个成功的匹配
def search():
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)


# re.findall 搜索字符串,并以列表形式返回全部能匹配的子串
def findall():
    pass


# re.sub 替换字符串中每一个匹配的子串后返回替换后的字符串
def subs():
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
    result = re.sub('\d+', '', content)
    print(result)


# 删除元字符串中的数据
def subs1():
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
    result = re.sub('\d+', 'Replacement', content)
    print(result)


# 对原字符串中的数据进行增加的操作
def subs2():
    content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
    # 1.需要指定替换的规则加上小括号 2.匹配的数据需要加上 \1
    result = re.sub('(\d+)', r'\1 9900', content)
    print(result)


if __name__ == '__main__':
    subs2()
