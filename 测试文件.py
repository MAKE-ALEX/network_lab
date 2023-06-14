from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command


# 需要安装pip install  nornir_table_inventory
def get_nornir_by_your_func(some_args=None, num_workers=100):
    ''' 用你能想到的手段结合封装的some_args从api或者数据库中获取数据，进行转换，转后数据示例如下'''
    data = [{'name': 'netdevops01', 'hostname': '192.168.137.201',
             'platform': 'cisco_ios', 'port': 22, 'username': 'netdevops',
             'password': 'admin123!', 'city': 'bj', 'model': 'catalyst3750',
             'netmiko_timeout': 180, 'netmiko_secret': 'admin1234!',
             'netmiko_banner_timeout': '30', 'netmiko_conn_timeout': '20'},
            {'name': 'netdevops02', 'hostname': '192.168.137.202', 'platform':
                'cisco_ios', 'port': 22, 'username': 'netdevops', 'password': 'admin123!',
             'city': 'bj', 'model': 'catalyst3750', 'netmiko_timeout': 120,
             'netmiko_secret': 'admin1234!', 'netmiko_banner_timeout': 30,
             'netmiko_conn_timeout': 20}
            ]
    runner = {
        "plugin": "threaded",
        "options": {
            "num_workers": num_workers,
        },
    }
    inventory = {
        "plugin": "FlatDataInventory",
        "options": {
            "data": data,
        },
    }
    nr = InitNornir(runner=runner, inventory=inventory)
    return nr


if __name__ == '__main__':
    nr = get_nornir_by_your_func()
    bj_devs = nr.filter(city='bj')
    r = bj_devs.run(task=netmiko_send_command, command_string='display version')
    print_result(r)