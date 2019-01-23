import math
list=[]
inp=int(input("What is Yours number??"))

def isint(x):
    return math.floor(x) == x # done!

def f1(self):
    for i in range(1,(inp+1)):
        a=inp/i
        if isint(a)==True:
            list.append(a)
            list.sort()
        else:
            pass

def f2(self):
    for i in range(inp,0):
        a=inp/i
        if isint(a)==True:
            list.append(a)
            list.sort()
        else:
            pass

if inp>0:
    f1("self")
else:
    f2("self")
    print("This number is less than 0")

if len(list)==2:
    print("This is Prime Number",list)
else:
    print("This are all Factors of Yours number:",list)




