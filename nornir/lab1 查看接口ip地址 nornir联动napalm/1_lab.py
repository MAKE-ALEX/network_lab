from nornir import InitNornir
# 这里我们从nornir中导入InitNornir子类，InitNornir的作用是用来初始化nornir，是nornir下面最重要的一个子类。
from nornir_napalm.plugins.tasks import napalm_get
# 另外我们还从nornir_napalm.plugins.tasks中调用了napalm_get，napalm_get这个子类允许我们调用napalm的getter类的API来获取设备的信息
from nornir_utils.plugins.functions import print_result

# 最后我们调用nornir_utils.plugins.functions中的print_result来将我们通过nornir_napalm的getter类API得到的设备信息打印出来。

"""
pip3 install netmiko
pip3 install napalm
pip3 install nornir
pip3 install nornir_utils
pip3 install nornir_napalm
pip3 install nornir_netmiko
"""

"""
使用InitNornir()函数来初始化设备并将它赋值给变量nr。
InitNonir()函数中需要放入config_file这个参数，针对这个参数这里我们使用的是前面提到的config.yaml这个文件， 
后面的dry_run参数在调用nornir_napalm时必须设为True。
"""

nr = InitNornir(config_file="config.yaml", dry_run=True)

"""
然后我们调用nr.run()函数来正式使用napalm下的两个getter类API，
"get_interfaces_ip", "get_interfaces"两个API分别用于获取接口地址和接口信息
参考:https://github.com/napalm-automation-community/napalm-huawei-vrp/blob/master/README-ZH.md
"""
results = nr.run(task=napalm_get, getters=["get_interfaces_ip"])

"""
最后用print_result()将结果打印出来
（注意这里nr.run()返回的值的类型为nornir.core.task.AggregatedResult，必须用nornir.utils里的print_result()才能将它完整打印出来，我们常用的print()对它是无效的）
"""
print_result(results)
