from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result

nr = InitNornir(config_file='config.yaml')

print(type(nr))


def host_parm(task_wgsy: Task) -> Result:
    return (task_wgsy.host.name,
            task_wgsy.host.hostname,
            task_wgsy.host.username,
            task_wgsy.host.password,
            task_wgsy.host.platform,
            task_wgsy.host.groups,
            task_wgsy.host.data)


result = nr.run(task=host_parm)
print_result(result)
