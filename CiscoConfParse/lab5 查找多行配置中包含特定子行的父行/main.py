"""
find_objects_w_child()用于查找多行配置中包含特定子行的父行。

需要传递2个参数：

（1）parentspec，指定要查找的父行

（2）childspec，指定要查找的子行。如果childspec搜索的结果存在，则返回父行
"""

from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./cisco.txt')

qos_int = parse.find_objects_w_child(parentspec=r'^interface', childspec=r'service-policy \w+\s+\w+')
# 可以匹配正则使用

print(qos_int)
