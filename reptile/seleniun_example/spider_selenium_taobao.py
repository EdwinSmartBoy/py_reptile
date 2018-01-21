# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  spider_selenium
  Description  :
  Author       :  Edwin
  Date         :  2018/1/20 12:18
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/20 12:18
  Description  :  
-----------------------------------------
"""
import json
import re

__author__ = 'Edwin'

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


# 调动浏览器  请求淘宝数据
def search():
    try:
        browser.get('https://www.taobao.com')
        input_keyword = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input_keyword.send_keys('美食')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_page_products()
        return parse_page_count(total)
    except TimeoutException:
        print('TIMEOUT')
        return 0


# 解析页面数  判断是否返回数据
def parse_page_count(content):
    if content:
        count = re.compile(r'(\d+)').search(content.text).group(1)
        if count:
            return int(count)
        else:
            return 0
    else:
        return 0


# 获取下一页的数据  不断请求page_number的数据
def parse_next_page(page_number):
    print('请求第%s页的数据' % page_number)
    try:
        input_number = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        submit_number = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        # 清空页码输入框中的数据
        input_number.clear()
        # 输入要请求的页码
        input_number.send_keys(page_number)
        # 发送请求
        submit_number.click()
        # 判断当前要请求的页面是否成功加载
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        # 保存数据
        get_page_products()
    except TimeoutException:
        print('请求第%s页超时,重新请求中...' % page_number)
        parse_next_page(page_number)


# 获取每一页的原始数据  并解析 存储到文件中
def get_page_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    source = browser.page_source
    if source:
        doc = pq(source)
        items = doc('#mainsrp-itemlist .items .item').items()
        for item in items:
            product = {
                'image': item.find('.pic .img').attr('data-src'),
                'price': item.find('.price').text(),
                'deal': item.find('.deal-cnt').text(),
                'title': item.find('.title').text(),
                'shop': item.find('.shop').text(),
                'location': item.find('.location').text()
            }
            save_to_file(product)


# 将请求的数据存储到文件中
def save_to_file(product):
    with open('taobao_info.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(product, ensure_ascii=False))
        f.close()


if __name__ == '__main__':
    page_count = search()
    if page_count:
        for number in range(2, page_count + 1):
            parse_next_page(number)
    else:
        print('请求失败')
