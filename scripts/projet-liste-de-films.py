# demander à l'utilisateur de rentrer des films
# ajouter dans une liste
# gérer les doublons
# classer dans l'ordre alphabétique
# affichier la liste

films = []
continuer = True
while continuer:
    filmAAjouter = input("Saisissez le nom d'une film : ")
    if filmAAjouter.lower() in [film.lower() for film in films]:
        print("le film {0} est déjà dans la liste de films".format(filmAAjouter))
    else:
        films.append(filmAAjouter)
    encore = input("Voulez-vous en saisir un autre ? (y/n) ? : ")
    if(encore.lower()!='y'):
        continuer = False
films.sort()
print(films)