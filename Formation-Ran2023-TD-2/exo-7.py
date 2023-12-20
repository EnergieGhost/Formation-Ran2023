print()
print("==========================================================")
print()

prix_ttc = float(input("Sesir un prix TTC"))
if prix_ttc > 500 and prix_ttc < 1000 :
    print(f"la remise et de 2% le prix apres remise et de {prix_ttc * 0.98}")
elif prix_ttc > 1000 and prix_ttc < 2000 :
    print(f"la remise et de 5% le prix apres remise et de {prix_ttc * 0.95}")
elif prix_ttc > 2000 :
    print(f"la remise et de 10% le prix apres remise et de {prix_ttc * 0.90}")
print()
print("==========================================================")
print()