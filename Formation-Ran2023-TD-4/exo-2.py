print()
print("==========================================================")
print()

date_user = "2011/10/17" #input("Merci de saisir une date de la forme AAAA/MM/JJ : ")

liste_date = [date_user.replace("/","")]


year = int(date_user[0:4])
month = int(date_user[5:7])
day = int(date_user[8:10])

if (month == 1 or month == 2):
    year += -1
    month += 12

nombre = day + int((13 * month + 3) / 5) + int(5 * year / 4) - int(year / 100) + int(year / 400)
nombre = nombre % 7


if month == 1:
    month = "janvier"
elif month == 2:
    month = "février"
elif month == 3:
    month = "mars"
elif month == 4:
    month = "avril"
elif month == 5:
    month = "mai"
elif month == 6:
    month = "juin"
elif month == 7:
    month = "juillet"
elif month == 8:
    month = "août"
elif month == 9:
    month = "septembre"
elif month == 10:
    month = "octobre"
elif month == 11:
    month = "novembre"
elif month == 12:
    month = "décembre"
 
if nombre == 0:
    print(f"{day} {month} {year} est un lundi")
elif nombre == 1:
    print(f"{day} {month} {year} est un mardi")
elif nombre == 2:
    print(f"{day} {month} {year} est un mercredi")
elif nombre == 3:
    print(f"{day} {month} {year} est un jeudi")
elif nombre == 4:
    print(f"{day} {month} {year} est un vendredi")
elif nombre == 5:
    print(f"{day} {month} {year} est un samedi")
elif nombre == 6:
    print(f"{day} {month} {year} est un dimanche")

print()
print("==========================================================")
print()

#ok       Demandez à saisir une date de la forme AAAA/MM/JJ (par exemple 2011/10/17) et afficher « Le
#ok       17 octobre 2011 est un lundi. » Pour connaitre le nom du jour, on part de la date avec :
#ok       • A = année complète (dans l’exemple 2011),
#ok       • M = numéro du mois (dans l’exemple 10),
#ok       • J = numéro du jour (dans l’exemple 17).
#ok       Si MM vaut 1 ou 2, il faut :
#ok       • retrancher 1 à A,
#ok       • ajouter 12 à M.
#ok       Avec ces valeurs, on calcule un nombre N
#ok       • N = J + ENT((13 * M + 3) / 5) + ENT(5 * A / 4) — ENT(A / 100) + ENT(A / 400)
#ok       • N = MOD(N ; 7)
#       N donne le nom du jour avec : 0 pour lundi, 1 pour mardi, ..., 6 pour dimanche