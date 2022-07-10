from pprint import pprint

from napalm import get_network_driver
import json
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Side
from pprint import pprint

driver = get_network_driver('huawei_vrp')
host = driver('192.168.59.10', 'python', '123456')
host.open()

facts = host.get_facts()
facts_json = json.dumps(facts, indent=2)
# print(facts_json)

get_interfaces = host.get_interfaces()
get_interfaces_json = json.dumps(get_interfaces, indent=2)
pprint(get_interfaces_json)

interfaces = []
descriptions = []
status = []
for key, value in get_interfaces.items():
    interfaces.append(key)
    descriptions.append(value['description'])
    status.append(value['is_up'])

for n, i in enumerate(status):
    if i == False:
        status[n] = 'Inactive'
    else:
        status[n] = 'Active'

    pprint(interfaces)
pprint(descriptions)
pprint(status)

row_numbers = [n + 2 for n in range(len(interfaces))]

wb = Workbook()
ws = wb.active
ws.title = facts['hostname']

ws['A1'] = 'Interfaces'
ws['B1'] = 'Description'
ws['C1'] = 'Status'

for interface, row in zip(interfaces, row_numbers):
    ws.cell(row=row, column=1, value=interface)
for description, row in zip(descriptions, row_numbers):
    ws.cell(row=row, column=2, value=description)
for stat, row in zip(status, row_numbers):
    ws.cell(row=row, column=3, value=stat)

yellowFill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'),
                     bottom=Side(style='thin'))

ws['A1'].fill = yellowFill
ws['B1'].fill = yellowFill
ws['C1'].fill = yellowFill

dims = {}
for row in ws.rows:
    for cell in row:
        cell.border = thin_border
        if cell.value:
            dims[cell.column_letter] = max((dims.get(cell.column, 0), len(str(cell.value))))

for col, value in dims.items():
    ws.column_dimensions[col].width = value + 1

wb.save('switch.xlsx')
