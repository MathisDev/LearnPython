text = input('Salut rentre tes coordoner en splitant comme cesi email-nom-mot de passe ').split("-")
print("Nom :{}".format(text[1]))
print("Email :{}".format(text[0]))
print("Mot de passe :{}".format(text[2]))
