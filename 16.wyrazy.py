#Napisz program "wyrazy.py", który wczyta od użytkownika pewien tekst, a następnie podzieli go na zdania
# (zakładamy, że jednoznacznie kropka rozdziela zdania) i dla każdego zdania wyświetli ile jest w nim wyrazów
# (zakładamy, że spacja oddziela wyrazy w zdaniu).

text = input("Podaj text:")
print(text)
zdania = []

zdania = text.split('.')
dl = int(len(zdania))

for i in range(0,(dl-1)):
    jed = zdania[i].split()
    print("Dlugosc zdania:",len(jed), zdania[i],)
