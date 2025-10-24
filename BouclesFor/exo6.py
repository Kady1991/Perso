# Afficher uniquement les nombres pairs de 1 à 50.
# (Indice : un nombre pair donne un reste 0 quand on le divise par 2)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)