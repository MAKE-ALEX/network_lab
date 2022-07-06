from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./cisco1.txt')


retval = list()

HELPER_REGEX = r'ip\s+helper-address\s+(\S+)'

NO_MATCH = '__no_match__'

for intf_obj in parse.find_objects(r'^interface\s+Vlan10$'):
    for child_obj in intf_obj.children:
        val = child_obj.re_match_typed(HELPER_REGEX, default=NO_MATCH)
        if val != NO_MATCH:
            retval.append(val)


print(retval)
