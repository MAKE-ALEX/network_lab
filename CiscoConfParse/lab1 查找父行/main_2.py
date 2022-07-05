from ciscoconfparse import CiscoConfParse

with open('r1.txt', 'r') as f:
    cfg = f.read()
    cfg = cfg.splitlines()  # 读取r1.txt到变量cfg，按行分割成列表

parse = CiscoConfParse(cfg)

for obj in parse.find_objects('interface'):
    print(f'Object: {str(obj)}')

print('\n')

for port in parse.find_objects('interface XGE'):
    print(obj.text)
