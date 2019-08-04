#Napisz program "login.py", który wczyta od użytkownika login i hasło.
# Jeżeli  login i hasło są prawidłowe, program powinien wyświetlić „Autoryzacja pomyślna”; inaczej – „Błąd logowania”.


dlogin = "wojciech"
dhaslo = "blokada"

login = input("Podaj login: ")
pas = input("Podaj hasło: ")

if login == dlogin and pas == dhaslo:
    print("Autoryzacja Pomyślna")
else:
    print("Błąd Logowania")
