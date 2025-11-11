# Créer une liste de prénoms entrée par l’utilisateur,
print("")

listePrenom = []
nombre = int(input(" Combien de prénom voulez-vous entrer ? "))


for i in range(nombre):
    Prenom = (input( f" le prenom  {i+1} est : "))
    listePrenom.append(Prenom)
print(f" La liste est {listePrenom} ")
listePrenom.append('jolie')
print(" La nouvelle liste est" , listePrenom)

print("")


# puis l’afficher, la modifier et compter combien il y en a.

    

