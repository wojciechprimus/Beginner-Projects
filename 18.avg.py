#Zdefiniuj funkcję "avg", która dla dowolnej liczby parametrów zwróci ich średnią arytmetyczną (lub 0 dla 0 parametrów).
import statistics
list = []

while True:
    try:
        wart = int(input("Podaj wartosc do obliczen: "))
        list.append(wart)
    except:
        break

print("Mean Value is: ",statistics.mean(list))
