from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

# 使用配置文件初始化，获取回显使用模板过滤
nr = InitNornir(config_file="config.yaml")
output = nr.run(netmiko_send_command, command_string='display current-configuration | be interface GigabitEthernet',
                use_textfsm=True)

# dict_keys(['sw1', 'sw2', 'sw3', 'sw4'])
# print(output.keys())

for switch in output.keys():
    print(output[switch].result)  # 这种可以用来调测，探寻返回是啥，具体操作思路在lab11、12中介绍了。
    for i in range(len(output[switch].result)):
        trunk_cmd = ['interface ' + output[switch].result[i]['interface'], 'description Trunk Port (Nornir)']
        access_cmd = ['interface ' + output[switch].result[i]['interface'], 'description Access Port to VLAN ' +
                    (output[switch].result[i]['vlan'] if output[switch].result[i]['vlan'] else '1') + ' (Nornir)']
        # a if a else b的逻辑，假如access接口没有配置VLAN，用VLAN 1补上
        # print(trunk_cmd,',', access_cmd)
        if 'trunk' in output[switch].result[i]['mode']:
            nr.run(netmiko_send_config, config_commands=trunk_cmd)
            print(switch, output[switch].result[i]['interface'], '已配置完成')
        elif 'access' in output[switch].result[i]['mode']:
            nr.run(netmiko_send_config, config_commands=access_cmd)
            print(switch, output[switch].result[i]['interface'], '已配置完成')

results = nr.run(netmiko_send_command, command_string='display interface description | inc Nornir')
print_result(results)
