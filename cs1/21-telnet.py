import telnetlib
import time

DeviceName = 'R1'; MgmtIP = '203.1.113.1'; Password = 'saiban'

tn = telnetlib.Telnet(MgmtIP) #实例化telnet连接对象
tn.read_until(b'Password:') #读取回显，直到这个字符串
tn.write(Password.encode('ascii') + b"\n") #以字节码方式输入密码并回车
tn.read_until('{}>'.format(DeviceName).encode('ascii')) #读取到指定字节码
tn.write('enable'.encode('ascii') + b"\n")
tn.read_until('Password:'.encode('ascii')) #这种方式读也可以
tn.write(Password.encode('ascii') + b"\n")
tn.read_until('{}#'.format(DeviceName).encode('ascii'))
tn.write('terminal length 0'.encode('ascii') + b"\n")
tn.read_until('{}#'.format(DeviceName).encode('ascii'))
tn.write('show run'.encode('ascii') + b"\n")
time.sleep(0.5) # 给计算机一点计算和通信的时间
a = DeviceName + '\n' + tn.read_very_eager().decode('ascii')
aa = a.replace('\r\n','\n') # 回忆回车和换行
tn.close()
print(aa)

