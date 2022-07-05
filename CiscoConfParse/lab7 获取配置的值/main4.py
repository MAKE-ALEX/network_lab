from pprint import pprint
from ciscoconfparse import CiscoConfParse

# 从cisco1.txt中获取SVI10下的HSRP地址
parse = CiscoConfParse('./cisco1.txt')

intf_obj = parse.find_objects(r'^interface\s+Vlan10$')[0]

hsrp_ip = intf_obj.re_match_iter_typed(r'standby\s10\sip\s(\S+)',default='')

print(hsrp_ip)

"""

"""