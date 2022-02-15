import napalm
import json
import napalm_huawei_vrp
from napalm import get_network_driver

driver = get_network_driver('huawei_vrp')
sw1 = driver('192.168.11.12', 'python', '123')
sw1.open()

output = sw1.get_arp_table()
print(json.dumps(output,indent=2))
