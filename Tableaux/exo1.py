print("")
print(" ====================== LES TABLEAUX ====================================")
print("")

# Crée une liste appelée animaux contenant ["chat", "chien", "lapin"].
animaux = ["chat" , "chien" , "lapin"]
# Affiche la liste complète.
print(" Liste complete de depart " , animaux)
print("")

# Remplace "chien" par "lion".
animaux [1] = "Lion"
print(" Remplacer chien par lion" , animaux)
print("")

# Ajoute "tigre" à la fin de la liste.
animaux.append("tigre")
print(" Ajouter tigre à la fin de la liste" , animaux)
print("")
# Supprime "lapin".
animaux.remove("lapin")
# Affiche le résultat final.
print(" Suprimer lapin" , animaux)
print("")


print("================== PARCOURIR AVEC LA BOUCLE FOR ============================")
# afficher 1 par 1 avec la boucle for
for animal in animaux:
    print(" => " , animal)
print("")

print("================= Parcourir la liste avec les positions (index) : ==========")
print("")

for i in range(len(animaux)):
    print(" L'animal à la position " , i , " est ", animaux[i])
print("")