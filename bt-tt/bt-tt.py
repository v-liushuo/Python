import operator
import time

import requests
from bs4 import BeautifulSoup

search_keyword = input('请输入要搜索的名称：\r\n')
first_page = '1'
base_url = 'https://www.bt-tt.com'

page_dict = ["/e/search/"]
headers = {
    'content-type': 'application/x-www-form-urlencoded'
}

data = {
    'show': 'title,newstext',
    'keyboard': search_keyword,
    'searchtype': '影视搜索'
}

result_dict = dict()

for url in page_dict:
    # 发送搜索请求
    response = requests.post(base_url + url, headers=headers, data=data)
    soup = BeautifulSoup(response.text, "lxml")

    # 获取后面的页数
    cur_page_e = soup.select_one("div.pages > ul > span > b")
    if cur_page_e:
        next_ = cur_page_e.next_sibling
        while next_ and next_.text.isdigit():
            next_link = next_['href']
            if next_link not in page_dict:
                page_dict.append(next_link)
            next_ = next_.next_sibling

    # 解析搜索结果页面
    results = soup.select("div.main > div.wp > div.container > div.row > div > div > ul > li")
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
