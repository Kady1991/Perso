# Apprendre à faire des calculs sur toute une liste, comme :
print("")
print(" ================= SOMME TOTAL ET MOYENNE ====================")
print("")

# la somme totale et la moyenne
nombres = [2, 4, 6, 8, 10]
somme = 0
moyenne = 0

for nombre in nombres:
    somme = somme + nombre
    moyenne = somme / len(nombres)

print(" La somme est " ,  somme , " et la moyenne est " , moyenne )

print("")
print("")
print("===== PLUS GRAND ET PLUS PETIT NOMBRE =====")
print("")



# On suppose d'abord que le plus grand et le plus petit sont le premier élément

nombres = [2, 4, 6, 8, 10]
max = nombres[0]
min = nombres[0]

for nombre in nombres:
    if nombre > max:
        max = nombre
    if nombre < min:
        min = nombre
print(" Le plus grand est" , max , " et le plus petit " , min)

print("")
print("")
# trouver le plus grand ou le plus petit nombre