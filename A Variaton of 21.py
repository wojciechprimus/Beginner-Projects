from random import random
from random import randint
from random import choice
from time import sleep

score=100
round=0

E=[50,59]
D=[60,69]
C=[70,79]
B=[80,89]
A=[90,100]



i=0
list=[2,3,4,5,6,7,8,9,10]
Ace=1
face=[10]
lista=[1,2,3,4,5,6,7,8,9,10,10,10,10]

for i in range(1, 6):
    print("You have now so many points in total:",score)
    sleep(2)
    print("Now is this round: ",i)
    sleep(2)
    a = choice(lista)
    b = choice(lista)
    c=a+b
    if c>=21:
        score=score-21
        print("Yours score in total: ",score)
        break
    else:
        pass
    print("You have now so many points in this round: ",c)
    while True:
        quest2=int(input("Do You want next card?? (no=0, yes=1)"))
        if quest2==0:
            score=score-(21-c)
            print("Yours score",score)
            break
        else:
            d = choice(lista)
            print("Random value was",d)
            c=c+d
            if c>=21:
                score=score-21
                print("Yours score in total: ",score)
                break
            else:
                print("Yours score in this round are: ",c)
                pass

print("This is END of the game:")

if score in range(50, 59):
    print("You have rank E")
elif score in range(60, 69):
    print("You have rank D")
elif score in range(70, 79):
    print("You have rank C")
elif score in range(80, 89):
    print("You have rank B")
elif score in range(90, 100):
    print("You have rank A")
else:
    print("You are under value")


