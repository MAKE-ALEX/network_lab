#导入python内建的telnetlib模块
import telnetlib
import time
import datetime
import random
import string


#获取当前日期时间并格式化成需要的字符串
DateTime = str(datetime.datetime.now())[0:-7].replace(':','_').replace(' ','_')


#实例化存储登录信息的文本文件
DeviceLoginFile = 'D:\\michael\\Videos\\login.txt'


#通过文本生成序列化数据，以元组列表形式返回每台设备的登录信息；
def generateLoginInfo(DeviceLoginFile):
    LoginInfo = []
    with open(DeviceLoginFile,mode='r') as f:
        DeviceInfo = f.readlines()
        for i in DeviceInfo:
            i = tuple(i.strip('\n').split(',')) #去掉\n 以逗号分割为列表 转成元组
            LoginInfo.append(i)
    return LoginInfo


# 定义登录并返回设备配置信息的函数
# encode/decode为 ascii，telnetlib传递的信息是标准ascii码表对应的二进制编码；
# \n 表示回车，输入命令后需要回车执行；是ascii码表中的控制字符；
# b表示通过ascii码表二进制编码 \n
def ShowRun(DeviceName, MgmtIP, Password, EnablePass):
    tn = telnetlib.Telnet(MgmtIP)
    tn.read_until(b'Password:')
    tn.write(Password.encode('ascii') + b"\n")
    tn.read_until('{}>'.format(DeviceName).encode('ascii'))
    tn.write('enable'.encode('ascii') + b"\n")
    tn.read_until(b'Password:')
    tn.write(EnablePass.encode('ascii') + b"\n")
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))
    tn.write('terminal length 0'.encode('ascii') + b"\n")
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))
    tn.write('show run'.encode('ascii') + b"\n")
    time.sleep(0.5)
    Result = DeviceName + '\n' + tn.read_very_eager().decode('ascii')
    Config = Result.replace('\r\n','\n')
    tn.close()
    return Config


#生成一个长度八位可能包含大小写字母及数字的随机密码
a = string.ascii_letters+string.digits
def generateKey():
    RandomList = random.sample(a,8)
    Key = ''.join(RandomList)
    return Key


#定义修改enable password的函数，并以字符串形式返回新的登录信息，以便保存
def ChangePass(DeviceName, MgmtIP, Password, EnablePass,NewPass):
    tn = telnetlib.Telnet(MgmtIP)
    tn.read_until(b'Password:')
    tn.write(Password.encode('ascii') + b"\n")
    tn.read_until('{}>'.format(DeviceName).encode('ascii'))
    tn.write('enable'.encode('ascii') + b"\n")
    tn.read_until(b'Password:')
    tn.write(EnablePass.encode('ascii') + b"\n")
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))
    tn.write('configure terminal'.encode('ascii') + b"\n")
    tn.read_until('{}(config)#'.format(DeviceName).encode('ascii'))
    tn.write('enable password {}'.format(NewPass).encode('ascii') + b'\n')
    tn.read_until('{}(config)#'.format(DeviceName).encode('ascii'))
    tn.write('exit'.encode('ascii') + b"\n")
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))
    tn.write('write'.encode('ascii') + b"\n")
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))
    tn.close()
    NewInfo = DeviceName + ',' + MgmtIP + ',' + Password + ',' + NewPass + '\n'
    return NewInfo


# 定义将配置写入文本文件的函数
# 文件路径需要提前创建好，不要存C盘，不要有空格，不要带中文
def config_bkp(DeviceName, Config):
    File = open('D:\\michael\\Videos\\' + DeviceName + '_' +DateTime + '.txt', mode='w')
    File.write(Config)
    File.close()
    print(DeviceName + ' config backup finished')


#将新的登录信息写入文本，带上时间日期
def SaveNewInfo(DateTime,NewInfo):
    NewLoginFile = 'D:\\michael\\Videos\\newlogin{}.txt'.format(DateTime)
    with open(NewLoginFile,mode='w') as f:
        f.writelines(NewInfo)


#调用函数，生成登录信息
LoginInfo = generateLoginInfo(DeviceLoginFile)


#等待用户输入选择，以确定执行何种功能
Choice = input('【1】backup running-config\n'
               '【2】change enable password\n'
               'enter your chonce pls:')


if Choice == '1':
    for i in LoginInfo:
        #实例化登录信息变量
        DeviceName = i[0]; Ip = i[1]; Password = i[2]; EnablePass = i[3]
        #实例化获取到的配置
        config = ShowRun(DeviceName, Ip, Password, EnablePass)
        #将配置写入文件
        config_bkp(DeviceName, config)
elif Choice == '2':
    NewInfoList = []
    for i in LoginInfo:
        #实例化登录信息变量
        DeviceName = i[0]; Ip = i[1]; Password = i[2]; EnablePass = i[3]
        #生成随机密码
        # NewPass = 'saiban'
        NewPass = generateKey()
        #修改密码并返回新的登录信息
        NewInfo = ChangePass(DeviceName, Ip, Password, EnablePass, NewPass)
        #将新的登录信息添加到列表 NewInfoList = []
        NewInfoList.append(NewInfo)
    #将新的登录信息列表写入文本
    SaveNewInfo(DateTime, NewInfoList)
else:
    print('enter error')

