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
[['FastEthernet0/0', '15.0.15.1', 'up', 'up'], ['FastEthernet0/1', '10.0.12.1', 'up', 'up'], ['FastEthernet0/2', '10.0.13.1', 'up', 'up'], ['FastEthernet0/3', 'unassigned', 'up', 'up'], ['Loopback0', '10.1.1.1', 'up', 'up'], ['Loopback100', '100.0.0.1', 'up', 'up']]
INTF             ADDR        STATUS    PROTO
---------------  ----------  --------  -------
FastEthernet0/0  15.0.15.1   up        up
FastEthernet0/1  10.0.12.1   up        up
FastEthernet0/2  10.0.13.1   up        up
FastEthernet0/3  unassigned  up        up
Loopback0        10.1.1.1    up        up
Loopback100      100.0.0.1   up        up
"""