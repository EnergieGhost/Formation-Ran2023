import math
print()
print("==========================================================")
print()


borne_depart = int(input("Borne de départ :"))
borne_arrivee = int(input("Borne d’arrivée :"))
pas = int(input("Intervale :"))

boucle = (borne_arrivee - borne_depart) / pas
boucle = math.ceil(boucle)
for i in range(0, boucle) :
    print(borne_depart, end=" ")
    borne_depart = borne_depart + pas

print()
print("==========================================================")
print()


