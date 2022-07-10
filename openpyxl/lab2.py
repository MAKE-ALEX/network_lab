from openpyxl import Workbook

# 实验一代码部分
# 新建一个工作蒲
wb = Workbook()
# 获取当前的活动的工作表
ws = wb.active
# 修改工作表的名称
ws.title = 'Test'

# 实验二代码部分
# 创建一个工作表，并放在第一位
ws1 = wb.create_sheet("Switch", 0)
# 创建一个工作表
ws2 = wb.create_sheet("Router")
wb.save('test_openpyxl.xlsx')
print (wb.sheetnames)
