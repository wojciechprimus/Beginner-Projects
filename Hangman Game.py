
import random
i=1
game=["bike","travel","watch","keys","paint","blue","swim","plane","house","trip","boat","print"]
game=random.choice(game)
lista=list(game)
win=['x','x','x','x','x','x','x','x','x','x']
length=int(len(lista))
chance=int(input("How many chance You wanted to have??"))
chance=chance+1

win2=win[:length]
print("This is the word You were looking for",win2)

while True:
    if i==chance:
        print("You lost all of your chances, END of the game")
        print("The answer was: ",game)
        break
    you=input("what kind of letter You are asking for?? ")
    il=game.count(you)
    if you==game:
        print("You won the game!! ")
        print("You tried so many times: ",i)
        break
    elif il==0:
        print("This letter doesn`t exist in my string")
        i=i+1
    elif il>=1:
        wh=lista.index(you)                 #Checking the index of value wh in a list
        win2.pop(wh)                        #Remove the item at the index[wh] in a list "win2"
        win2.insert(wh,you)                 #Insert the letter(you) at the index[wh] in a list "win2"
        lista.pop(wh)
        lista.insert(wh," ")
        while True:
            if you in lista:
                print("this exist more times")
                wh=lista.index(you)
                win2.pop(wh)
                win2.insert(wh,you)
                lista.pop(wh)
                lista.insert(wh," ")
            else:
                break
        print("This is yours word now",win2)
        i=i+1
    ask=int(input("Do You want to give up??(yes=1,no=0)"))
    if ask==1:
        i=chance
        break
    else:
        pass
    continue


