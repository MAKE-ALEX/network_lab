from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
# 在Nornir中我们可以使用nornir.core.filter下面的F()函数来做过滤

nr = InitNornir(config_file="config.yaml")

"""
Nornir的过滤中支持取非操作，首先我们调用nr.filter(F(groups__contains="cisco_group1")来过滤cisco_group1下的SW1和SW2，
将其赋值给变量group1，这里注意F()函数里面的groups__contains参数，中间的那个__是双下划线不是单下划线。
"""
group1 = nr.filter(F(groups__contains="huawei_group1"))

"""
然后在F的前面加上一个波浪号~对其进行取非来过滤cisco_group2下的SW3和SW4，
并将结果赋值给变量group2（因为我们这里总共只有cisco_group1和cisco_group2两个group，因此对cisco_group1取非后过滤出的就是cisco_group2）
"""
group2 = nr.filter(~F(groups__contains="huawei_group1"))

# 这里我们首先打印出group1的内容
# results = group1.run(netmiko_send_command, command_string='display ip int brief')
# results = group2.run(netmiko_send_command, command_string='display ip int brief')
results = nr.run(netmiko_send_command, command_string='display ip int brief')
print_result(results)