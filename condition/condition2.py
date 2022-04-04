# Exercice Cinema

priceT = 0
age = input("Quelle age avez vous ?")
if int(age) < 18:
    priceT += 7
else:
    priceT += 13

optionPop = input(" Voulez vous du pocorn ? (reponder par oui/non)")
if optionPop == "oui":
    priceT += 5
    print("Bonne journee le montent totale et de {} ".format(priceT))
elif optionPop == "non":
    print("Bonne journee le montent totale et de {} ".format(priceT))
else:
    print("reponce non valide ")

