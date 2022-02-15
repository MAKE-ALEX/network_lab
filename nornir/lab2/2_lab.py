from nornir import InitNornir
# 初始化nornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
results = nr.run(netmiko_send_command, command_string='display clock')
print(type(results))
print(results)
print_result(results)