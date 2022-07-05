from ciscoconfparse import CiscoConfParse

# Parse the config into objects
parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

# Iterate over all the interface objects
for intf_obj in parse.find_objects('^interface'):
    print(f"ciscoconfparse object: {str(intf_obj)}")

"""
Output:
ciscoconfparse object: <IOSCfgLine # 4 'interface GigabitEthernet 1/1'>
ciscoconfparse object: <IOSCfgLine # 8 'interface GigabitEthernet 1/2'>
ciscoconfparse object: <IOSCfgLine # 14 'interface GigabitEthernet 1/3'>
"""