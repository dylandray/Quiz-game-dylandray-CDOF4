#Le Grand Quiz


import random

Questions = [("Quel est le nom de la capitale de la France ?", "Paris"),("Quel est le nom de la capitale de l'Espagne ?", "Madrid"),("Quel est le nom de la capitale de l'Italie ?", "Rome"),("Quel est le nom de la capitale de l'Allemagne ?", "Berlin"),("Quel est le nom de la capitale de la Belgique ?", "Bruxelles"),("Quel est le nom de la capitale de la Suisse ?", "Berne"),("Quel est le nom de la capitale de la Russie ?", "Moscou"),("Quel est le nom de la capitale de la Chine ?", "Pekin"),("Quel est le nom de la capitale de l'Inde ?", "New Delhi"),("Quel est le nom de la capitale de l'Egypte ?", "Le Caire")]

points=0

while len(Questions) != 0:
    x = random.randint(0,len(Questions)-1)
    print(Questions[x][0])
    reponse = input("Votre réponse : ")
    if reponse == Questions[x][1]:
        points +=1
        print("Bonne réponse")
        del Questions[x]
    else: 
        print("Mauvaise réponse!")
        del Questions[x]

print("Vous avez eu "+str(points)+" bonnes réponses!")
if points < 3:
    print("Vous devriez réviser votre géographie..")
    
elif points < 7:
    print("Continuez vos efforts!")
    
elif points <= 9:
    print("Bon boulot !!")

elif points == 10:
    print("WOOOOOW Bravo!!! Perfect")