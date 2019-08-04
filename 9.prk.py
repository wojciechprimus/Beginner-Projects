# Napisz program "prk.py", który obliczy wszystkie pierwiastki rzeczywiste równania kwadratowego o postaci ax2+bx+c=0,
# gdzie a, b i c podaje użytkownik. Program powinien na początku sprawdzić, czy wprowadzone równanie jest rzeczywiście kwadratowe.

a = int(input("Podaj pierwsza wartosc rownania:", ))
b = int(input("Podaj druga wartosc rownania:", ))
c = int(input("Podaj trzecia wartosc rownania:", ))

delta = b*b-4*a*c                            # Obliczanie wartosci delta
pierd = pow(delta, 1/2)                      # Obliczanie pierwiastka delta


if a==0:
    print("Równanie liniowe")
elif delta > 0:
    m1 = round((-b-pierd)/(2*a),3)
    m2 = round((-b+pierd)/(2*a),3)
    print("Dwa miejsca zerowe: ",m1, "oraz ", m2)

elif delta == 0:
    m3 = -b/(2*a)
    print("Mamy jedno miejsce zerowe:", m3)
else:
    print("Nie ma miejsca zerowego")
