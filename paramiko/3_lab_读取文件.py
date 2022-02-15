import paramiko
import time
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

# 此时 ip_list.txt 需要与 lab3.py 在相同的文件夹中
f = open('ip_list.txt')

for line in f.readlines():
    ip = line.strip()

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username,
                       password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 Layer3Switch-' + ip)
    # 关闭分屏功能
    command.send('screen-length 0 temporary\n')
    # 进入系统视图
    command.send('sys\n')
    # 关闭消息通知（防止log信息刷屏）
    command.send('undo info-center enable\n')

    # 将交换机默认的 mstp 修改为 stp
    command.send('stp mode stp\n')
    time.sleep(2)

    # 返回用户视图
    command.send('return\n')
    # 执行保存
    command.send('save\n')
    command.send('Y\n')
    time.sleep(2)
    output = command.recv(65535).decode('ASCII')
    print(output)
    f.close()
    ssh_client.close()