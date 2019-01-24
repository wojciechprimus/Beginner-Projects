from random import random
from random import randint

first=randint(18,25)
second=randint(10,35)
heal=randint(18,25)
comp=int(100)
me=int(100)

print("Let start the game:")

def com():
    global me
    global  comp
    first=randint(18,25)
    second=randint(10,35)
    heal=randint(18,25)
    c=randint(1,4)
    if c==1:
        print("Computer made this move: KICK")
        me=me-first
        print("Now yours health is:",me)
    elif c==2:
        print("Computer made this move: PUNCH")
        me=me-second
        print("Now yours health is:",me)
    else:
        print("Computer made this move: HEAL")
        comp=comp+heal
        print("Now Computer health is:",comp)

def my():
    global  comp
    global me
    first=randint(18,25)
    second=randint(10,35)
    heal=randint(18,25)
    m=int(input("Which move you wanted to make: 1-kick, 2-punch, 3-heal"))
    if m==1:
        print("You have made this move: KICK")
        comp=comp-first
        print("Now computer health is:",comp)
    elif m==2:
        print("You have made this move: PUNCH")
        comp=comp-second
        print("Now computer health is:",comp)
    else:
        print("You have made this move: HEAL")
        me=me+heal
        print("Now Yours health is:",me)


while True:
    com()
    if me<0:
        print("End of the game, Yours health reached: 0 ")
        break
    else:
        my()
        if comp<0:
            locals(comp)
            comp==0
            print("End of the game, Computer health reached: 0")
            break
        else:
            pass


