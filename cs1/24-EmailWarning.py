import subprocess
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
#为保护隐私，我的用户名和密码存在了一个python模块里
from Secret import UserName,Password


#定义存储ping返回结果的文件
File = 'd:\\michael\\Videos\\test.txt'


#定义两个用于测试ping的地址
target = '203.0.113.6'
# target = '1.2.3.4'


#定义ping指令，实例化ping的返回结果
cmd = ['ping','-n','3',target]
ping_result = subprocess.call(cmd,stdout=open(File,'w'),stderr=open(File,'w'))


#定义接收告警的邮箱地址及邮件内容
receivers = 'tea_9527@163.com'
EmailContentList = ['报告主人，一切正常！','哎呀呀，你的喵需要喝水哦！']


#定义发送邮件的函数
def sent_email(receivers, EmailContent):
    sender = UserName
    # 三个参数：第一个为邮件正文文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEMultipart() #实例化一个带附件的邮件
    message.attach(MIMEText(EmailContent, 'plain', 'utf-8'))  # 邮件正文
    message['From'] = formataddr(['邮件来自塞班', sender])  # 给定发送者
    message['To'] = formataddr(['塞班的爸爸',receivers])  # 给定接收者
    message['Subject'] = Header('欢迎加入喵星', 'utf-8') # 定义邮件主题

    # 构造附件，传送 test.txt 文件
    att = MIMEText(open(File, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att)

    smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465) #使用ssl
    smtpObj.login(UserName, Password) #邮箱登录信息
    smtpObj.sendmail(sender, receivers, message.as_string()) #发送邮件
    smtpObj.quit()
    print('邮件发送成功')


#根据ping返回码决定要发送的邮件内容
if ping_result == 0:
    EmailContent = EmailContentList[0]
    print('ping OK')
else:
    EmailContent = EmailContentList[1]
    print('ping Failed')


#发送邮件
sent_email(receivers, EmailContent)


