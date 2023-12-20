print()
print("==========================================================")
print()

prix_ht = float(input("sesire un prix ht"))


print("Pour une TVA de 5,5 %, saisissez 1")
print("Pour une TVA de 19,6 %, saisissez 2")
print("Pour une TVA de 33 %, saisissez 3")

code_tva = int(input("Sesire le code pour la TVA"))

if code_tva == 1 :
    print(f"Le prix HT est de {prix_ht} €, la TVA est de 5,5 % et le prix TTC est de {prix_ht * 1.55} €.")
elif code_tva == 2 :
    print(f"Le prix HT est de {prix_ht} €, la TVA est de 19,6 % et le prix TTC est de {prix_ht * 1.196} €.")
else :
    print(f"Le prix HT est de {prix_ht} €, la TVA est de 33 % et le prix TTC est de {prix_ht * 1.33} €.")

print()
print("==========================================================")
print()


