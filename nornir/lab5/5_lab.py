from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

# # 过滤单台
# nr = InitNornir(config_file="config.yml")
# targets = nr.filter(filter_func=lambda host: host.name == 'sw4')
# # 这里我测试了用大写'SW4'也行
# # targets = nr.filter(filter_func=lambda host: host.hostname=='192.168.11.14')#用IP进行定位
# results = targets.run(netmiko_send_command, command_string='dis arp')
# print_result(results)

# 过滤多台
nr = InitNornir(config_file="config.yaml")
switches = ['sw1', 'sw2', 'sw3']
targets = nr.filter(filter_func=lambda host: host.name in switches)
results = targets.run(netmiko_send_command, command_string='dis arp | inc 11.14')
print_result(results)
