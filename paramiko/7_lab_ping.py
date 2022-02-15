import paramiko
import time

username = 'python'
password = '123'

for i in range(11, 16):
    ip = '192.168.11.' + str(i)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username,
                       password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 Layer3Switch-' + str(i - 10) + ' ' + ip)
    # 关闭分屏功能
    command.send('screen-length 0 temporary\n')
    # 进入系统视图
    command.send('sys\n')
    command.send('dis int bri\n')
    time.sleep(2)

    # 抓取回显，放入output变量
    output = command.recv(65535).decode('ASCII').replace('\r', '')
    print(output)

    # 保存结果到python脚本同目录下的result文件夹中
    f1 = open(f".\\result\\{ip}_dis_int_bri.txt", "w")
    f1.write(output)
    f1.close()

    ssh_client.close()
