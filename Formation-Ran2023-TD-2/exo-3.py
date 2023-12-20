import datetime

print()
print("==========================================================")
print()

current_date = datetime.date.today()

current_year = current_date.year

date_bebe = int(input("Saisire la date de naissance du bebe"))

age_bebe = current_year - date_bebe
if age_bebe < 3:
    print("Votre bebe a gagner une palette de petit pots")
else:
    print("Votre bebe a plus de 3 ans dommage")



print()
print("==========================================================")
print()
