from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

intf_obj = parse.find_objects(r'interface\s+GigabitEthernet\s+1\/3')

# Search children of GigabitEthernet1/3 for a regex match and return
# the value matched in regex match group 1.  If there is no match, return a
# default value: ''
# 搜索gex接口GigabitEthernet1/3的子接口并返回
# 正则表达式匹配组1中匹配的值。如果没有匹配，返回a
# 默认值:''
intf_ip_addr = intf_obj[0].re_match_iter_typed(
    r'ip\s+address\s(\d+\.\d+\.\d+\.\d+)\s', result_type=str,
    group=1, default='')
print("ip addr: " + intf_ip_addr)