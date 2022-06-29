from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result


"""
这里我们调用filter()里的filter_func参数，将lambda host: host.name=='sw4'赋值给它，
即可过滤出sw4这台交换机（注意，host.name对应的sw4是我们在hosts.yaml文件中给192.168.2.14这台交换机取的名称，
这个host.name对应的设备名称只在本地有效，和交换机真实的hostname没有任何关系，如果你在hosts.yaml中给这台交换机取名为abc，
那么这里lambda后面就要写成lambda host: host.name=='abc'）
"""
# 过滤单台
# nr = InitNornir(config_file="config.yaml")
# """
# 这里我们调用filter()里的filter_func参数，将lambda host: host.name=='sw4'赋值给它，
# 即可过滤出sw4这台交换机（注意，host.name对应的sw4是我们在hosts.yaml文件中给192.168.2.14这台交换机取的名称，
# 这个host.name对应的设备名称只在本地有效，和交换机真实的hostname没有任何关系，
# 如果你在hosts.yaml中给这台交换机取名为abc，那么这里lambda后面就要写成lambda host: host.name=='abc'）
# """
# targets = nr.filter(filter_func=lambda host: host.name == 'sw4')
# # 这里我测试了用大写'SW4'也行
# # targets = nr.filter(filter_func=lambda host: host.hostname=='192.168.11.14')#用IP进行定位
# results = targets.run(netmiko_send_command, command_string='dis arp')
# print_result(results)

# 过滤多台
nr = InitNornir(config_file="config.yaml")
switches = ['sw1', 'sw2', 'sw3']
targets = nr.filter(filter_func=lambda host: host.name in switches)
results = targets.run(netmiko_send_command, command_string='dis arp | inc 59.10')
print_result(results)
