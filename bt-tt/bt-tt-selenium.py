import operator
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

base_url = 'https://www.bt-tt.com'

# chromedriver的绝对路径
service = Service("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(service=service)
# 请求网页
driver.get(base_url)
search_keyword = driver.find_element(by=By.ID, value='search-keyword')
search_keyword.send_keys('闪电侠')
sub_form = driver.find_element(by=By.NAME, value="searchtype")
sub_form.click()
print('')

result_dict = dict()

page_dict = ["/e/search/"]
for url in page_dict:

    # 获取后面的页数
    cur_page_e = driver.find_elements(by=By.XPATH, value="//div[@class='pages']")
    if cur_page_e:
        next_ = cur_page_e.next_sibling
        while next_ and next_.text.isdigit():
            next_link = next_['href']
            if next_link not in page_dict:
                page_dict.append(next_link)
            next_ = next_.next_sibling

    # 解析搜索结果页面
    results = driver.find_elements(by=By.CSS_SELECTOR,
                                   value="div.main > div.wp > div.container > div.row > div > div > ul > li")
    # 提取磁力链接
    for result in results:
        a = result.select_one("div.txt > h3 > a")
        if a is None:
            continue
        title = a.text.strip()
        if not operator.contains(title, search_keyword):
            continue
        detail_link = a["href"]
        detail_res = requests.get(base_url + detail_link)
        detail_soup = BeautifulSoup(detail_res.text, 'lxml')
        down_url_a = detail_soup.select('div#pad_01 > div.wp > div > div > div > div.bot > tr > td > a')
        if down_url_a is None:
            print(detail_res.url, base_url + detail_link)
            continue
        magnet_links = []
        for down_url_a1 in down_url_a:
            magnet_link = down_url_a1["href"]
            print(title, magnet_link)
            magnet_links.append(magnet_link)
        result_dict.setdefault(title, magnet_links)
        # print(magnet_link)
        time.sleep(1)
print('')
with open(search_keyword + '.txt', 'wb') as f:
    for item in result_dict.items():
        for magnet in item[1]:
            line = item[0] + ' ' + magnet
            f.write(bytes(line, 'utf-8'))
            f.write(bytes('\n', 'utf-8'))
