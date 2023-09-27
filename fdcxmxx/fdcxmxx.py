import json
import os
import sys

import requests
from prettytable import PrettyTable

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import lib.userAgent as userAgent

param_dict = dict()
sProjectName = input('请输入项目名称：\r\n')
if len(sProjectName.strip()) != 0:
    param_dict.setdefault('sProjectName', sProjectName)

if len(param_dict) == 0:
    sProjectAddress = input('请输入项目地址 ：\r\n')
    if len(sProjectAddress.strip()) != 0:
        param_dict.setdefault('sProjectAddress', sProjectAddress)

if len(param_dict) == 0:
    sDeveloper = input('请输入开发商：\r\n')
    if len(sDeveloper.strip()) != 0:
        param_dict.setdefault('sDeveloper', sDeveloper)
    else:
        param_dict.setdefault('sDeveloper', '广州市沙步广裕实业发展有限公司')
if len(param_dict) == 0:
    sPresellNo = input('请输入预售证：\r\n')
    if len(sPresellNo.strip()) != 0:
        param_dict.setdefault('sPresellNo', sPresellNo)

if len(param_dict) == 0:
    print("输入的全部查询条件为空")
    sys.exit(0)
ValidateCode = '245291'
first_page = '1'
base_url = 'http://zfcj.gz.gov.cn'
search_url = "/zfcj/fyxx/fdcxmxxRequest?sProjectName=" + param_dict.get('sProjectName', '') \
             + "&sProjectAddress=" + param_dict.get('sProjectAddress', '') \
             + "&sDeveloper=" + param_dict.get('sDeveloper', '') \
             + "&sPresellNo=" + param_dict.get('sPresellNo', '') \
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
    # http://zfcj.gz.gov.cn/zfcj/fyxx/projectdetail?sProjectId=520ce7cf7d004dc1958355e8c0b8b769&sDeveloperId=91440101MA5CQ1G38B
else:
    print("请求异常", response.text)
