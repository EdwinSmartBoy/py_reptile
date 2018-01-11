# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  re_test
  Description  :  尽量使用泛匹配/使用括号匹配目标/尽量使用非贪婪模式/有换行符就用re.S
  Author       :  Edwin
  Date         :  2018/1/11 21:02
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/11 21:02
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import re


# 常规匹配
def regex():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    pattern = re.compile(r'^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$')
    result = pattern.match(content)
    print(result)
    print(result.group())
    print(result.span())
    print(result.groups())


# 泛匹配
def regex1():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    pattern = re.compile(r'^Hello.*Demo$')
    result = pattern.match(content)
    print(result)
    print(result.group())
    print(result.span())
    print(result.groups())


# 目标匹配
def regex2():
    content = 'Hello 1234567 World_This is a Regex Demo'
    pattern = re.compile(r'^Hello\s(\d+)\s.*Demo$')
    result = pattern.match(content)
    print(result)
    print(result.group())
    print(result.span())
    print(result.groups(1))


# 贪婪匹配
def regex3():
    content = 'Hello 1234567 World_This is a Regex Demo'
    pattern = re.compile(r'^He.*(\d+).*Demo$')
    result = pattern.match(content)
    print(result)
    print(result.group(1))
    print(result.span())


# 非贪婪匹配
def regex4():
    content = 'Hello 1234567 World_This is a Regex Demo'
    pattern = re.compile(r'^He.*?(\d+).*Demo$')
    result = pattern.match(content)
    print(result)
    print(result.group(1))
    print(result.span())


# 匹配模式
def regex5():
    content = '''Hello 1234567 World_This
     is a Regex Demo'''
    pattern = re.compile('^He.*?(\d+).*Demo$', flags=re.S)
    result = pattern.match(content)
    print(result.group(1))

    result1 = re.match('^He.*?(\d+).*?Demo$', content, flags=re.S)
    print(result1.group(1))


# 转义
def regex6():
    content = 'price is $5.00'
    result = re.match(r'price is \$5.00', content)
    print(result)


if __name__ == '__main__':
    regex6()
