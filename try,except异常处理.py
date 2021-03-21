


try:
    print(10/8)
    print(10+'0')
except AttributeError as e:
    print(e)
except TypeError as a:
    print(a)

###############
try:
    print(10/8)
    print(10+'0')
except AttributeError as e:
    print(e)
except Exception:
    print('there is something wrong')









