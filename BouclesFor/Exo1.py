# Calcul du prix avec réduction

print("")
prixArticle = int(input("entrez le prix d'un aricle : "))
print("")

if prixArticle > 100 :
    prixFinal = prixArticle - (prixArticle * 10 / 100 ) 
    print(prixFinal)
else :
    print(prixArticle)

    print("")

