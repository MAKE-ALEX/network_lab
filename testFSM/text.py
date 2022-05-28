# textfsm_quick.py 增加 CSV 格式打印

import textfsm

with open('template_file.txt') as template, open('raw_text_data_file.txt') as raw_text_data_file:
    raw_text_data = raw_text_data_file.read()
    re_table = textfsm.TextFSM(template)
    data = re_table.ParseText(raw_text_data)

print(', '.join(re_table.header))  # 打印表头，表头是 re_table 的一个属性。
for row in data:
    print(', '.join(row))  # join是一个字符串处理方法，需要跟列表配合使用。

    # print(data))  # 早前调测，注释掉
    # print(type(data))
    # print(type(template))
    # print(template)
    # print(type(raw_text_data))
    # print(raw_text_data)