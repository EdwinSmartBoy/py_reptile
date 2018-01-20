# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  request_re_text
  Description  :  用requeests库抓取猫眼电影的top排行榜前一百名数据
  Author       :  Edwin
  Date         :  2018/1/15 19:59
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/15 19:59
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import json
import re
import requests
from requests.exceptions import RequestException


# 获取网页单页的内容
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


# 解析网页内容
def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + r'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)'
                           r'</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4][5:],
            'score': item[5] + item[6],
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


if __name__ == '__main__':
    for position in range(10):
        main(position * 10)
