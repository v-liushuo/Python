import json
import random

import requests
from prettytable import PrettyTable

sProjectName = input('请输入项目名称：\r\n')
sProjectAddress = input('请输入项目地址：\r\n')
sDeveloper = input('请输入开发商：\r\n')
sPresellNo = input('请输入预售证：\r\n')
ValidateCode = '245291'
first_page = '1'
base_url = 'http://zfcj.gz.gov.cn'
search_url = "/zfcj/fyxx/fdcxmxxRequest?sProjectName=" + sProjectName \
             + "&sProjectAddress=" + sProjectAddress \
             + "&sDeveloper=" + sDeveloper \
             + "&sPresellNo=" + sPresellNo \
             + "&ValidateCode=" + ValidateCode \
             + "&page=1" \
             + "&pageSize=50"
print(search_url)
header1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
                  "Safari/537.36"}
header2 = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 "
                  "MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools"}
header3 = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile "
                  "Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN"}
header4 = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 ("
                  "KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"}
header5 = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 ("
                  "KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"}
headers_list = [header1, header2, header3, header4, header5]
i = random.randint(1, 4)
response = requests.get(base_url + search_url, headers=headers_list[i])
if 200 == response.status_code:
    res_text = response.text
    json_dict = json.loads(res_text)
    data = json_dict["data"]
    sorted_data = sorted(data, key=lambda x: int(x['houseSoldNum']), reverse=True)
    # 创建表格对象
    table = PrettyTable()
    # 添加表头
    table.field_names = ["项目名称", "已售套数", "未售套数", "总套数"]
    table.align['项目名称'] = 'l'
    table.align['已售套数'] = 'r'
    table.align['未售套数'] = 'r'
    table.align['总套数'] = 'r'
    # 添加行数据
    for item in sorted_data:
        table.add_row([item['projectName'], item['houseSoldNum'], item['houseUnsaleNum'],
                       int(item['houseSoldNum']) + int(item['houseUnsaleNum'])])
    print(table)
else:
    print("请求异常", response.text)
