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
network    mask      distance    metric  nexthop
---------  ------  ----------  --------  -------------
10.1.1.0   24             110        20  ['10.0.12.2']
10.2.2.0   24             110        20  ['10.0.13.3']
10.3.3.3   32             110        11  ['10.0.12.2']
10.4.4.4   32             110        11  ['10.0.13.3']
                          110        11  ['10.0.14.4']
10.5.5.5   32             110        21  ['10.0.13.3']
                          110        21  ['10.0.12.2']
                          110        21  ['10.0.14.4']
10.6.6.0   24             110        20  ['10.0.13.3']
"""
