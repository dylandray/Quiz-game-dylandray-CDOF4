#Le Grand Quiz


import random
import time


def GrandQuiz():
    QuestionsFacile = [("Quel est le nom de la capitale de la France ?", "Paris"),("Quel est le nom de la capitale de l'Espagne ?", "Madrid"),("Quel est le nom de la capitale de l'Italie ?", "Rome"),("Quel est le nom de la capitale de l'Allemagne ?", "Berlin"),("Quel est le nom de la capitale de la Belgique ?", "Bruxelles"),("Quel est le nom de la capitale de la Suisse ?", "Berne"),("Quel est le nom de la capitale de la Russie ?", "Moscou"),("Quel est le nom de la capitale de la Chine ?", "Pekin"),("Quel est le nom de la capitale de l'Inde ?", "New Delhi"),("Quel est le nom de la capitale de l'Egypte ?", "Le Caire")]

    QuestionsMoyen = [
        ("Quelle est la capitale du Vietnam?", "Hanoï"),
        ("Quelle est la capitale de la Grèce ?", "Athènes"),
        ("Quelle est la capitale de l'Angleterre ?", "Londres"),
        ("Quelle est la capitale du Japon ?", "Tokyo"),
        ("Quelle est la capitale de l'Australie ?", "Canberra"),
        ("Quelle est la capitale du Maroc ?", "Casablanca"),
        ("Quelle est la capitale de la Corée du Sud ?", "Séoul"),
        ("Quelle est la capitale du Pérou ?", "Lima"),
        ("Quelle est la capitale du Brésil ?", "Brasília"),
        ("Quelle est la capitale des États-Unis ?", "Washington D.C")
    ]

    QuestionsDures = [
        ("Quelle est la capitale du Bangladesh ?", "Dacca"),
        ("Quelle est la capitale de l'Oman ?", "Mascate"),
        ("Quelle est la capitale du Mozambique ?", "Maputo"),
        ("Quelle est la capitale de la Croatie ?", "Zagreb"),
        ("Quelle est la capitale du Guatemala ?", "Guatemala"),
        ("Quelle est la capitale de la Lettonie ?", "Riga"),
        ("Quelle est la capitale de la Bolivie ?", "La Paz"),
        ("Quelle est la capitale de la Slovénie ?", "Ljubljana"),
        ("Quelle est la capitale du Liban ?", "Beyrouth"),
        ("Quelle est la capitale du Paraguay ?", "Asunción")
    ]

    QuestionsImpo = [
        ("Quelle est la capitale du Bhoutan ?", "Thimphou"),
        ("Quelle est la capitale du Lesotho ?", "Maseru"),
        ("Quelle est la capitale du Tadjikistan ?", "Douchanbé"),
        ("Quelle est la capitale de la Mongolie ?", "Oulan-Bator"),
        ("Quelle est la capitale du Suriname ?", "Paramaribo"),
        ("Quelle est la capitale de la Sierra Leone ?", "Freetown"),
        ("Quelle est la capitale du Kirghizistan ?", "Bichkek"),
        ("Quelle est la capitale de la Mauritanie ?", "Nouakchott"),
        ("Quelle est la capitale du Malawi ?", "Lilongwe"),
        ("Quelle est la capitale du Nauru ?", "Yaren")
    ]

    points=0
    compteur=0
    nbquestions=0
    difficulte = 0
    
    print("C'est parti ! Choississez la difficulté en tapant le nombre associé:"
          "\n1. Facile"
          "\n2. Moyen"
          "\n3. Difficile"
          "\n4. Impossible"
          "\n5. Tout mélangé!")
    while difficulte <= 0 or difficulte > 5:
        print("Appuyez sur 1,2,3,4 ou 5")
        difficulte = int(input("Votre choix: "))
    if difficulte == 1:
        Questions = QuestionsFacile
    elif difficulte == 2:
        Questions = QuestionsMoyen
    elif difficulte == 3:
        Questions = QuestionsDures
    elif difficulte == 4:
        Questions = QuestionsImpo
    elif difficulte == 5:
        Questions = QuestionsFacile + QuestionsMoyen + QuestionsDures + QuestionsImpo

    print("Combien de questions voulez-vous ? (10 maximum)")
    nbquestions = int(input("Votre choix : "))
    while nbquestions > 10 or nbquestions < 1:
        print("Le nombre de questions doit être compris entre 1 et 10")
        nbquestions = int(input("Votre choix : "))

    print("Chaque question doit être répondue en 10 secondes. Bonne chance !")
    while compteur < nbquestions:
        compteur += 1
        x = random.randint(0, len(Questions) - 1)

        print(Questions[x][0])

        start_time = time.time()
        reponse = input("Votre réponse (10 secondes) : ")
        end_time = time.time()

        # Check if response was given in time
        if end_time - start_time < 10:
            if reponse == Questions[x][1]:
                points += 1
                print("Bonne réponse")
            else:
                print("Mauvaise réponse!")
        else:
            print("Temps écoulé !")

        del Questions[x]

    print("Vous avez eu " + str(points) + " bonnes réponses !")
    
GrandQuiz()
