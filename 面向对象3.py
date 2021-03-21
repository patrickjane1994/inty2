class Student:
    name='inty'
    age=18
    def eat(self):
        print(self.name,"can eat"+'and he is',self.age)
#因为name,age的赋值不是在def这个method里面所以必须加一个self来指定是在Student里面。
    @staticmethod  #静态的方法，不能调用name,age
    def walk():
        print('student can walk')

Student1=Student()
Student1.eat()
Student1.walk()

Student2=Student()
Student2.eat()
Student2.walk()