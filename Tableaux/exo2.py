# Crée une liste nombres = [2, 4, 6, 8, 10]
print("")
print("")

listes = [2, 4, 6, 8, 10]

# Utilise une boucle for pour afficher chaque nombre.
for liste in listes:
    print(" => " , liste)
print("")

# Puis, affiche le double de chaque nombre (ex: 2 → 4, 4 → 8, etc.)

for i in range(len(listes)):
    print(" Le douche de ", listes[i] , "est " , listes[i] * 2 )
print("")
print("")

