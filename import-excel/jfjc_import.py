import os

import pandas as pd

folder_path = r"D:\work\wisdom_lighthouse\进出审批流程\角色收集结果"

files = os.listdir(folder_path)


def read_sheet(excel_file, sheet_name):
    sheet_data = pd.read_excel(
        excel_file, sheet_name=sheet_name, header=[0, 1])
    data_values = sheet_data.values
    role_name_account_index_dict = dict()
    for index in range(sheet_data.columns.size):
        column = sheet_data.columns[index]
        if column[1] == 'OA账号':
            role_name_account_index_dict.setdefault(column[0], index)

    role_name_account_dict = dict()
    for dv in data_values:
        for key, value in role_name_account_index_dict.items():
            cv = dv[value]
            if pd.isna(cv):
                continue
            put_into_dict(role_name_account_dict, key, cv)
    return role_name_account_dict


def put_into_dict(role_name_account_dict, key, cv):
    if role_name_account_dict.__contains__(key):
        users = role_name_account_dict.get(key)
        users.add(cv)
        role_name_account_dict.setdefault(key, users)
    else:
        users = set()
        users.add(cv)
        role_name_account_dict.setdefault(key, users)


def read_fourth_sheet(excel_file, sheet_name):
    sheet_data = pd.read_excel(
        excel_file, sheet_name=sheet_name, header=1)
    role_name_account_dict = dict()

    for dv in sheet_data.values:
        cv = dv[1]
        key = dv[0]
        if pd.isna(cv):
            continue
        put_into_dict(role_name_account_dict, key, cv)
    return role_name_account_dict


def get_role_name_code_dict():
    role_name_code_dict_result = dict()
    role_str = '''jfjc_admin,（机房进出审批）机房管理员 
                jfjc_contractor,（机房进出审批）机房承包人 
                jfjc_localSecurity,（机房进出审批）属地安保人员 
                jfjc_inspector,（机房进出审批）综合维护团队总监 
                jfjc_district,（机房进出审批）综维片区长 
                jfjc_cantonalLeader,（机房进出审批）分管领导 
                jfjc_stationManager,（机房进出审批）楼长 
                pre_jfjc_maintenanceAuditor,（预审批流程）网运部审核人 
                pre_jfjc_maintenanceAuditor,（预审批流程）云网部审核人
                pre_jfjc_securityAuditor,（预审批流程）安保部审核人'''
    area_str_arr = role_str.split('\n')

    for area_info in area_str_arr:
        area_infos = area_info.strip().split(',')
        role_name_code_dict_result.setdefault(area_infos[1].replace(
            '（预审批流程）', '').replace('（机房进出审批）', ''), area_infos[0])

    return role_name_code_dict_result


def get_area_name_id_dict():
    area_str = '''441000000000000102224423,756,珠海市
                441020000000001060167911,200,广州市
                441066000000001015206033,660,汕尾市
                441066200000001011643833,662,阳江市
                441066300000001020950039,663,揭阳市
                441066800000001014843643,668,茂名市
                441075000000001025282636,750,江门市
                441075100000001019538846,751,韶关市
                441075200000001023640797,752,惠州市
                441075300000001032984133,753,梅州市
                441075400000001029249567,754,汕头市
                441075500000001057793095,755,深圳市
                441075700000001036961414,757,佛山市
                441075800000001016811672,758,肇庆市
                441075900000001014161688,759,湛江市
                441076000000001028795493,760,中山市
                441076200000001020634059,762,河源市
                441076300000001019528468,763,清远市
                441076600000001013839773,766,云浮市
                441076800000001029619094,768,潮州市
                441076900000001057355065,769,东莞市'''
    area_str_arr = area_str.split('\n')
    area_name_id_dict_result = dict()
    for area_info in area_str_arr:
        area_infos = area_info.strip().split(',')
        area_name_id_dict_result.setdefault(area_infos[2], area_infos[0])
    return area_name_id_dict_result


def add_to_all_data(abc_room_dict, all_dict):
    for role_name, users in abc_room_dict.items():
        if all_dict.__contains__(role_name):
            temp = all_dict.get(role_name)
            temp_set = set(temp)
        else:
            temp_set = set()
        temp_set.update(set(users))
        all_dict.setdefault(role_name, temp_set)


def get_sql_list(role_name_code_dict, all_data_dict):
    template = '''insert into sys_role_user (user_id, role_id, city_id) select u.id, r.id, '##cityId##' from sys_user u, sys_role r where u.username = '##username##' and r.code = '##roleCode##' and not exists(select 1 from sys_role_user ru where ru.user_id = u.id and ru.role_id = r.id and city_id = '##cityId##');'''
    sql_list = []
    for area_id, role_name_users_dic in all_data_dict.items():
        for role_name, users in role_name_users_dic.items():
            for user in users:
                sql = template.replace('##cityId##', area_id).replace(
                    '##username##', user).replace('##roleCode##', role_name_code_dict.get(role_name))
                sql_list.append(sql)
    return sql_list


if __name__ == '__main__':
    all_data_dict = dict()
    area_name_id_dict = get_area_name_id_dict()
    role_name_code_dict = get_role_name_code_dict()
    for file in files:
        file_path = os.path.join(folder_path, file)
        if not os.path.isfile(file_path):
            continue
        print(file_path)

        docIndex = file.index('.')
        lineIndex = file.index('-')
        areaName = file[lineIndex + 1:docIndex]
        if not area_name_id_dict.__contains__(areaName):
            print('没有找到对应的地市信息，areaName:' + areaName + ';fileName:' + file)
            continue
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        abc_room_dict = read_sheet(excel_file, 'ABC级及自有IDC机房')
        d_z_room_dict = read_sheet(excel_file, 'D级机房综合接入局站')
        d_uz_room_dict = read_sheet(excel_file, 'D级机房非综合接入局站')
        fourth_room_dict = read_fourth_sheet(excel_file, '云网安保审核人')
        all_dict = dict()
        add_to_all_data(abc_room_dict, all_dict)
        add_to_all_data(d_z_room_dict, all_dict)
        add_to_all_data(d_uz_room_dict, all_dict)
        add_to_all_data(fourth_room_dict, all_dict)
        all_data_dict.setdefault(area_name_id_dict.get(areaName), all_dict)

    sql_list = get_sql_list(role_name_code_dict, all_data_dict)

    with open('result.sql', 'w') as f:
        for sql in sql_list:
            f.write(sql + '\n')
