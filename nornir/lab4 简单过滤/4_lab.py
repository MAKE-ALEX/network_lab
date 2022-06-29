from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
# 过滤'building'为1的设备
targets = nr.filter(level='1')
# 查询过滤后的设备的arp表
results = targets.run(netmiko_send_command, command_string='dis arp')

print_result(results)