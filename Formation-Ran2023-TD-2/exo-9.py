print()
print("==========================================================")
print()

francais = float(input("saissire votre note de francais (/20) :"))
math = float(input("saissire votre note de math (/20) :"))
geo = float(input("saissire votre note de geo (/20) :"))
info = float(input("saissire votre note de info (/20) :"))

moyene = (francais + math + geo + info) /4

if moyene > 16 and moyene < 20 :
    print("tres Bien")
elif moyene > 12 and moyene < 16 :
    print("bien")
elif moyene > 8 and moyene < 12 :
    print("assez bien")
elif moyene > 4 and moyene < 8 :
    print("inssuffisant")
elif moyene > 0 and moyene < 4 :
    print("nul")

print()
print("==========================================================")
print()