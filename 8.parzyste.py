#Napisz program "parzyste.py", który wczyta od użytkownika liczbę całkowitą i wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.

liczba = int(input("Podaj liczbe: ",))

if liczba%2==0:
    print("Liczba parzysta")
else:
    print("Liczba nie parzysta")
