#Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita.
# Napisz program "stopnie.py", który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita
# w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze.

for i in range(-20,45,5):
    far = -4 + (20+i)*1.8
    print("Stopnie Celsjusza:", i, " Stopnie Fahrenheita:", far)
