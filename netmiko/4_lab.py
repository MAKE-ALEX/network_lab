import netmiko
from netmiko import ConnectHandler, file_transfer

sw1 = {'device_type': 'huawei',
       'ip': '192.168.11.12',
       'username': 'python',
       'password': '123',
       'secret': '123'}

with ConnectHandler(**sw1) as connect:
    print("已经成功登陆交换机" + sw1['ip'])

    output = connect.send_command_timing(command_string="dir", )
    output += connect.send_command_timing(command_string="ftp 192.168.11.11")
    output += connect.send_command_timing(command_string="python")
    output += connect.send_command_timing(command_string="123")
    output += connect.send_command_timing(command_string="dir")
    output += connect.send_command_timing(command_string="get text.txt")
    output += connect.send_command_timing(command_string="quit")
    print(output)
