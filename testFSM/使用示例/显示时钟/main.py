import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))


"""
python main.py template.template command_output.txt
[['15:10:44', 'UTC', 'Sun', 'Nov', '13', '2016']]
Time      Timezone    WeekDay    Month      MonthDay    Year
--------  ----------  ---------  -------  ----------  ------
15:10:44  UTC         Sun        Nov              13    2016
"""