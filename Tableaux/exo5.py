print("")
listemot = []

# Demande combien de mots l’utilisateur veut saisir.
nombreChoisi = int(input(" Veuillez entrer le nombre de mots : "))
print(" Vous avez rentré " , nombreChoisi , " mots.")

# faire une boucle pour 
for i in range(nombreChoisi):
    choixMot = input(" Entrer le mot " + str(i + 1) + " : ")
    listemot.append(choixMot)

# Affiche à la fin la liste des mots entrés.
print(" La liste final de mots est " , listemot)
print("")