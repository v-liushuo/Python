import json

import requests
from prettytable import PrettyTable

import lib.userAgent as userAgent

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
response = requests.get(base_url + search_url, headers=userAgent.get())
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
