# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  py_reptile
-----------------------------------------
  File Name    :  selenium_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/14 11:01
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/14 11:01
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


# selenium的基本使用
def driver():
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element_by_id('kw')
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()


# selenium 的使用步骤解析


# 1. 声明浏览器对象
def web():
    chrome = webdriver.Chrome()
    firefox = webdriver.Firefox()
    edge = webdriver.Edge()
    phantomJs = webdriver.PhantomJS()
    safari = webdriver.Safari()


# 2. 访问页面
def web_access():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    print(browser.page_source)
    browser.close()


# 3. 查找元素

# 3.1 查找单个元素

# 查找单个元素的其他方式如下:
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

def web_access_single():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    print(browser.find_element_by_id('q'))
    print(browser.find_element_by_css_selector('#q'))
    print(browser.find_element_by_xpath('//*[@id="q"]'))
    browser.close()


# 查找单个元素
def web_access_single1():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element(By.ID, 'q')
    print(input_first)
    browser.close()


# 3.2 查找多个元素


# 查找多个元素的其他方式如下:
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

def web_access_more():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    lis = browser.find_elements_by_css_selector('.service-bd li')
    for item in lis:
        print(item)
    browser.close()


# 3.2 查找多个元素
def web_access_more1():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    lis = browser.find_elements(by=By.CSS_SELECTOR, value='.service-db li')
    for item in lis:
        print(item)
    browser.close()


# 4. 元素交互操作
def web_element():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input = browser.find_element_by_id('q')
    input.send_keys('iPhone')
    time.sleep(1)
    input.clear()
    input.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()


# 5. 交互动作 将动作附加到动作链中串行执行
def web_action():
    browser = webdriver.Chrome()
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to_frame('iframeResult')
    source = browser.find_element_by_class_name('#draggable')
    target = browser.find_element_by_class_name('#droppable')
    action = ActionChains(browser)
    action.drag_and_drop(source, target)
    action.perform()


# 6. 执行JavaScript
def web_javascript():
    browser = webdriver.Chrome()
    browser.get('http://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')


# 7.获取元素信息

# 7.1 获取属性
def web_get_attr():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo.text)
    print(logo.get_attribute('class'))


# 7.2 获取文本值
def web_get_text():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.text)


# 7.3 获取ID/位置/标签名/大小
def web_get_other():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)


# 8 Frame
def web_frame():
    browser = webdriver.Chrome()
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to_frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    print(source)
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)


# 9 等待
# 9.1 隐式等待
#     当使用了隐式等待执行测试的时候,如果webDriver没有在DOM中找到元素,将继续等待,超出设定时间后则抛出找不到元素的异常,
#     换句话说,当查找元素或元素并没有立即出现的时候,隐式等待将等待一段时间后再查找DOM,默认的时间是0

def web_implicitly_wait():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('http://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)


# 9.2 显示等待 关键点1.设置显示等待时间 2.设置显示等待着的条件

# 设置等待着的条件的api如下所示:
# title_is 标题是某内容
# title_contains 标题包含某内容
# presence_of_element_located            元素加载出来,传入定位元组, 如 (By.ID, 'q')
# visibility_of_element_located          元素可见,传入定位元组
# visibility_of                          可见,传入元素对象
# presence_of_all_elements_located       所有元素加载出来
# text_to_be_present_in_element          某个元素文本包含某文字
# text_to_be_present_in_element_value    某个元素值包含某文字
# frame_to_be_available_and_switch_to_it frame加载并切换
# invisibility_of_element_located        元素不可见
# element_to_be_clickable                元素可点击
# staleness_of                           判断一个元素是否仍在DOM,可判断页面是否已经刷新
# element_to_be_selected                 元素可选择,传元素对象
# element_located_to_be_selected         元素可选择,传入定位元组
# element_selection_state_to_be          传入元素对象以及状态,相等返回True,否则返回False
# element_located_selection_state_to_be  传入定位元组以及状态,相等返回True,否则返回False
# alert_is_present                       是否出现Alert

def web_until_wait():
    browser = webdriver.Chrome()
    browser.get('https://www.taoboa.com')
    # 1.设置显示等待的时间
    wait = WebDriverWait(10)
    # 2.设置显示等待的条件
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    # 显示等待条件
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)


# 10 前进后退
def web_forward_back():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.python.org/')
    browser.back()
    time.sleep(5)
    browser.forward()
    time.sleep(5)
    browser.close()


# 11 Cookies
def web_cookies():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'edwin'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


# 12 选项卡管理
def web_window():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(5)
    browser.switch_to_window(browser.window_handles[0])
    browser.get('https://python.org')


# 13 异常处理
def web_exception():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.find_element_by_id('hello')


# 13.2 异常处理
def web_exception1():
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('hello')
    except NoSuchElementException:
        print('No Element')
    finally:
        browser.close()


if __name__ == '__main__':
    web_exception1()
