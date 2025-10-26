# Créer un programme qui fait un compte à rebours depuis un nombre choisi par l’utilisateur jusqu’à 0.


print("")
print("")

print("===== COMPTE A REBOURS =====")
print("")

# Le programme demande un nombre de départ.
choix = int(input(" Veuillez rentrer un nombre : "))

if choix < 0:
    print(" Le chiffre doit etre superieur à 0 ")

while choix >= 0:
    print(choix)
    choix = choix - 1 

if choix < 0:
    print(" Décolage ")

    print("")

# À la fin, il affiche "Décollage ".
    
print("")