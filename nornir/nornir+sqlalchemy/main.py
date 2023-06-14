from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

# 使用配置文件初始化，获取回显使用模板过滤
nr = InitNornir(config_file="config.yaml")
