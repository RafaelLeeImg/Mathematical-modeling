#!/bin/python3

from PyPDF2 import PdfReader

import sys
import os

if len(sys.argv) == 1:
    print("usage: %s [OUTPUT_PDF_INFO_FILENAME]" % sys.argv[0])
    info_file = '数学建模算法与程序.pdf.info'
else:
    info_file = sys.argv[1]


info_file_head = '''InfoBegin
InfoKey: Creator
InfoValue: Adobe Acrobat Pro 9.0.0
InfoBegin
InfoKey: ModDate
InfoValue: D:20110918213006+08'00'
InfoBegin
InfoKey: CreationDate
InfoValue: D:20100719160939+08'00'
InfoBegin
InfoKey: Producer
InfoValue: Acrobat Distiller 7.0.5 (Windows)
InfoBegin
InfoKey: Author
InfoValue: 司守奎
InfoBegin
InfoKey: Title
InfoValue: 数学建模算法与程序
PdfID0: 255662d9784fab45b63be741d727eaa7
PdfID1: 1515869ccc55654fb184a46d1919a4c6
'''


pdf_files = ['封面.pdf',
             '前言.pdf',
             '目录.pdf',
             '第一章 线性规划.pdf',
             '第二章 整数规划.pdf',
             '第三章 非线性规划.pdf',
             '第四章 动态规划.pdf',
             '第五章 图与网络.pdf',
             '第六章 排队论.pdf',
             '第七章 对策论.pdf',
             '第八章 层次分析法.pdf',
             '第九章 插值与拟合.pdf',
             '第十章 数据的统计描述和分析.pdf',
             '第十一章 方差分析.pdf',
             '第十二章 回归分析.pdf',
             '第十三章 微分方程建模.pdf',
             '第十四章 稳定状态模型.pdf',
             '第十五章 常微分方程的解法.pdf',
             '第十六章 差分方程模型.pdf',
             '第十七章 马氏链模型.pdf',
             '第十八章 变分法模型.pdf',
             '第十九章 神经网络模型.pdf',
             '第二十章 偏微分方程的数值解.pdf',
             '第二十一章 目标规划.pdf',
             '第二十二章 模糊数学模型.pdf',
             '第二十三章 现代优化算法.pdf',
             '第二十四章 时间序列模型.pdf',
             '第二十五章 灰色系统理论及其应用.pdf',
             '第二十六章 多元分析.pdf',
             '第二十七章 偏最小二乘回归分析.pdf',
             '第二十八章 存贮论.pdf',
             '第二十九章 经济与金融中的优化问题.pdf',
             '第三十章 生产与服务运作管理中的优化问题.pdf',
             '第三十一章 支持向量机.pdf',
             '第三十二章 作业计划.pdf',
             '附录一 Matlab入门.pdf',
             '附录二 Matlab在线性代数中的应用.pdf',
             '附录三 运筹学的LINGO软件.pdf',
             '附录四 Excel在统计分析与数量方法中的应用.pdf',
             '附录五 SPSS在统计分析中的应用.pdf',
             '参考文献.pdf']

print(info_file_head, end="")

last_page_number = 1

bookmark_str_list = []
for pdf_name in pdf_files:
    with open(pdf_name, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        page_count = len(pdf_reader.pages)
        bookmark_str = f'''BookmarkBegin\nBookmarkTitle: {pdf_name[:-4]}\nBookmarkLevel: 1\nBookmarkPageNumber: {last_page_number}\n'''
        print(bookmark_str, end="")
        bookmark_str_list.append(bookmark_str)

        for i in range(page_count):
            colspacing = 2
            command = f'pdftotext "{pdf_name}" -f {i+1} -l {i+1} -colspacing {colspacing} - |grep §'
            # print (command)
            pipe_content = os.popen(command)
            texts = pipe_content.read().split('\n')
            for text in texts:
                if text != '':
                    bookmark_str = f'''BookmarkBegin\nBookmarkTitle: {text}\nBookmarkLevel: 2\nBookmarkPageNumber: {last_page_number+i}\n'''
                    print(bookmark_str, end="")
                    bookmark_str_list.append(bookmark_str)
                    print(text)

        # (\d+)([^\d]+)$
        # $1\n$2

        # §(\d)
        # § $1

        last_page_number += page_count

with open(info_file, "w") as fw:
    fw.write(info_file_head+"".join(bookmark_str_list))
