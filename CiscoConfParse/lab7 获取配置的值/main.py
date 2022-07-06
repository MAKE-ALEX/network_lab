# 从cisco1.txt中获取主机名
from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./cisco1.txt')

global_obj = parse.find_objects(r'^hostname')[0]

hostname = global_obj.re_match_typed(r'^hostname\s+(\S+)', default='')

print(hostname)

"""
熟悉了CiscoConfParse的父子缩进关系后，就可以使用

re_match_typed() 从对象中获取值

re_match_iter_typed() 遍历所有子节点并获得一个值

从配置中获取特定的值了。没错，使用他们的前提是，需要了解一些正则表达式的知识。
"""
"""
re_match_typed，可以从对象中来获取想要的值
"""