# Table de multiplication

# L’utilisateur entre un nombre n, et le programme affiche la table de multiplication de n jusqu’à 10.
# Exemple pour n = 3 :

print("")
nombre = int(input(" Entrez un nombre : "))

for i in range( 1, 11):
    resultat = nombre * i
    print(nombre , "x" , i , " = " , resultat)