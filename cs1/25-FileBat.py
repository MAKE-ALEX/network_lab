import os
import shutil


Path = 'e:\\tmp\\' #定义要操作的目录
FileType = ['txt','jpg','bat','py'] #定义要创建的文件类型，用于后续实验的测试
AllFileNameList = [] #准备一个存储所有文件名的列表


#创建几个文件类型的子文件夹
def CreateDIRs(filetype):
    for Type in filetype:
        FullPath = os.path.join(Path,Type)
        os.mkdir(FullPath)


#批量产生文件,每种一百个
def CreateFiles(path,type):
    for Type in type:
        for Index in range(0,100):
            FileName = '{}\\file{}.{}'.format(path,Index,Type)
            with open(FileName,mode='w+'):
                pass


#获取当前目录下所有对象，包括目录和文件，当前只有文件
#思考，当有子目录的情况下，怎么办呢？
FileNameList = os.listdir(Path)


#定义函数，获取当前目录及子目录下的所有文件
#思考，为什么列表不能定义在函数内部，然后返回呢？
def AllFiles(path,AllFileNameList):
    CurrentList = os.listdir(path) #读取当前目录下所有对象形成列表
    for obj in CurrentList: #遍历列表
        Current_path = os.path.join(path,obj) #将所有对象形成绝对路径
        if os.path.isdir(Current_path): #如果是目录则执行自我迭代
            AllFiles(Current_path,AllFileNameList) #检查是否有子目录
        elif os.path.isfile(Current_path):
            AllFileNameList.append((Current_path,obj)) #返回绝对路径和文件名
        else:
            pass
    return AllFileNameList


#进行文件整理，根据扩展名将文件自动移动到对应的子目录
def SortFiles(allfiles,path):
    for File in allfiles:
        f_Type = File[1].split('.')[-1]
        shutil.move(File[0],path+f_Type)


#批量重命名
def renames(allfiles,path):
    for file in allfiles:
        type = file[1].split('.')[-1] #判断文件类型
        path_type = os.path.join(path,type) #生成类型路径
        NewName = type + '_' + file[1] #修改文件名，前面增加一个前缀
        NewFull = os.path.join(path_type,NewName) #生成绝对路径
        os.rename(file[0],NewFull) #修改文件名


#批量修改扩展名，在最后增加一个下划线
def re_ext(allfiles,path):
    for file in allfiles:
        type = file[1].split('.')[-1] #判断文件类型
        path_type = os.path.join(path,type) #生成类型路径
        NewName = file[1] + '_' #修改文件名，在最后增加一个下划线
        NewFull = os.path.join(path_type,NewName) #生成绝对路径
        os.rename(file[0],NewFull) #修改文件名


#文件批量删除
def DelAll(allfiles,path):
    for file in allfiles:
        os.remove(file[0])
    ObjList = os.listdir(path)  # 实例化目录下对象
    for dir in ObjList:
        c_dir = os.path.join(path,dir)
        shutil.rmtree(c_dir)


if __name__ == '__main__':
    # pass
    Choice = input('[1] for Create DIRs \n'
                   '[2] for Create Files \n'
                   '[3] for Sort Files \n'
                   '[4] for rename files \n'
                   '[5] for fix extend names \n'
                   '[6] for delete all files \n'
                   'enter your choice pls:')
    if Choice == '1':
        CreateDIRs(FileType)
    elif Choice =='2':
        CreateFiles(Path, FileType)
    elif Choice == '3':
        SortFiles(AllFiles(Path, AllFileNameList),Path)
    elif Choice == '4':
        renames(AllFiles(Path, AllFileNameList),Path)
    elif Choice == '5':
        re_ext(AllFiles(Path, AllFileNameList), Path)
    elif Choice == '6':
        DelAll(AllFiles(Path, AllFileNameList),Path)
    else:
        print('I am groot.')

