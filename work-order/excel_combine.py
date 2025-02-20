import os
import platform
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd


def reveal_file_in_explorer(file_path):
    """
    打开文件所在文件夹并高亮/定位指定文件
    支持 Windows、macOS 和 Linux
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    file_path = os.path.abspath(file_path)

    system = platform.system()

    try:
        if system == "Windows":
            # Windows: 使用 explorer 的 /select 参数
            subprocess.run(f'explorer /select,"{file_path}"', shell=True)

        elif system == "Darwin":
            # macOS: 使用 open 的 -R 参数
            subprocess.run(["open", "-R", file_path])

        elif system == "Linux":
            # Linux: 尝试使用文件管理器（不同发行版可能不同）
            if os.path.isfile(file_path):
                parent_dir = os.path.dirname(file_path)
            else:
                parent_dir = file_path

            # 尝试常见 Linux 文件管理器
            try:
                subprocess.run(["xdg-open", parent_dir])
            except:
                try:
                    subprocess.run(["nautilus", "--select", file_path])
                except:
                    try:
                        subprocess.run(["dolphin", "--select", file_path])
                    except:
                        print("请手动打开文件管理器定位文件")
        else:
            print("不支持的操作系统")

    except Exception as e:
        print(f"操作失败: {str(e)}")


def combine_excel():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(title="选择文件", filetypes=(("excel文件", "*.xlsx"), ("所有文件", "*.*")))

    # 读取 Excel 文件
    all_sheets = pd.read_excel(file_path, sheet_name=None, dtype=str)

    # 创建一个空的 DataFrame 用于存储合并后的数据
    combined_df = pd.DataFrame()

    # 遍历所有 sheet
    for sheet_name, df in all_sheets.items():
        # 添加一列表示来源 sheet
        df['来源Sheet'] = sheet_name
        # 将当前 sheet 的数据添加到合并后的 DataFrame 中
        combined_df = pd.concat([df, combined_df], ignore_index=True)

    file_name = os.path.split(file_path)[-1]
    base, ext = os.path.splitext(file_name)
    suffix = 'result'
    new_file_name = f'{base}-{suffix}{ext}'
    work_path = os.path.join(os.path.split(file_path)[-2], new_file_name)

    # 将合并后的数据保存到新的 Excel 文件
    combined_df.to_excel(work_path, index=False)
    return work_path


if __name__ == "__main__":
    output_file_path = combine_excel()

    messagebox.showinfo("合并完成", f"合并完成，结果已保存到 {output_file_path}")
    reveal_file_in_explorer(f'{output_file_path}')
