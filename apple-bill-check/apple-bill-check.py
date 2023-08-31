import time
import json


import requests
from bs4 import BeautifulSoup

search_keyword = input('请输入要搜索的名称：\r\n')
first_page = '1'
base_url = 'https://www.apple.com.cn'
global search_url
if len(search_keyword) == 0:
    search_url = '/xc/cn/vieworder/W1223720323/shuo145678@yeah.net'
else:
    search_url = '/xc/cn/vieworder/'+search_keyword+'/shuo145678@yeah.net'

page_dict = [search_url]

result_dict = dict()

for url in page_dict:
    # 发送搜索请求
    try:
        response = requests.get(base_url + url, timeout=10)
    except ConnectionError as e:
        continue
    soup = BeautifulSoup(response.text, "lxml")
    init_json = soup.select_one('#init_data')
    json_dict = json.loads(init_json.text)
    orderItems = json_dict['orderDetail']['orderItems']
    orderList = orderItems['c']
    for orderId in orderList:
        orderItem = orderItems[orderId]
        orderItemDetailsD = orderItem['orderItemDetails']['d']
        print('商品名称：' + orderItemDetailsD['productName'])
        print('预计送达日期：' + orderItemDetailsD['deliveryDate'])
        orderItemStatusTracker = orderItem['orderItemStatusTracker']
        orderItemStatusTrackerD = orderItemStatusTracker['d']
        if 'SHIPPED' == orderItemStatusTrackerD['currentStatus']:
            print(orderItemStatusTrackerD['statusDescription'])
            trackingUrls = orderItemStatusTrackerD['trackingUrls']
            for trackingUrl in trackingUrls:
                print(trackingUrl)
        else:
            print('待发货')
        print('\r\n')
