#Zdefiniuj funkcję "samogloska", która dla parametru będącego wyrazem w języku polskim,
#zwróci listę jego samoglosek. Funkcja nie musi działać perfekcyjnie dla każdego wyrazu (wyjątków itp.),
#ale im więcej przypadków obsłuży prawidłowo, tym lepiej.

list = []
sylaby = ['a','e','i','o','u','y','ą','ę','ó']
par = input("Podaj parametr do sprawdzenia: ")

for i in range(len(par)):
    check = par[i]
    if check in sylaby:
        list.append(check)
    else:
        pass

print('dla wyrazu:', par, "otrzymamy następujące samogłoski",list)
