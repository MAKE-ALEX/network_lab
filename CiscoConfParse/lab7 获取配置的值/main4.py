from pprint import pprint
from ciscoconfparse import CiscoConfParse

# 从cisco1.txt中获取SVI10下的HSRP地址
parse = CiscoConfParse('./cisco1.txt')

intf_obj = parse.find_objects(r'^interface\s+Vlan10$')[0]

hsrp_ip = intf_obj.re_match_iter_typed(r'standby\s10\sip\s(\S+)',default='')

print(hsrp_ip)

"""
re_match_iters_typed()有2个关键字属性：default、untyped_default

（1）default 关键字的意思是，如果正则表达式与配置不匹配时的默认值，该默认值会自动转换为result_type。

（2）untyped_default，如果不希望默认值转换为result_type，可以使用untyped_default=True
"""