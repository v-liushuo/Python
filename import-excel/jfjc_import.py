import os

import pandas as pd

folder_path = r"D:\work\wisdom_lighthouse\进出审批流程\角色收集结果"

files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)
    if not os.path.isfile(file_path):
        continue
    print(file_path)

    docIndex = file.index('.')
    lineIndex = file.index('-')
    areaName = file[lineIndex + 1:docIndex]
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    sheet_data = pd.read_excel(excel_file, sheet_name='ABC级及自有IDC机房', header=[0, 1])
    for column in sheet_data.columns:
        if not column[1].startswith('Unnamed'):
            print(column)
    print()
