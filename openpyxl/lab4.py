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

# 实验四代码部分
# 查看指定单元格里的内容，需要用到value这个属性, 这里我们查看Switch工作表里A3的内容
a3 = ws1['A3']
print(a3.value)

# 要查看Switch工作表里整个A列下已有的内容，可以这么写：
column_A = ws1['A']
for i in column_A:
    print(i.value)

# 要查看Switch工作表里整个第3排已有的内容，可以这么写
row_3 = ws1[3]
for i in row_3:
    print(i.value)

# 要同时查看Switch工作表里单元格A1-A3，B1-B3里的内容，可以用iter_rows()函数，其显示的顺序为A1,B1,A2,B2,A3,B3
for row in ws1.iter_rows(min_row=1, max_col=2, max_row=3):
    for cell in row:
        print(cell.value)

# 要一次性查看excel文件里所有单元格的内容，可以用到ws.values:
for row in ws1.values:
    for value in row:
        print(value)

# 要改变已有的单元格里的内容并查看可以这么写：
b3 = ws1['B3']
b3.value = 'PC3'
print(b3.value)
wb.save('test_openpyxl.xlsx')

b3 = ws1['B3']
b3.value = 'PC31234123412342134123421341234'
print (b3.value)
wb.save('test_openpyxl.xlsx')
