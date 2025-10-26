# Mot de passe (sécurité)
# Demande à l’utilisateur de saisir un mot de passe.
# Tant qu’il n’écrit pas bonjour, le programme répète la demande.
# Quand le mot est correct, affiche :
# "Mot de passe accepté "
print("")
print(" ===== CONTROLE D'ACCES ====")
print("")

motDePasse = "bonjour"
tentative = 0
tentativeMax = 2
choix = 0

while choix != motDePasse and tentative < tentativeMax:
    choix = str(input(" Veuillez entrer un mot de passe : "))
    tentative += 1
    reste = tentativeMax - tentative

    if choix == motDePasse:
        print(" Mot de passe accepté  ")  
    elif reste > 0:
        print(" il vous reste " , reste , "tentative ")
    else:
        print(" Acces bloqué")

# attention a la tabutation
print("")
