myDic = {"key":"value","key2":"value"}


myPhones={"Iphone X":"1000","Sumsang":"900"}
Iphone_Price=myPhones["Iphone X"]
print(Iphone_Price)
print("Iphone Price:"+str(Iphone_Price))
#改价格
myPhones["Iphone X"]=500
print(myPhones)
myPhones.clear()
print(myPhones)