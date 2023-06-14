from ciscoconfparse import  CiscoConfParse

parse = CiscoConfParse('./exampleswitch.conf', syntax='ios')

ddd = parse.find_objects(r'^interface')
# 查找父类对象

var = parse.find_lineage(ddd[], linespec='')
print(var)
# 返回对象最远的父项
parse.find_lines()
parse.find_children()
parse.find_blocks()
parse.find_objects_w_child()
parse.find_objects_w_parents()

parse.re_search_children()
parse.re_match_iter_typed()

parse.replace_children()