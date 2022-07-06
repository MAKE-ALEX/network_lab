from pprint import pprint

from ciscoconfparse import CiscoConfParse

"""
Suppose you have a large switched network and need to run audits on your configurations; assume you need to build configurations which conform to the following criteria:

Access switchports must be configured with storm-control

Trunk ports must not have port-security

Timestamps must be enabled on logging and debug messages

You should follow the following steps.

Assume that you start with the following Cisco IOS configuration saved as short.conf (All the interfaces need to be changed, to conform with audit requirements):
"""
"""
假设你有一个大型交换网络，需要对你的配置进行审计；假设你需要建立符合以下标准的配置。

接入交换机端口必须配置有广播风暴控制功能

主干端口必须没有端口安全功能

必须在日志和调试信息中启用时间戳。

你应该遵循以下步骤。

假设你从以下保存为short.conf的Cisco IOS配置开始（所有的接口都需要改变，以符合审计要求）。
"""


def standardize_intfs(parse):
    # Search all switch interfaces and modify them
    # 搜索所有交换机接口并修改
    # r'^interface.+?thernet' is a regular expression, for ethernet intfs
    # r'^interface.+?thernet'是一个正则表达式，适用于以太网intfs。
    for intf in parse.find_objects(r'interface.+?thernet'):

        has_stormcontrol = intf.has_child_with(r' storm-control broadcast')
        is_switchport_access = intf.has_child_with(r'switchport mode access')
        is_switchport_trunk = intf.has_child_with(r'switchport mode trunk')

        # Add missing features
        # 增加缺少的功能
        if is_switchport_access and (not has_stormcontrol):
            intf.append_to_family(' storm-control action trap')
            intf.append_to_family(' storm-control broadcast level 0.4 0.3')

        # Remove dot1q trunk misconfiguration...
        # 删除dot1q中继线的错误配置...
        elif is_switchport_trunk:
            intf.delete_children_matching('port-security')


# Parse the config
# 解析配置
parse = CiscoConfParse('short.conf', syntax='ios')

# Ensure that 'end' at the bottom of configs doesn't break append() below...
# var = parse.find_objects('end')[0]
# pprint(var)

try:
    # parse.find_object('end')[0].delete()
    parse.delete_lines(r'end')
    parse.commit()
except IndexError():
    pass

# Add a new switchport at the bottom of the config...
# 在配置的底部添加一个新的交换机端口...

parse.append_line('interface FastEthernet0/4')
parse.append_line(' switchport')
parse.append_line(' switchport mode access')
parse.append_line('!')
parse.commit()  # commit() **must** be called before searching again
# 在再次搜索之前，必须调用commit()。

# Search and standardize the interfaces...
# 搜索和规范接口...
standardize_intfs(parse)
parse.commit()  # commit() **must** be called before searching again

# I'm illustrating regular expression usage in has_line_with()
# 我在说明正则表达式在has_line_with()中的用法
if not parse.has_line_with(r'service\stimestamp'):
    # prepend_line() adds a line at the top of the configuration
    # prepend_line()在配置的顶部添加一行。
    parse.prepend_line('service timestamps debug datetime msec localtime show-timezone')
    parse.prepend_line('service timestamps log datetime msec localtime show-timezone')

# Write the new configuration
# 编写新的配置
parse.save_as('short.conf.new')
