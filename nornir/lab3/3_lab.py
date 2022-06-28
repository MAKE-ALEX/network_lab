from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
# 在Nornir中我们可以使用nornir.core.filter下面的F()函数来做过滤

nr = InitNornir(config_file="config.yaml")
group1 = nr.filter(F(groups__contains="huawei_group1"))
group2 = nr.filter(~F(groups__contains="huawei_group1"))
results = group1.run(netmiko_send_command, command_string='display ip int brief')
print_result(results)