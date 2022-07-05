from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

# Choose the first interface (parent) object
for intf_obj in parse.find_objects('^interface')[0:1]:
    print(intf_obj.text)

"""
Output:
interface GigabitEthernet 1/1
"""