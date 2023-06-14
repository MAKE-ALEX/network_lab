from openpyxl import Workbook
# 实验五代码部分
from openpyxl.styles import PatternFill, Border, Side

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
a3 = ws1['A3']
print(a3.value)
column_A = ws1['A']
for i in column_A:
    print(i.value)
row_3 = ws1[3]
for i in row_3:
    print(i.value)
for row in ws1.iter_rows(min_row=1, max_col=2, max_row=3):
    for cell in row:
        print(cell.value)
for row in ws1.values:
    for value in row:
        print(value)
b3 = ws1['B3']
b3.value = 'PC3'
print(b3.value)

b3 = ws1['B3']
b3.value = 'PC31234123412342134123421341234'
print(b3.value)
wb.save('test_openpyxl.xlsx')

# 实验五代码部分
yellowFill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'),
                     bottom=Side(style='thin'))

ws1['A1'].fill = yellowFill
ws1['B1'].fill = yellowFill

# 首先创建一个名为dims的空字典
dims = {}
# ws1.rows返回值的类型为生成器generator，其中包含每一排和每一列有交集的所有单元格
# （每一排中至少有一个单元格为非空），比如(A1,B1), (A2,B2), (A3,B3)
for row in ws1.rows:
    # 遍历每一排元组里的每一个元素（即单元格A1,B1,A2,B2,A3,B3）
    for cell in row:
        # 为每一个单元添加边框
        cell.border = thin_border
        # 如果单元格内容为非空，则用max()比较每一列下最长的字符，比如从A1和A2,A3相比较，B1和B2,B3相比较
        if cell.value:
            # cell.column_letter返回的值是单元格所在的列的名称，其数据类型为字符串，比如A1,A2,A3返回'A'，B1,B2,B3则返回'B'。
            # 第一次故意用dims.get(cell.column, 0)返回一个0，因为此时dims字典下还没有cell.column这个键名，
            # 字典的的get()函数在键名缺失的情况下会返回第二个我们给定的参数，即这里的0。
            dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))

# 遍历字典里的键值对，以每一排宽度最长的单元格作为自动调整单元格长度的标准，
# 长度+1以确保列的宽度超过最长单元格的宽度
for col, value in dims.items():
    ws1.column_dimensions[col].width = value + 1

wb.save('test_openpyxl.xlsx')
