#Napisz program "odsetki.py", który obliczy stan konta za N lat, gdzie stan początkowy konta wynosi SPK,
#a stopa oprocentowania P % rocznie (obowiązuje roczna kapitalizacja odsetek). N, SPK i P podaje użytkownik programu.

SPK = int(input("Stan Poczatkowy konta wynosi: ",))
N = int(input("Ilosc lat trwania : ",))
P = int(input("Stopa oprocentowania rocznie(100==100%): ",))
ASK = SPK #Aktualny stan konta

for i in range(1,N+1):
    ASK = ASK*P/100+ASK
    print("Stan konta po", i, "Okresie wynosi", ASK)
