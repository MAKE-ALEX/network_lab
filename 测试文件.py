import os

key = ' '
while key != 'quit' and key != 'QUIT':
    print('|---------系统运维程序 @by 惰惰猴-------|')
    print('| ip 查看IP地址                     |')
    print('| disk 查看硬盘空间                   |')
    print('|------------------------------------|')
    key = input('ip/disk: ')
    match key:
        case 'ip':
            os.system('ipconfig')
        case 'disk':
            os.system('dir')
        case 'quit':
            pass
