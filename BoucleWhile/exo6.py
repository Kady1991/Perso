# Créer un programme qui demande à l’utilisateur de deviner un code secret (par exemple 1234).
# L’utilisateur a 3 essais maximum.
print("")
print("")

codeSecret = 123
essaieMax = 3
essaie = 0
ChoixSaisi = 0

while ChoixSaisi != codeSecret and essaie < essaieMax:
    int(input(" Veuillez rentrer le code secret : "))
    essaie += 1
    reste = essaieMax - essaie

    if ChoixSaisi == codeSecret:
        print(" Code valider")

    elif reste > 0:
        print(" Mauvaise reponse , il vous reste " , reste , "essais")
    else:
        print(" Trop de tentatives")

        
print("")
print("")


# Si l’utilisateur échoue 3 fois → afficher Accès bloqué !