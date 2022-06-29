from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result, print_title

# 初始化
nr = InitNornir(config_file="config.yaml")

"""
定义一个函数config(cisco)用来给给4台交换机做配置， 这里注意参数名为自定义，
这里我用的是huawei。另外在run()函数里使用netmiko_send_config时，需要配置参数config_file来调用实验开始前我们准备的commands.cfg这个配置命令文件，
配置完成过后，我们继续使用netmiko_send_command来输入命令show vlan brief以验证VLAN999是否配置成功。
"""


def config(huawei):
    huawei.run(task=netmiko_send_config, config_file='commands.cfg')
    huawei.run(task=netmiko_send_command, command_string='display vlan')


print_title('正在配置VLAN999')
results = nr.run(task=config)

print_result(results)
