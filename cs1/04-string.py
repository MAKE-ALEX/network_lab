#续行 \
xh = 'cisco and huawei are very good,and they \
also racing.'
print(xh)

#反斜杠 \\
#关于文件路径的跨平台移植方法可使用os内建模块，将在后续小节讲到
path = 'd:\\tmp\\test.txt'
print(path)

#引号 \'
daddy1 = 'who\'s your daddy'
daddy2 = "who's your daddy"
print(daddy1,'\n',daddy2,'\n',daddy1 == daddy2)

#退格 \b
print('cisco \bhuawei')
#空  最多三个0 \0  \00  \000
print('\0')

#换行 \n
print(1,'\n','\n',2)

#横向制表符 \t  一般用于对齐数据列
print("name \t 小明")
print('tel \t 1234567890')
print('addr \t beijing')

#原始字符串 r 或者 R 都可以
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#多行字符串，使用三引号，自动包含换行符，转义字符可以预防本行包含换行符；
#but it’s possible to prevent this by adding a \ at the end of the line.
#当我们需要使用python处理xml文本、sql语句、html文本等，这个语法尤其实用；
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#字符串运算符
print('cisco' 'and' 'huawei') #多个字符串自动拼接
pa = 'cisco' ; pb = 'huawei'
print(pa + 'and' + pb) #标识符与字符加法拼接
print('-'*80) #字符串乘法

#整形转换为字符串
sint = 1234567
sint1 = str(sint)
print(sint,type(sint),'\n',sint1,type(sint1))

#字符串长度测量及索引
s1 = 'supercalifragilisticexpialidocious'
print(len(s1))
print(s1[8])

#字符串切片
s1a = s1[14:18]
print(s1a)
s1b = s1[0:5]
print(s1b)
s1c = s1[-7:]
print(s1c)
s1d = s1[12:]
print(s1d)

#字符串分割   从设备获取到的就是这个 syslog
syslog= b'show cdp neighbors | begin Device\r\nDevice ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\r\ncsr1000v-1.2022skill.com\r\n                 Gig 0/2           153              R I   CSR1000V  Gig 1\r\n\r\nTotal cdp entries displayed : 1\r\nSwitch1#'
print(syslog)
print('='*80)
print(syslog.decode())  #解码为字符
print('='*80)
lines = syslog.decode().splitlines() #以换行符为记号分割为列表
print(lines[2]) # 取出CDP邻居的名称
print('='*80)
NBR_If = lines[3].split()[0] + lines[3].split()[1] #取出本地连接该邻居的接口
print(NBR_If)

#交互式字符串
# Name = input('enter your name pls:')
# print('Your name is ' + Name)

#格式化字符串
# Name = input('enter your name pls:')
# print('Your name is {}'.format(Name))
# print('Your name is %s' % Name)
# print(f'Your name is {Name}') #3.6之后增加的

#其它
qt = 'abcdefg     '
print('c' in qt)
print('c' not in qt)
print('x' in qt)
print('x' not in qt)
qt1 = qt.replace('c','C')
print(qt,qt1,'|')
qt2 = qt.strip() #默认删除字符串前后的空格，还可以删除指定字符
print(qt,qt2,'|')
