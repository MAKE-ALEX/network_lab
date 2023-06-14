from openpyxl import Workbook

# 实验一代码部分
wb = Workbook()
ws = wb.active
ws.title = 'Test'

# 实验二代码部分
ws1 = wb.create_sheet("Switch", 0)
ws2 = wb.create_sheet("Router")

# 实验三代码部分
ws1['A1'] = 'Interfaces'
ws1['B1'] = 'Description'
ws1.cell(row=2, column=1, value='Gi1/0/1')
ws1.cell(row=3, column=1, value='Gi1/0/2')
ws1.cell(row=2, column=2, value='PC1')
ws1.cell(row=3, column=2, value='PC2')
wb.save('test_openpyxl.xlsx')

# column_A = ws1['A']
# for i in column_A:
#     print(i.value)
