
# Lire une note sur 20 et afficher :
print("")
note = int(input("Entrez la note : "))
if note > 20 or note < 0 :
    print("note incorrecte")
    
# “Excellent” si la note ≥ 16
elif note >= 16:
    print("Excellent")

# “Bien” si la note ≥ 14
elif note  >= 14:
    print("Bien")

# “Assez bien” si la note ≥ 12
elif note >= 12:
    print("Assez bien")

# “Passable” si la note ≥ 10
elif note >= 10:
    print("Passable")

# “Insuffisant” sinon
else:
    print("Insuffisant")