#initialize初始化
class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age



    def wake(self):
        print(self.name,'can walk')
        print(self.name,'is',self.age)
s1=Students('inty','18')
s1.wake()

s2=Students('james',15)
s2.wake()

















