from random import randint
print()
print("==========================================================")
print()
nb_utilisateur = 0
nb_programe = randint(0,10)

while(nb_utilisateur != nb_programe):
    nb_utilisateur = int(input("Merci de saisire un nombre de 1 et 10 :"))   
    if nb_utilisateur > 10:
        print("valeur non permise")
    elif nb_utilisateur > nb_programe :
        print("Trop grand")
    elif nb_utilisateur < nb_programe : 
        print("Trop petit")
    elif nb_utilisateur == nb_programe :
        print("Gagné")
  
print()
print("==========================================================")
print()
