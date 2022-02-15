import paramiko
import time

ip = "192.168.11.11"
username = "python"
password = "123"

ssh_client = paramiko.SSHClient()
# 开启ssh客户端
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# paramiko接收所有的公钥，默认不接收。
ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
# .connect方法输入ip，username，password；look_for_keys是让paramiko不要使用系统的公钥
print("Successfully connected to ", ip)
# 成功后打印

command = ssh_client.invoke_shell()
# 把连接成功后的shell传递给command
command.send("sys\n")
command.send("interface LoopBack 0\n")
command.send("ip address 1.1.1.1 255.255.255.255\n")
command.send("return\n")
command.send("save\n")
command.send("y\n")
# 输入命令

time.sleep(3)
command.send("display this\n")
time.sleep(1)
# 要添加延迟，防止出错

output = command.recv(65535)
# recv方法打印shell回显
print(output.decode("ascii"))
# 回显的类型是字节型字符串，要用ascii解码

ssh_client.close()
# 断开连接
