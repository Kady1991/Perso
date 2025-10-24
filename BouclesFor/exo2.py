# Écrire un algorithme qui lit une année et affiche si elle est bissextile ou non.

print("")
annee = int(input("Entrer une année : "))
print("")

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0) :
    print( " L'année " , annee , " est " ,  "bissextile")
else :
    print("Cette année n'est pas bissextile")
    print("")

# (Rappel : une année est bissextile si elle est divisible
#   par 4 et non divisible par 100, sauf si elle est aussi divisible par 400.)

