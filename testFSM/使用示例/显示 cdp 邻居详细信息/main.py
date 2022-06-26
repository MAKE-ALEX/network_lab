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
[['SW1', 'R2', '10.2.2.2', 'Cisco 2911', 'GigabitEthernet1/0/21', 'GigabitEthernet0/0', '15.2(2)T1']]
LOCAL_HOST    DEST_HOST    MGMNT_IP    PLATFORM    LOCAL_PORT             REMOTE_PORT         IOS_VERSION
------------  -----------  ----------  ----------  ---------------------  ------------------  -------------
SW1           R2           10.2.2.2    Cisco 2911  GigabitEthernet1/0/21  GigabitEthernet0/0  15.2(2)T1
"""

