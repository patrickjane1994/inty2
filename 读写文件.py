file=open('inty.txt')
text=file.read()
print(text)
file.close()#直接open,必须关闭文件夹close，不然会死机


#####################


with open('inty.txt') as f:        #使用with后不需要关闭命令close
    print(f.read())
#############
with open('inty.txt','w') as f:    #w（write）直接写入会覆盖源文件内容
    f.write('i love you')
############
with open('inty.txt','a') as f:    #a（append）会增加内容到源文件下面
    f.write('i love you')
#############
with open('inty.txt','a') as f:
    f.write('i love you\n')        #\n转行



