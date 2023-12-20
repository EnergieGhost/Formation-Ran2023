print()
print("==========================================================")
print()

francais = float(input("saissire votre note de francais (/20) :"))
coef_francais = float(input("entrer le coefficients"))
math = float(input("saissire votre note de math (/20) :"))
coef_math = float(input("entrer le coefficients"))
geo = float(input("saissire votre note de geo (/20) :"))
coef_geo = float(input("entrer le coefficients"))
info = float(input("saissire votre note de info (/20) :"))
coef_info= float(input("entrer le coefficients"))

moyenne = (francais * coef_francais + math * coef_math + geo * coef_geo + info * coef_info) / (coef_info + coef_francais + coef_math + coef_geo)

print(f"la moyenne est {round (moyenne, 2)} (/20)")

print()
print("==========================================================")
print()