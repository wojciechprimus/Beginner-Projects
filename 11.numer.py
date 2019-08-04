#Napisz program "numer.py", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
#a) znaki nie będące cyframi mają być ignorowane
#b) konwertujemy cyfry, nie liczby, a zatem:
#- 911 to "dziewięć jeden jeden"
#- 1100 to "jeden jeden zero zero"

list = []
liczby = input("Podaj Ciąg Liczbowy: ")
le = len(liczby)

for i in range(0,le):
    l = int(liczby[i])
    if l == 0:
        list.append("zero")
    elif l == 1:
        list.append("jeden")
    elif l == 2:
        list.append("dwa")
    elif l == 3:
        list.append("trzy")
    elif l == 4:
        list.append("cztery")
    elif l == 5:
        list.append("piec")
    elif l == 6:
        list.append("szesc")
    elif l == 7:
        list.append("siedem")
    elif l == 8:
        list.append("osiem")
    elif l == 9:
        list.append("dziewiec")

print(liczby ,' '.join(list))


