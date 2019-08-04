#Napisz program "tryg.py", który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość
# czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.

import math

degree = int(input("Give me value of degree: "))
degree = degree*0.0174533

cos = round(math.cos(degree),3)
sin = round(math.sin(degree),3)
tan = round(math.tan(degree),3)
arctan = round((tan**-1),3)

print("Output is:",
      "Cos = ",cos,
      "Sin = ",sin,
      "Tan = ",tan,
      "Arctan = ",arctan)
