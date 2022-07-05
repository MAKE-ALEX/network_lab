from netmiko import ConnectHandler
from textfsm import TextFSM
from pprint import pprint

connection_info = {'device_type': 'huawei',
                   'ip': '192.168.59.10',
                   'username': 'python',
                   'password': '123456'}

with ConnectHandler(**connection_info) as conn:
    output = conn.send_command("display interface brief", use_textfsm=True)

print(output)
pprint(output)
