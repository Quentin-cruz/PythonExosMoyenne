tab = [22, 22.6, 21.1, 21.9, 18.3, 18.7, 21.7, 21.1, 23.6, 27.4, 25.1,
       24.9, 23.7, 28.9, 23.2, 26.1, 26.1, 29.8, 28.2, 28.7, 25.9, 26.7,
       30.3, 25.2, 21.8, 22, 20.9, 20.7, 20.6, 19.5, 18.8]

valeur_minimale=tab[0]
valeur_maximale=tab[0]
étendue=0
for i in range (len(tab)):
    if tab[i]<valeur_minimale:
        valeur_minimale=tab[i]
    if tab[i]>valeur_maximale:
        valeur_maximale=tab[i]
étendue=valeur_maximale-valeur_minimale
print("L'étendue des températures est de :",étendue,)
print("La température minimale est de :",valeur_minimale,"°C")
print("La température maximale est de :",valeur_maximale,"°C")