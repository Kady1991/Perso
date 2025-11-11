# Contient une liste de nombres (par exemple [12, 45, 23, 67, 34, 89, 10])


listes = [12, 45, 23, 67, 34, 89, 10]
somme = 0
moyenne = 0
plusGrand = listes[0]
plusPetit = listes[0]

for liste in listes:
    somme = somme + liste

    if liste > plusGrand:
        plusGrand =  liste
    if liste < plusPetit:
        plusPetit = liste


    moyenne =  somme / len(listes)
print("")
print("::::::::::::::::: ANALYSE TABLEAU ::::::::::::::::::")
print("")
print( " La somme total est :" ,  somme)
print("")
print(" La moyenne est :" , moyenne)
print("")
print(" Le plus grand est :" , plusGrand)
print("")
print(" Le plus petit est " , plusPetit)
print("")
print("")