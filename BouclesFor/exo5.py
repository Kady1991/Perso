# Somme des nombres de 1 à 100

# Calculer et afficher la somme des nombres de 1 à 100
# Exemple : 1 + 2 + 3 + … + 100

somme = 0
for i in range(1, 101):
    somme = i + somme
    
    print(i ,  " + ", somme , " = ",  somme)