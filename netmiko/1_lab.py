from netmiko import ConnectHandler

'''
net_connect.send_command()        # 向下发送命令，返回输出（基于模式）
net_connect.send_command_timing() # 沿通道发送命令，返回输出（基于时序）
net_connect.send_config_set() # 将配置命令发送到远程设备
net_connect.send_config_from_file() # 发送从文件加载的配置命令
net_connect.save_config() # 将running#config保存到startup#config
net_connect.enable() # 输入启用模式
net_connect.find_prompt() # 返回当前路由器提示符
net_connect.commit() # 在Juniper和IOS#XR上执行提交操作
net_connect.disconnect() # 关闭连接
net_connect.write_channel() # 通道的低级写入
net_connect.read_channel() # 通道的低级写入
'''

S2 = {'device_type': 'huawei',
      'ip': '192.168.59.10',
      'username': 'python',
      'password': '123456'}

connect = ConnectHandler(**S2)
print('已经成功登陆交换机' + S2['ip'])

# netmiko 已集成休眠、截屏等操作
config_commands = ['interface LoopBack 0', 'ip add 2.2.2.2 32']
# 如果需要系统视图下执行，可用 send_config_set ，会自动执行 sys
# 截屏直接作为函数返回
output = connect.send_config_set(config_commands)
print(output)

print('\n======我是分割线======\n')

# 如果需要用户视图下执行，可用 send_command
# 截屏直接作为函数返回
result = connect.send_command('display current-configuration interface LoopBack 0')
print(result)
