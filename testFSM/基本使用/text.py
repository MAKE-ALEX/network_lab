import textfsm

traceroute = '''
r2#traceroute 90.0.0.9 source 33.0.0.2
traceroute 90.0.0.9 source 33.0.0.2
Type escape sequence to abort.
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 msec 0 msec
  2 15.0.0.5  0 msec 5 msec 4 msec
  3 57.0.0.7  4 msec 1 msec 4 msec
  4 79.0.0.9  4 msec *  1 msec
'''

with open('traceroute.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)

"""
Value ID (\d+)- 这一行定义了一个ID描述正则表达式的变量：(\d+)- 一个或多个数字，这里是跳数
Value Hop (\S+)- 定义一个Hop通过这种正则表达式描述 IP 地址的变量的行
行后Start，模板本身开始。在这种情况下，它非常简单：

^  ${ID} ${Hop} -> Record
首先是插入符号，然后是两个空格和ID和Hop变量
在 TextFSM 中，变量是这样写的：${variable name}
末尾的wordRecord表示匹配正则表达式的行将被处理并包含在 TextFSM 的结果中
"""

'''
traceroute - 包含 traceroute 命令输出的变量
template = open('traceroute.template')- TextFSM 模板文件的内容被读入模板变量
fsm = textfsm.TextFSM(template)- 在 TextFSM 中处理模板并从中创建对象的类
result = fsm.ParseText(traceroute)- 根据模板处理输出并返回列表列表的方法，其中每个元素都是已处理的字符串
最后print(fsm.header)显示包含变量名称和处理结果的标题
'''