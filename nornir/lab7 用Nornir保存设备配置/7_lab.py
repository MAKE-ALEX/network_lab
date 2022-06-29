from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date

"""
创建一个函数backup_configuration(task)，在该函数中我们使用napalm中的get-config这个getter类API来获取设备的show run配置，
然后调用write_file来将show_run内容写进文本文件，该文本文件名称的格式为swx-yyyy-mm-dd.txt
"""


def backup_configurations(task1):
    r = task1.run(task=napalm_get, getters=["config"])
    task1.run(task=write_file, content=r.result["config"]["running"],
              filename=str(task1.host.name) + "-" + str(date.today()) + ".txt")


nr = InitNornir(config_file="config.yaml")
# 除了实验6中提到的print_title()外，我们还可以在nr.run()里面加入参数name来给nornir的输出内容加上标题和脚注。
result = nr.run(name="正在备份交换机配置", task=backup_configurations)
print_result(result)
