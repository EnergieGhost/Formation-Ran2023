print()
print("==========================================================")
print()

francais = float(input("saissire votre note de francais (/20) :"))
coef_francais = int(input("entrer le coefficients (/10) :"))

math = float(input("saissire votre note de math (/20) :"))
coef_math = int(input("entrer le coefficients (/10) :"))

geo = float(input("saissire votre note de geo (/20) :"))
coef_geo = int(input("entrer le coefficients (/10) :"))

info = float(input("saissire votre note de info (/20) :"))
coef_info= int(input("entrer le coefficients (/10) :"))

while (francais > 20 or math > 20 or geo > 20 or info > 20 or coef_francais > 20 or coef_math > 20 or coef_geo> 20 or coef_info > 20) :
    francais = float(input("saissire votre note de francais (/20) :"))
    coef_francais = int(input("entrer le coefficients (/10) :"))

    math = float(input("saissire votre note de math (/20) :"))
    coef_math = int(input("entrer le coefficients (/10) :"))

    geo = float(input("saissire votre note de geo (/20) :"))
    coef_geo = int(input("entrer le coefficients (/10) :"))

    info = float(input("saissire votre note de info (/20) :"))
    coef_info= int(input("entrer le coefficients (/10) :"))


moyenne = (francais * coef_francais + math * coef_math + geo * coef_geo + info * coef_info) / (coef_info + coef_francais + coef_math + coef_geo)
print(moyenne)
if 16 <= moyenne <= 20:
    print("tres Bien")
elif 12 <= moyenne < 16 :
    print("bien")
elif 8 <= moyenne < 12 :
    print("assez bien")
elif 4 <= moyenne < 8 :
    print("inssuffisant")
elif 0 <= moyenne < 4 :
    print("nul")

print()
print("==========================================================")
print()
