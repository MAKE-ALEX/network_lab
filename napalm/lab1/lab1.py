from napalm import get_network_driver
import json

driver = get_network_driver('huawei_vrp')
SW1 = driver('192.168.59.10', 'python', '123456')
SW1.open()

output = SW1.get_arp_table()
print(output)
print(json.dumps(output, indent=2))
