#传统写法

newList=[]
for i in range(11):
    newList.append(i*2)

print(newList)



#简单写法
print([i*2 for i in range(11)])

#复杂写法
list=['小明','王八']
emptyList=[]
for name in list:
    if name.startswith('王'):
        emptyList.append(name)
print(emptyList)


#简单写法
print([name for  name in list if name.startswith(('王'))])
