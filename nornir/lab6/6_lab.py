from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result, print_title

nr = InitNornir(config_file="config.yaml")


def config(huawei):
    huawei.run(task=netmiko_send_config, config_file='commands.cfg')
    huawei.run(task=netmiko_send_command, command_string='display vlan summary')


print_title('正在配置VLAN999')
results = nr.run(task=config)

print_result(results)
