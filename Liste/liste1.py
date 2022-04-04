
onlinePlayer = ["Graver", "Anna" , "Claymax" , "Bob"]
print(onlinePlayer)

# modifier les elements

onlinePlayer[0] = 'Gravenilvec'
print(onlinePlayer)
onlinePlayer[2:4] = ["Paul", "Jacques"]

# Les modification de listes

onlinePlayer.append("Gamer1")# apppend pour en ajouter un seul 
onlinePlayer.extend["Gamer21","Gamer22"]# extend pour en ajouter plusieurs

del onlinePlayer[1] # del pour supp l'elements 1
onlinePlayer.pop(2) # pop pour supp l'elements 2
# pop et del on a peux pres la meme utilite

onlinePlayer.remove("Claymax") # remove permet de supp un element grace a son nom et pas sa position dans la liste

del onlinePlayer.clear() # Pour mettre a 0 tout la liste 

