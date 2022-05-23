class cat():
    count = 0
    print('现在一共有 {} 只猫。'.format(count))
    __sex = 'secret'
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        self.__sex = ''
        print('已经有 {} 只猫了，算上这只就有 {} 只了。'.format(self.count,self.count+1))
        cat.count += 1
    def ShowCat(self):
        Result = '{} 的年龄是 {} 岁'.format(self.Name,self.Age)
        print(Result)
        return Result

class orange_cat(cat):
    def __init__(self,name,age,grade):
       cat.__init__(self,name,age)
       self.Grade = grade

    def ShowCat(self):
        Result = '{} 的年龄是 {} 岁，性别是 {}.'.format(self.Name,self.Age,self.Grade)
        print(Result)
        return Result

saiban = orange_cat('saiban',2,'male')
saiban.ShowCat()
