from netmiko import ConnectHandler

"""
Netmiko 有几种发送命令的方式：

send_command - 发送一个命令
send_config_set - 在配置模式下发送命令或命令列表
send_config_from_file - 从文件发送命令（使用send_config_set内部方法）
send_command_timing - 发送命令并等待基于计时器的输出
"""

# 设置设备连接参数的字典
sw1 = {'device_type': 'huawei',
       'ip': '192.168.59.10',
       'username': 'python',
       'password': '123456'}

# 设置要执行的命令
commands = ['interface GigabitEthernet 0/0/1', 'description descby_send_config_set()']

# 连接设备，使用’with as‘可以在结束命令执行完成后自动断开ssh连接
with ConnectHandler(**sw1) as connect:
    # 用with在脚本运行完成后会自动关闭ssh连接
    print("已经成功登陆交换机" + sw1['ip'])

    print('===实验目的（1），交互形式推送一条指令。')
    output = connect.send_command('display interface description | include GE0/0/[12][^0-9]')
    print(output)

    print('===实验目的（2），列表形式推送多条指令。')
    output = connect.send_config_set(commands)
    print(output)

    print('===实验目的（3），文件形式推送多条指令。')
    output = connect.send_config_from_file('netmiko-config-lab2.txt')
    print(output)

    print('===最后再检查配置')
    output = connect.send_command('display interface description | include GE0/0/[12][^0-9]')
    print(output)

    # 华为设备的保存配置save后需要输入y进行确认，后面实验再演示。
