#Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w ramce z gwiazdek,

text = input("Podaj tekst: ")

l=(len(text)+4)

print(l*('*'))
print('*',text,'*')
print(l*('*'))
