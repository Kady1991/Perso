print("")
print("")

notes = []


nombre = int(input(" Veuillez entrer un nombre de note : "))
print(f" Vous avez rentrez {nombre} ")

for i in range(nombre):
    note = float(input(f" Veuillez entrer une note entre 0 et 20  : {i + 1} "  ))
    notes.append(note)

moyenne = sum(notes) / len(notes)
noteHaute = max(notes)
noteFaible = min(notes)

print(f" La liste des notes est : {notes} ")
print(f" La moyenne est : {moyenne} ")
print(f" La plus haute note est :{noteHaute} ")
print(f" La note la plus faible est : {noteFaible} ")


print("")
print("")