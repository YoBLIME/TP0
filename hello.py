import math
#TODO Affichez l'aire d'un cercle avec le rayon indiqué
def aire_cercle (rayon):
    return math.pi * rayon**2
    
rayon = 4
aire = aire_cercle(rayon)
print(f"l'aire de ce cercle de rayon" ,rayon, "est:" ,aire)

#TODO Ajoutez une ligne qui affichera votre nom et prénom à la fin
nom = "Blime"
prenom = "Alvyn Yoan"
print (nom +" "+ prenom)
