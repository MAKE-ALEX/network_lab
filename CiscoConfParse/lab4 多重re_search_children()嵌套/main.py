from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./sw1.txt')

for obj in parse.find_objects('ospf'):
    areas = obj.re_search_children('area')
    for area in areas:
        if area.re_search_children('172.16.1.1'):
            print(area.text)
