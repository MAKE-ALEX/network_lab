from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./exampleswitch.conf', syntax='ios', factory=True)
intf = parse.find_objects(r'interface\s+GigabitEthernet\s+1/3')[0]

print(intf)
print(intf.name)
print(intf.ipv4_addr)
print(intf.ipv4_netmask)
