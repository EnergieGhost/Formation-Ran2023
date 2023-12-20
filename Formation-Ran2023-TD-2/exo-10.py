print()
print("==========================================================")
print()

temperatur_anbiant = float(input("Rentre la temperature anbiant"))
temperatur_bassin = float(input("Rentre la temperature anbiant"))
diff = abs(temperatur_anbiant - temperatur_bassin)

if diff < 20 and diff > 40 :
    print("alarme")
else :
    print("RAS")

print()
print("==========================================================")
print()
