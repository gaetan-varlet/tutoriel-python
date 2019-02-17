# demander à l'utilisateur de rentrer des films
# ajouter dans une liste
# gérer les doublons
# classer dans l'ordre alphabétique
# affichier la liste
# associer une note à chaque film

films = []
continuer = True
while continuer:
    filmAAjouter = input("Saisissez le nom d'une film : ")
    if filmAAjouter.lower() in [film[0].lower() for film in films]:
        print("le film {0} est déjà dans la liste de films".format(filmAAjouter))
    else:
        noteFilm = input("Entrez une note sur 5 pour ce film : ")
        films.append((filmAAjouter, noteFilm))
    encore = input("Voulez-vous en saisir un autre ? (y/n) ? : ")
    if(encore.lower()!='y'):
        continuer = False
films.sort()
print(films)