print("")

nombreMax = None

for i in range(1,6):
    nombre = int(input(" Entrez le nombre " + str(i) + " : "))
    
    if nombreMax is None or nombre > nombreMax:
        nombreMax = nombre
print(" Le plus grand est " , nombre)
print("")
