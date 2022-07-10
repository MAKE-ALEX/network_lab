from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'Test'
wb.save('test_openpyxl.xlsx')