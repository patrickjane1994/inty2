#inheritance继承
class Father:
    name='inty'
    def eat(self):
        print("father can eat")

class Son(Father):
    pass#继承父亲的eat
littleInty=Son()
littleInty.eat()

#override覆盖
class Father:
    name='inty'
    def eat(self):
        print("father can eat")
class Mother:
    def walk(self):
        print('walk like mother')
class Son(Father,Mother):
    def eat(self):
        print('eat like son')#下面这个儿子eat覆盖了上面父亲的eat
littleInty=Son()
littleInty.eat()
littleInty.walk()




