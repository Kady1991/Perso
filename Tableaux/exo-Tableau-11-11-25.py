# Créer une liste de prénoms entrée par l’utilisateur,
print("")
listePrenom = []
nombre = int(input(" Combien de prenom veux-tu entrer ? "))

for i in range(nombre):
    Prenom = input(f" Le prenom {i + 1 } est : ")
    listePrenom.append(Prenom)
print("La liste des prenoms est : " , listePrenom)

for i in listePrenom:
    listePrenom.remove(listePrenom[1])
    print(" La nouvelle liste est : " , listePrenom)
# puis l’afficher, la modifier et compter combien il y en a.

    

