from pprint import pprint
from ciscoconfparse import CiscoConfParse

# 从cisco1.txt中获取主机名
parse = CiscoConfParse('./cisco1.txt')

hostname = parse.re_match_iter_typed(r'hostname\s+(\S+)', default='')

pprint(hostname)
"""
很容易看出re_match_iters_typed()会自动完成find_objects()的动作，所以，在需要查找的父行下，有许多子行这样的情况。re_match_iters_typed()就会显得不实用。
"""