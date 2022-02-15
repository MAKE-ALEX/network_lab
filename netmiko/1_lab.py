from netmiko import ConnectHandler

S2 = {'device_type': 'huawei',
      'ip': '192.168.11.12',
      'username': 'python',
      'password': '123'}

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
