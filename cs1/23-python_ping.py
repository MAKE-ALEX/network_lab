import subprocess


File = 'd:\\michael\\Videos\\test.txt'
# target = '203.0.113.6'
target = '6.6.6.6'
cmd = ['ping','-n','3',target]
ping_result = subprocess.call(cmd,stdout=open(File,'w'),stderr=open(File,'w'))


if ping_result == 0:
    print('ping OK')
else:
    print('ping Failed')

