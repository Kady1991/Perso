# Mot de passe (sécurité)
# Demande à l’utilisateur de saisir un mot de passe.
# Tant qu’il n’écrit pas “python123”, le programme répète la demande.
# Quand le mot est correct, affiche :
# "Mot de passe accepté "

print("")

motDePasse = ""
while motDePasse != "python123":
    motDePasse = input(" Entrez le mot de passe ")

    if motDePasse == "python123":
        print( " Mot de passe accepté ")
    else:
        print("Incorrect")

print("")
