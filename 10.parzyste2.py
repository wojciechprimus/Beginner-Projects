# Napisz program "parzyste2.py", który wczyta od użytkownika liczbę całkowitą i bez użycia instrukcji "if"
# wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.

liczba = int(input("Podaj liczbe całkowitą: ",))
check = (liczba%2==0)

while check == True :
    print("Parzysta")
    break
else:
    print("Nie parzysta")

