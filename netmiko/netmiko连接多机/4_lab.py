import netmiko
from netmiko import ConnectHandler, ssh_exception

# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放网络不通的设备信息
switch_not_reachable = []

with open('ip_list.txt') as f:
    for ips in f.readlines():
        try:
            ip = ips.strip()
            connection_info = {
                'device_type': 'huawei',
                'ip': ip,
                'username': 'python',
                'password': '123456',
                # 'conn_timeout':10
            }
            with ConnectHandler(**connection_info) as conn:
                print(f'已经成功登陆交换机{ip}')
                output = conn.send_command('display cur | inc sysname')
                print(output)

        except netmiko.NetmikoAuthenticationException:
            print(ip + "用户验证失败！")
            switch_with_authentication_issue.append(ip)

        except netmiko.ssh_exception.NetmikoTimeoutException:
            print(ip + "目标不可达！")
            switch_not_reachable.append(ip)

        except:
            print("未知错误")

print('\n ====结果输出====')
print('·下列交换机用户验证失败：')
for i in switch_with_authentication_issue:
    print(f"  {i}")

print('·下列交换机不可达：')
for i in switch_not_reachable:
    print(f"  {i}")
