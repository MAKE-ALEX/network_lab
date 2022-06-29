from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date


def backup_getports(task2):
    """功能xx：……"""
    r = task2.run(task=napalm_get, getters=["facts"])
    # print(type(r.result["facts"]["interface_list"]))
    task2.run(task=write_file, content='\n'.join(r.result["facts"]["interface_list"]),
              filename=str(task2.host.name) + "-ports-" + str(date.today()) + ".txt")


nr = InitNornir(config_file="config.yaml")
result2 = nr.run(name="正在采集交换机端口", task=backup_getports)
print_result(result2)
