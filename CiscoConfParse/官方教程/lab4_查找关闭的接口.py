from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

for intf_obj in parse.find_objects_w_child('^interface', '^\s+shutdown'):
    print("Shutdown: " + intf_obj.text)

"""
Output:
Shutdown: interface GigabitEthernet1/1
"""
