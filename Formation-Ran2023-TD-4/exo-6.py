print()
print("==========================================================")
print()

number_user = 19 #int(input("Merci de rentrer un Nombre : "))

binaire = ""


while number_user > 0:
    quotient = number_user // 2
    binaire = str(number_user - quotient * 2) + binaire
    number_user = quotient

print(binaire)
    
#10011
print()
print("==========================================================")
print()