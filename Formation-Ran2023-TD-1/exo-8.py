print()
print("==========================================================")
print()

produitHt = float(input("Prix du produit ht ?"))
quantite = float(input("quantite ?"))
prixHt = produitHt * quantite
remise = 15 
calcul_remise = (prixHt / 100) * remise
prixremise = prixHt - remise
tva = 20
prix_tva = (prixremise / 100) * tva
prixttc = prixremise + prix_tva
print(prixttc)

print()
print("==========================================================")
print()
