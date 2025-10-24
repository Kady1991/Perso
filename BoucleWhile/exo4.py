#  Devine le nombre
# Le programme choisit un nombre (ex : 7).
# L’utilisateur doit deviner ce nombre.
# Tant qu’il se trompe, on affiche :
# “Trop petit !” ou “Trop grand !”
# Quand il trouve, afficher : “Bravo 🎉”.
print("")
nombre = 0

while nombre != 7:
    nombre = int(input(" Veuillez rentrer le nombre choisi : "))

    if nombre == 7:
        print(" Vous avez reussi")
    
    else:
        print(" Faux")

    print("")
