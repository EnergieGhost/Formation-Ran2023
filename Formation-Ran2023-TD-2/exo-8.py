print()
print("==========================================================")
print()

a = float(input("Veuiller saisire un nombre: "))
b = float(input("Veuiller saisire un nombre: "))

if a == 0 and b == 0 :
    print("l’ensemble des solutions est l’ensemble R.")
elif a == 0 and b != 0 :
    print("l’ensemble des solutions est l’ensemble vide.")
elif a != 0 :
    print("la solution est (-b / a).")

print()
print("==========================================================")
print()