from ciscoconfparse import CiscoConfParse
BASELINE = """!
interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.0
!""".splitlines()

REQUIRED_CONFIG = """!
interface GigabitEthernet0/1
 ip address 172.16.1.1 255.255.255.0
  no ip proxy-arp
!""".splitlines()

parse = CiscoConfParse(BASELINE)

# Build diffs to convert the BASELINE to the REQUIRED config
# 构建差异以将 BASELINE 转换为 REQUIRED 配置
print(parse.sync_diff(REQUIRED_CONFIG, ''))
