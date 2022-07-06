from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

# Standardize switchport configs with 0.5% broadcast storm control
# 使用 0.5% 广播风暴控制标准化交换机端口配置
a = parse.replace_children(r'^interface\s\S+?thernet', r'broadcast\slevel\s\S+', 'broadcast level 0.5')

print(a)
# Now save the new version...
# parse.save_as('/path/to/the/newconfig')