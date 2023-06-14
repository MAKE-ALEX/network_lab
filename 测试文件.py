import telnetlib  # 导入telnetlib模块
import time

# 定义设备信息数据
DeviceInfo = [
    ('SW1', '192.168.20.30', '32772', 'saiban'),
    ('SW2', '192.168.20.30', '32773', 'saiban'),
    ('SW3', '192.168.20.30', '32774', 'saiban')
]


# 定义函数，用于telnet登录设备并返回syslog
def TELNET(DeviceName, MgmtIP, port, Password):
    tn = telnetlib.Telnet(MgmtIP, port=port)  # 实例化telnet类，给出IP地址；
    # tn.read_until(b'Password:')  # 读取回显，直到读取出 Password: b后面跟字符串表示这是字节对象，此处的编码格式遵循telnetlib模块要求；
    # tn.write(Password.encode('ascii') + b"\n")  # 发送密码 encode和decode函数的作用是以指定的方式编码和解码字符串；
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"\n")
    time.sleep(1)
    tn.read_until(f'{DeviceName}>'.encode())
    tn.write('terminal length 0'.encode('ascii') + b"\n")
    tn.read_until(f'{DeviceName}>'.encode())
    tn.write('show cdp neighbors'.encode('ascii') + b"\n")
    time.sleep(1)
    Syslog = tn.read_very_eager().decode()
    print(Syslog)
    tn.close()
    return Syslog


# 定义函数，用于将syslog写入文件
def BkpSyslog(DeviceName, Syslog):
    with open(f'{DeviceName}_CdpNbr.txt', mode='w') as f:
        f.write(Syslog)


if __name__ == '__main__':
    for a, b, c, d in DeviceInfo:
        SysLog = TELNET(a, b, c, d)
        BkpSyslog(a, SysLog)

