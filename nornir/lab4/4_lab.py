from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
targets = nr.filter(building='1')
results = targets.run(netmiko_send_command, command_string='dis arp')

print_result(results)