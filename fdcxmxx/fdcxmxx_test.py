import json
from prettytable import PrettyTable

text = {
    "data": [
        {
            "presell": "20230075",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "282",
            "projectAddress": "黄埔区南岗街沙步大路66号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "0",
            "projectName": "文芳花园自编7#",
            "projectId": "58249ce179ab4c81add0b1f638cc2725"
        },
        {
            "presell": "20220399",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "124",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路27号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "89",
            "projectName": "文采花园南区自编1#",
            "projectId": "520ce7cf7d004dc1958355e8c0b8b769"
        },
        {
            "presell": "20220398",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "117",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路15号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "219",
            "projectName": "文采花园北区自编1#",
            "projectId": "38fb84a03fa442198150eb4cb2a098e8"
        },
        {
            "presell": "20220531",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "140",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路39号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "80",
            "projectName": "文采花园南区自编5#",
            "projectId": "87a03b2cbb26489daed37a13088c256a"
        },
        {
            "presell": "20230017",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "215",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路33号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "5",
            "projectName": "文采花园南区自编4#",
            "projectId": "28ff20f3bd4442f5be81e8bdf78653ac"
        },
        {
            "presell": 'null',
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "220",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路31号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "0",
            "projectName": "文采花园南区自编3#",
            "projectId": "b15018caef1f425e83ffba4bea7ce9ff"
        },
        {
            "presell": "20220400",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "129",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路29号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "86",
            "projectName": "文采花园南区自编2#",
            "projectId": "56cd1759d63d4607a1d8cc419a7b2c24"
        },
        {
            "presell": 'null',
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "340",
            "projectAddress": "黄埔区南岗街沙步沙步大路23号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "0",
            "projectName": "文采花园北区自编5#",
            "projectId": "d3716bca11184cc88e512b41517a5e73"
        },
        {
            "presell": "20230007",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "343",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路19号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "1",
            "projectName": "文采花园北区自编3#",
            "projectId": "a474a4347c264ad9b26e7ce19c6fa126"
        },
        {
            "presell": "20230073",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "119",
            "projectAddress": "黄埔区南岗街沙步大路62号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "163",
            "projectName": "文芳花园自编6#",
            "projectId": "6a4eb89585c2408787139eb2da65a596"
        },
        {
            "presell": "20230072",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "163",
            "projectAddress": "黄埔区南岗街沙步大路58号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "26",
            "projectName": "文芳花园自编1#",
            "projectId": "56b2df226faa45e0a3d1a3e0f95f4d72"
        },
        {
            "presell": "20220401",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "122",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路21号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "214",
            "projectName": "文采花园北区自编4#",
            "projectId": "838d981cb6de4cfc9c57f8d0cf5c4571"
        },
        {
            "presell": "20220493",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "245",
            "projectAddress": "黄埔区南岗街沙步社区沙步大路17号",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "99",
            "projectName": "文采花园北区自编2#",
            "projectId": "7df51ab3abbf44b0bf81b61dde187444"
        },
        {
            "presell": "20230074",
            "developerId": "91440101MA5CQ1G38B",
            "houseUnsaleNum": "80",
            "projectAddress": "黄埔区南岗街沙步大路64",
            "developer": "广州市沙步广裕实业发展有限公司",
            "houseSoldNum": "108",
            "projectName": "文芳花园自编2#",
            "projectId": "a9dd850d4889458fb483ca51c8058d08"
        }
    ],
    "totalNum": 14,
    "totalPage": 1,
    "pageSize": 50,
    "currentPage": 1,
    "message": "ok",
    "status": 1
}

json_str = json.dumps(text)
json_dict = json.loads(json_str)
dict_local = dict()
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

list = []
projectNameList = []
houseSoldNumList = []
houseUnsaleNumList = []
houseAllNumList = []
# 添加行数据
for item in sorted_data:
    table.add_row([str.format(item['projectName']), item['houseSoldNum'], item['houseUnsaleNum'],
                   int(item['houseSoldNum']) + int(item['houseUnsaleNum'])])
print(table)

print()
