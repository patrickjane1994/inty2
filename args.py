'''什么是*args,,就是arguments 参数'''
#复杂写法
def add(num1,num2,num3):
    print(num1+num3+num2)
add(1,2,3)

#简单写法(args是元组tuple）

def add(*args):
    print(sum(args))
add(1,2,3)
#######
def add(*args):
    for name in args:
        print('i love',name)
add('小米','王二')





