from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./sw1.txt')

for ospf_areas in parse.find_objects('ospf 100'):
    # 使用children方法，直接找父行ospf100的子行area0和area1
    for ospf_area in ospf_areas.children:
        # 遍历area1和area2的子行，把包含172.16.1.1的父行找出来
        if ospf_area.re_search_children('172.16.1.1'):
            print(ospf_area.text)
