'''什么是*args,,就是arguments 参数'''
'''kwargs (key word args)'''

def m1(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
m1()
##############################


dic_inty={'name':'inty','age':'18 years old','height':'190cm'}

for k,v in dic_inty.items():
    print(k,':',v)
################################


dic_inty2={'name':'inty2','age':'18 years old','height':'180cm'}
def someone(dic_someone):
    for k,v in dic_someone.items():
        print(k,':',v)
someone(dic_inty2)


######所以kwargs来代替字典dic

def someone(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)
someone(name='xiao hong',age='20',height='180')





