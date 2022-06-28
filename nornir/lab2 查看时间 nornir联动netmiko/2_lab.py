from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

"""
使用InitNornir()函数来初始化设备并将它赋值给变量nr。
InitNonir()函数中需要放入config_file这个参数，针对这个参数这里我们使用的是前面提到的config.yaml这个文件， 
"""
nr = InitNornir(config_file="config.yaml")

# 这里我们用netmiko的send_command函数向SW1和SW2执行display clock命令
results = nr.run(netmiko_send_command, command_string='display clock utc')
print(type(results))
print(results)
print_result(results)