"""
find_objects_wo_child()同find_objects_w_child()相反，用于查找没有特定子行的父行。需要传递2个参数

（1）匹配父行的正则或者关键字

（2）匹配子行的正则或者关键字，如果子行查找的正则或关键字不存在，则返回父行

"""
import nornir

from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./cisco.txt')

if not bool(parse.find_objects(r'no cdp run')):
    cdp_intfs = parse.find_objects_wo_child(r'^interface', r'no cdp enable')

for i in cdp_intfs:
    print(i.text)

print(cdp_intfs)
