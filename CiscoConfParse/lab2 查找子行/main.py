from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('./sw1.txt')

for port in parse.find_objects('interface'):
    # 调用re_search_children方法来查找子行
    if port.re_search_children('trunk'):
        print(port.text)
