import netmiko
from netmiko import ConnectHandler, file_transfer

sw1 = {'device_type': 'huawei',
       'ip': '192.168.11.12',
       'username': 'python',
       'password': '123',
       }

with ConnectHandler(**sw1) as connect:
    print("已经成功登陆交换机" + sw1['ip'])

    output = connect.send_command(command_string="save",
                                  # 发送指令
                                  expect_string=r"Are you sure to continue",
                                  # 监听回传
                                  strip_prompt=False,
                                  strip_command=False)
    output += connect.send_command(command_string="y",
                                   expect_string=r">",
                                   strip_prompt=False,
                                   strip_command=False)

    print(output)
