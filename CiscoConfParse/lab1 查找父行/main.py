from ciscoconfparse import CiscoConfParse

# # 使用CiscoConfParse传入的配置会被解析成一个列表对象，这个对象的名字就叫IOSCfgLine
# parse = CiscoConfParse([
#     '#',
#     'interface GE1/0/0',
#     ' ip address 10.1.1.1 255.255.255.252',
#     ' undo shutdown',
#     'interface XGE1/0/1',
#     ' ip address 10.1.1.5 255.255.255.252',
#     ' undo shutdown',
#     'interface XGE1/0/2',
#     ' ip address 10.1.1.9 255.255.255.252',
#     ' undo shutdown'
# ])
#
# # 有兴趣的朋友可以自行查看一下parse的对象类型
# # print(type(parse))
# # print(parse)
#
# # 因为parse是一个列表，所以可以用for循环遍历
# for obj in parse.find_objects('interface'):
#     print(f'Object: {str(obj)}')
#
# print('\n')
#
# # 使用find_objects方法可以快速的匹配父行，当然，也可以用正则匹配
# for port in parse.find_objects('interface XGE'):
#     # 调用text属性，把IOSCfLine对象的父行转换成文本
#     print(obj.text)

parse = CiscoConfParse('./r1.txt')

for obj in parse.find_objects('interface'):
    print(f'Object: {str(obj)}')

print('\n')

for port in parse.find_objects('interface XGE'):
    print(obj.text)
