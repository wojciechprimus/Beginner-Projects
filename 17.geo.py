#Zdefiniuj funkcję "geo", która dla podanych trzech parametrów: n=numer elementu ciągu,
#a1=wartość pierwszego elementu ciągu (domyślnie 1),
#q=wartość iloczynu ciągu geometrycznego (domyślnie 2) zwróci n-ty element ciągu geometrycznego.

n=int(input("Podaj numer elementu ciągu: "))
a1=int(input("Podaj wartość pierwszego elementu ciągu: "))
q=int(input("Podaj wartość iloczynu ciągu geometrycznego: "))

def geo(n,a1=1,q=2):
    return a1*q**(n-1)

print(geo(n,a1,q))

#lam = lambda n,a1,q: a1*q**(n-1)               #Here is second possibilty using Lambda Function
#print(lam(n,a1,q))

