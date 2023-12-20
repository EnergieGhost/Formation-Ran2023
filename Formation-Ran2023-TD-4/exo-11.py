print()
print("==========================================================")
print()

nb_nb = int(input("Combien de chiffre voulais vous saisire :"))
nb_max = 0

for i in range (0, nb_nb) :
    nb = int(input("Merci de rentre un nombre :"))
    if nb > nb_max :
        nb_max = nb
print(f"le nombre le plus grand est {nb_max}") 

print()
print("==========================================================")
print()