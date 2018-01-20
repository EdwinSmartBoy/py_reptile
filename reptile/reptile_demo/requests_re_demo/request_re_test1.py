# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  request_re_test1
  Description  :  用requests库分析ajax抓取今日头条街拍组图
  Author       :  Edwin
  Date         :  2018/1/15 22:11
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/15 22:11
  Description  :
-----------------------------------------
"""
import json
import re
import os
from hashlib import md5
from multiprocessing.pool import Pool

from bs4 import BeautifulSoup

__author__ = 'Edwin'

import requests
from urllib.parse import urlencode
from requests import RequestException


# 获取今日头条街拍单页页面的数据
def get_one_page(keyword, offset=0):
    request_data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }

    url = 'http://www.toutiao.com/search_content/?' + urlencode(request_data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print("页面请求失败:url= %s, offset= %s" % (url, offset))
        return None


# 获取某个url的详情界面的数据
def get_web_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('页面请求失败: url= %s' % url)
        return None


# 解析获取到的单页文本数据
def parse_web_page(response_text):
    datas = json.loads(response_text)
    if datas and 'data' in datas.keys():
        for item in datas.get('data'):
            yield item.get('article_url')


# 解析某个话题的详情界面的数据
def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select_one('title').text
    image_pattern = re.compile('gallery: JSON.parse\((.*?)\),', re.S)
    result = re.search(image_pattern, html)
    if result:
        # 使用json.loads(result.group(1)) 返回的数据类型是str的json字符串   需要再次使用json.loads()来解析成dict的json
        data = json.loads(json.loads(result.group(1)))
        # 判断json数据中是否有sub_images字段的值
        if data and 'sub_images' in data.keys():
            # 获取包含图片的数据
            sub_images = data.get('sub_images')
            images = [item.get("url") for item in sub_images]
            for image_url in images:
                # 下载图片数据
                download_image(image_url)
                # 拼装数据  输入请求的页面的数据以及对应的图片数据
            return {
                'title': title,
                'article_url': url,
                'images': images
            }


# 下载图片
def download_image(url):
    print('正在下载: url= %s' % url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 如果图片请求成功,将图片保存下来
            save_image(response.content, url)
    except RequestException:
        print('请求下载图片失败: url= %s' % url)


# 保存下载的图片
def save_image(content, url):
    # 拼接图片的url os.getcwd()获取当前工程所在的文件夹  MD5将内容图片的url进行编码 防止重复
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(url).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


# 开始请求数据
def start_download(off):
    response = get_one_page('街拍', offset=off)
    for url in parse_web_page(response):
        # 判断url是否正确
        if not url:
            page_detail = get_web_page_detail(url)
            # 判断页面数据是否正确
            if page_detail:
                result = parse_page_detail(page_detail, url)
                # 判断是否有数据 有则输出 输出格式{'title': 'xxxxxx', 'article_url': 'xxxxxxxxx', 'images': ['xxxxsxx', 'xxxxxxxxxx']}
            if result:
                print(result)


if __name__ == '__main__':
    # 创建要请求的参数 使用多进程来进行处理   提高请求效率
    groups = [x * 20 for x in range(1, 21)]
    pool = Pool()
    pool.map(start_download, groups)
