import time

import requests
from bs4 import BeautifulSoup

search_keyword = input('请输入要搜索的名称：\r\n')
first_page = '1'
base_url = 'http://www.eclzz.bio'
search_url = "/s/" + search_keyword + "_rel_" + str(first_page) + ".html"

page_dict = [search_url]

result_dict = dict()

for url in page_dict:
    # 发送搜索请求
    try:
        response = requests.get(base_url + url)
    except ConnectionError as e:
        continue
    soup = BeautifulSoup(response.text, "lxml")

    # 获取后面的页数
    cur_page_e = soup.select_one("div#content > div > div.row > div.search-list > ul.pagination > li.active")
    if cur_page_e:
        next_ = cur_page_e.next_sibling
        while next_ and next_.get("class") is None:
            next_link = next_.select_one('li > a')['href']
            if next_link not in page_dict:
                page_dict.append(next_link)
            next_ = next_.next_sibling

    # 解析搜索结果页面
    results = soup.select("div#content > div > div.row > div.search-list > div.search-item")
    # 提取磁力链接
    for result in results:
        a = result.select_one("div.item-title > h3 > a")
        if a is None:
            continue
        title = a.text.strip()
        detail_link = a["href"]
        try:
            detail_res = requests.get(base_url + detail_link)
        except ConnectionError as e:
            continue
        detail_soup = BeautifulSoup(detail_res.text, 'lxml')
        down_url_a = detail_soup.select_one('div#content > div#wall > div.fileDetail > p > a#down-url')
        if down_url_a is None:
            print(detail_res.url, base_url + detail_link)
            continue
        magnet_link = down_url_a["href"]
        print(title, magnet_link)
        result_dict.setdefault(title, magnet_link)
        # print(magnet_link)
        time.sleep(1)
print('')
with open(search_keyword + '.txt', 'wb') as f:
    for item in result_dict.items():
        line = item[1] + ' ' + item[0]
        f.write(bytes(line, 'utf-8'))
        f.write(bytes('\n', 'utf-8'))
