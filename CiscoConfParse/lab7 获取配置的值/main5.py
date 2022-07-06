from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./cisco1.txt')

intf_obj = parse.find_objects(r'^interface\s+Vlan10$')[0]

arp_timeout = intf_obj.re_match_iter_typed(r'arp\s+timeout\s+(\d+)', result_type=int, default=4 * 3600)

print(arp_timeout)

"""
使用re_match_iter_typed()，转换数据类型。把SVI10下的arp超时时间从str转换成int

re_match_iters_typed()有2个关键字属性：default、untyped_default

（1）default 关键字的意思是，如果正则表达式与配置不匹配时的默认值，该默认值会自动转换为result_type。

（2）untyped_default，如果不希望默认值转换为result_type，可以使用untyped_default=True
"""


