#Napisz program "oceny.py", który wczytuje od użytkownika kolejne oceny i:
#a) sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen
# (jeżeli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją na listę otrzymanych ocen)
#b) jeżeli wciśnięto sam Enter, oznacza to koniec listy otrzymanych ocen
#c) wyświetla wyliczoną dla listy otrzymanych ocen średnią arytmetyczną.
import statistics

list = [1,2,3,4,5,6]
oceny = []

while True:
    try:
        ocena = int(input("Podaj Ocene: "))
        if ocena in list:
            print("Jest")
            oceny.append(ocena)
        else:
            print("Nope")
            pass
    except:
        break

print("Mean Value is: ",statistics.mean(oceny))
