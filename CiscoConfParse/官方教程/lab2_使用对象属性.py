from ciscoconfparse import CiscoConfParse

# Parse the config into objects
# 将配置解析为对象
parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

# Choose the first interface (parent) object
# 选择第一个接口（父）对象
for intf_obj in parse.find_objects('^interface')[0:1]:
    print("Parent obj: " + str(intf_obj))

    # Iterate over all the child objects of that parent object
    # 遍历该父对象的所有子对象
    for c_obj in intf_obj.children:
        print("Child obj :    " + str(c_obj))

"""
Output:
Parent obj: <IOSCfgLine # 4 'interface GigabitEthernet 1/1'>
Child obj :    <IOSCfgLine # 5 ' switchport mode trunk' (parent is # 4)>
Child obj :    <IOSCfgLine # 6 ' shutdown' (parent is # 4)>
"""