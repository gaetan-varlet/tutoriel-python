# La Programmation Orientée Objet côté utilisateur

- un objet est une structure de données, comme les variables, qui peut contenir elle-même d'autres variables et fonctions. **En Python, tout est objet**
- les fonctions définies dans une classe sont appelées des méthodes. On appelle une méthode d'un objet grâce à `objet.methode()`

## Les chaînes de caractères

- `str()` permet de créer une chaîne vide
```py
chaine = str()
```
- `lower()` renvoie la chaîne en minuscules mais ne modifie pas la chaîne, de même pour `upper()` en majuscules
```py
chaine = "HELLO"
chaine2 = chaine.lower()
print(chaine) # HELLO
print(chaine2) # hello
```
- `capitalize()` met la première lettre en majuscules
```py
chaine = "bonjour tout le monde"
chaine2 = chaine.capitalize()
print(chaine) # bonjour tout le monde
print(chaine2) # Bonjour tout le monde
```
- `strip()` retire les espaces au début et à la fin de la chaîne
- `center(n)`  permet de centrer une chaîne. On lui passe en paramètre la taille de la chaîne que l'on souhaite obtenir. La méthode va ajouter alternativement un espace au début et à la fin de la chaîne, jusqu'à obtenir la longueur demandée
```py
chaine = "hello"
chaine2 = chaine.center(10)
print(chaine) # hello
print("1"+chaine2+"1") # 1  hello   1
```
- la méthode `format()` permet de mettre en forme des chaînes de caractères sans faire de concaténation
```py
# avec l'ordre des variables dans format
prenom = "Gaëtan"
nom = "Varlet"
age = 30
presentation = "Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)
print(presentation) # Je m'appelle Gaëtan Varlet et j'ai 30 ans.
```
```py
# avec le nom des variables dans format
prenom = "Gaëtan"
nom = "Varlet"
age = 30
presentation = "Je m'appelle {prenom} {nom} et j'ai {age} ans.".format(prenom=prenom, nom=nom, age=age)
print(presentation) # Je m'appelle Gaëtan Varlet et j'ai 30 ans.
```

- la concaténation de chaînes se fait avec le `+`. Il faut que les chaînes à concaténer soient de type string ou les convertir en string
```py
prenom = "Gaëtan"
age = 30
presentation = "Je m'appelle " + prenom + " et j'ai " + str(age) + " ans."
print(presentation) # Je m'appelle Gaëtan et j'ai 30 ans.
```

- la fonction `len(chaine)` retourne la longueur de la chaine
```py
chaine = "Hello"
print(len(chaine)) # 5
```

- les caractères d'une chaîne. Une chaîne de caractères est une séquence constituée de caractères, elle-même constituée de chaînes de caractères, chacune d'elles n'étant composée que d'un seul caractère.
```py
chaine = "Hello"
print(chaine[0]) # H
print(chaine[1]) # e
print(chaine[-1]) # o (dernier élément de la chaîne)
```

- parcours d'une chaîne avec une boucle while
```py
chaine = "Hello"

i = 0
while i < len(chaine):
    print(chaine[i]) # affiche 'H' puis 'e' puis 'l' puis 'l' puis 'o'
    i+=1
```

- parcours avec une boucle for
```py
chaine = "Hello"
for lettre in chaine:
    print(lettre)
```

- sélection de sous-chaîne
```py
chaine = "Hello"
debut = chaine[0:2]
fin = chaine[2:len(chaine)]
print(debut) # He
print(fin) # llo
```

- `replace()` permet de remplacer des sous-chaines dans la chaine. `find()` permet de renvoyer le premier indice d'une sous-chaine, -1 si cette dernière n'existe pas
```py
chaine = "Hello"
print(chaine.replace("l","L"))  # HeLLo
print(chaine.find("o")) # 4
```


## Les listes

Une liste est un objet capable de contenir d'autres objets de n'importe quel type. Ce sont donc des séquences, comme les chaînes de caractères, mais au lieu de contenir des caractères, elles peuvent contenir n'importe quel objet. Le type des listes est **list**.
```py
liste = list() # création d'une liste vide
print(type(liste)) # <class 'list'>
print(liste) # []
liste2 = [] # autre méthode pour créer une liste vide
```

- création d'une liste et accès aux éléments via leur indice
```py
liste = [1, "deux", ["a", "b"]]
print(liste[0]) # 1
print(liste[1]) # deux
print(liste[2]) # ['a', 'b']
# récupérer le dernier élément
print(liste[-1]) # ['a', 'b']
print(liste[len(liste) - 1]) # ['a', 'b']
```

- la fonction `len(liste)` permet de compter le nombre d'éléments d'une liste, la méthode `count(element)` compte le nombre de fois ou un élément est présent dans la liste
```py
liste = ["zero", "deux", "trois", "un", "un"]
print(len(liste)) # 5
print(liste.count("un")) # 2
```

- il est possible de remplacer un élément par un autre car les listes sont **mutables** contrairement aux string
```py
liste = [1, "deux", ["a", "b"]]
liste[1] = "nouvelle chaine"
print(liste) # [1, 'nouvelle chaine', ['a', 'b']]
```

- `append()` ajoute un élément à la fin d'une liste. Elle ne renvoie rien mais modifie la liste d'origine.
```py
liste = [1, 2, 3]
liste.append(4)
print(liste) # [1, 2, 3, 4]

liste = [1, 2, 3]
liste2 = liste.append(4)
print(liste) # [1, 2, 3, 4]
print(liste2) # None
```

- `insert(i, element)` insert un élément à l'indice i
```py
liste = [1, 2, 3]
liste2 = liste.insert(2, 'nouveau')
print(liste) # [1, 2, 'nouveau', 3]
```

- `liste1.extend(liste2)` ajoute liste2 à la fin de liste1
```py
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste1.extend(liste2) # équivalent à liste1+=(liste2)
print(liste1) # [1, 2, 3, 4, 5, 6]
```

- il est aussi possible de concaténer 2 listes avec le `+`
```py
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste = liste1 + liste2
print(liste) # [1, 2, 3, 4, 5, 6]
```

- supprimer un élément avec son indice avec la fonction `del`, ou avec la méthode `pop(indice)`
```py
texte = "toto"
del texte # supprime la variable

liste = [1, 2, 3]
del liste[1] # supprime l'élément à l'indice 1
print(liste) # [1, 3]

liste = [1, 2, 3]
print(liste.pop(1)) # 2 (retourne l'élément supprimé)
print(liste) # [1, 3]
```

- supprimer un élément avec la méthode `remove(element)`. Uniquement la première occurence est supprimée
```py
liste = ['a', 'b', 'c', 'b']
liste.remove('b')
print(liste) # ['a', 'c', 'b']
```

- parcourir les éléments d'une liste avec `for`
```py
liste = ['a', 'b', 'c']
for element in liste:
    print(element) # 'a' puis 'b' puis 'c'
```

- parcourir la liste avec la fonction `enumerate` retourne un **tuple** avec l'élément parcouru et l'indice de position de l'élément dans la liste
```py
liste = ['a', 'b', 'c']
for element in enumerate(liste):
    print(element) # (0, 'a') puis (1, 'b') puis (2, 'c')
    print(type(element)) # tuple
```
```py
liste = ['a', 'b', 'c']
for i, element in enumerate(liste):
    print(i, element) # 0, a puis 1, b puis 2, c
```
- récupérer des sous-listes se fait comme pour extraire des sous-chaînes de caractères :
```py
liste = ['a','b','c','d','e']
print(liste[0:2]) # ['a', 'b']
print(liste[:2]) # ['a', 'b']
print(liste[2:-1]) # ['c', 'd'] (à partir du troisième jusqu'à la fin sauf le dernier)
print(liste[1:]) # ['b', 'c', 'd', 'e']
print(liste[:]) # ['a', 'b', 'c', 'd', 'e']
```

- pour savoir si un élément est dans une liste, on peut utiliser le mot clé `in` :
```py
liste = ['a', 'b', 'c', 'b']
print('a' in liste) # True
print('toto' in liste) # False
```

- `sort()` permet de trier les listes (trie dans l'ordre croissant par défaut)
```py
liste1 = [0, 3, 2, 1, 4]
liste1.sort()
print(liste1) # [0, 1, 2, 3, 4]

liste1 = [0, 3, 2, 1, 4]
liste1.sort(reverse=True)
print(liste1) # [4, 3, 2, 1, 0]

liste1 = [0, 3, 2, 1, 4]
liste1.sort()
liste1.reverse()
print(liste1) # [4, 3, 2, 1, 0]
```

- `count(element)` permet de connaitre le nombre d'occurences de l'élément en paramètre
```py
liste = [1, 2, 3, 4, 3, 3]
print(liste.count(2)) # 1
print(liste.count(3)) # 3
```

- `max(liste)` et `min(liste)` renvoie le maximum et le minimum d'une liste (et plus généralement d'un itérable) :
```py
maListe = [0,3,-1,2]
print(max(maListe)) # 3
print(min(maListe)) # -1
```

- `sum(liste)` et `len(liste)` renvoie la somme des éléments d'une liste et le nombre d'éléments dans la liste
```py
liste = [1, 2, 3, 4]
print(sum(liste)) # 10
print(len(liste)) # 4
```

- `split(separateur)` est une méthode de chaîne qui permet de découper la chaîne en liste en spécifiant la chaîne séparatrice
```py
texte = "Bonjour tout le monde"
liste = texte.split(" ")
print(liste) # ['Bonjour', 'tout', 'le', 'monde']
```

- `"".join(liste)` permet de coller les éléments d'une liste en string
```py
liste = ['Bonjour', 'tout', 'le', 'monde']
print(" ".join(liste)) # Bonjour tout le monde
```


## Les compréhensions de liste

permet de filtrer ou modifier des listes
```py
liste1 = [0, 1, 2, 3, 4, 5]
liste2 = [nb * nb for nb in liste1]
print(liste2) # [0, 1, 4, 9, 16, 25]
```
```py
liste1 = [0, 1, 2, 3, 4, 5]
liste2 = [nb * nb for nb in liste1 if nb % 2 == 0] # filtrage avec un if
print(liste2) # [0, 4, 16]
```


## Les tuples

Les tuples sont des listes immuables, qu'on ne peut pas modifier. Un tuple se définit comme une liste, sauf qu'on utilise comme délimiteur des parenthèses au lieu des crochets.

```py
tupleVide = ()
# pour faire un tuple avec un seul élément, il faut ajouter une virgule sinon Python le transforme en variable 'simple'
tupleUnSeulElement = (1,) # équivalent à tupleUnSeulElement = 1,
print(tupleUnSeulElement) # (1,)
print(len(tupleUnSeulElement)) # 1
print(type(tupleUnSeulElement)) # <class 'tuple'>
monTuple = ('a', 'b', 'c') # équivalent à  monTuple = 'a', 'b', 'c'
print(monTuple) # ('a', 'b', 'c')
print(len(monTuple)) # 3
print(type(monTuple)) # <class 'tuple'>
```

Cette syntaxe passe par des tuples qui ne sont pas déclarés explicitement. Quand Python trouve plusieurs variables ou valeurs séparées par des virgules et sans délimiteur, il va les mettre dans des tuples.
```py
a, b = 3, 4 # équivalent à (a, b) = (3, 4)
a, b = b, a
print (a,b) # 4 3
```

Une fonction peut également renvoyer plusieurs variables sous forme de tuple
```py
def maFonction():
    a = 5
    b = 2
    return a, b

retour = maFonction()
print(retour) # (5, 2)
c, d = maFonction()
print(c) # 5
print(d) # 2
```

- l'étoile `*` permet dans une définition de fonction qu'un nombre de paramètres variables soient capturés dans un tuple.
```py
def maFonction(*param):
     print("Les paramètres sont : {}.".format(param))

maFonction() # Les paramètres sont : ().
maFonction("a") # Les paramètres sont : ('a',).
maFonction("a", "b") # Les paramètres sont : ('a', 'b').
```

- l'étoile permet aussi dans l'appel d'une fonction de décomposer un tuple en paramètres envoyé à la fonction
```py
monTuple = ('a', 'b', 'c')
print(monTuple) # ('a', 'b', 'c')
print(*monTuple) # a b c
```


## Les dictionnaires

Les dictionnaires sont des objets en contenant d'autres, où chaque objet est associé à une clé. Un dictionnaire n'est **pas ordonné**. La **clé est forcément unique**, mais deux valeurs peuvent être identiques. On peut mettre presque tous les types en clé et tous les types en valeur


- création d'un dictionnaire, ajout de valeurs au dictionnaire et accès à la valeur d'une clé :
```py
monDictionnaire = {} # équivalent à monDictionnaire = dict()
print(type(monDictionnaire)) # <class 'dict'>
print(monDictionnaire) # {}
monDictionnaire['maCle1'] = 'maValeur1'
monDictionnaire['maCle2'] = 'maValeur2'
print(monDictionnaire) # {'maCle1': 'maValeur1', 'maCle2': 'maValeur2'}
monDictionnaire['maCle1'] = 'maValeur3' # maj de la valeur de maCle1 car la clé exite déjà
print(monDictionnaire) # {'maCle1': 'maValeur3', 'maCle2': 'maValeur2'}
print(monDictionnaire['maCle1']) # maValeur3
print(monDictionnaire.get('maCle1')) # maValeur3, équivalent à monDictionnaire['maCle1']

monDictionnaire['lat', 'long'] = "Paris" # la clé de l'élément Paris est un tuple
print(monDictionnaire) # {('lat', 'long'): 'Paris', 'maCle2': 'maValeur2', 'maCle1': 'maValeur3'}
```
- la méthode `get(cle)` retourne la valeur associée à *cle*, `None` si la clé n'existe pas alors que `monDico[cle]` retourne une erreur si la clé n'existe pas. On peut également spécifier une valeur par défaut :
```py
print(monDictionnaire.get('maCle5', 'oupsy')) # oupsy
```

- la méthode `update` permet de mettre à jour une valeur d'un dictionnaire
```py
monDictionnaire.update({'maCle1': 'maValeur4'}) # équivalent à monDictionnaire['maCle1'] = 'maValeur4'
```

- suppression d'un élément, avec `del` comme pour les listes, ou avec la méthode de dictionnaire `pop` qui renvoie la valeur supprimée
```py
print(monDictionnaire) # {'maCle1': 'maValeur1', 'maCle2': 'maValeur2'}
del monDictionnaire['maCle1']
print(monDictionnaire) # {'maCle2': 'maValeur2'}
```
```py
print(monDictionnaire) # {'maCle1': 'maValeur1', 'maCle2': 'maValeur2'}
valSup = monDictionnaire.pop('maCle1')
print(monDictionnaire) # {'maCle2': 'maValeur2'}
print(valSup) # maValeur1
```

- vérifier si une clé est dans un dictionnaire
```py
dictionnaire = {'cle1':30, 'cle2': 40}

if 'cle1' in dictionnaire: # équivalent à dictionnaire.keys()
    print('est dans les clés')

if 30 in dictionnaire.values():
    print('est dans les valeurs')
```

- stocker des références de fonctions
```py
# création de 2 fonctions qui écrivent dans la console
def hello():
    print('Hello')
def coucou():
    print('Coucou')

mesFonctions={}
# enregistrements des fonctions dans le dictionnaire
# on ne met pas les parenthèses car on enregistre la définition de la fonction, on ne veut pas l'exécuter
mesFonctions['hello'] = hello
mesFonctions['coucou'] = coucou
# appel de la fonction et exécution de celle-ci avec les parenthèses
mesFonctions['hello']() # Hello
```

- parcourir un dictionnaire. L'ordre de parcours change car il n'y a pas d'ordre dans un dictionnaire. Utilisation des méthodes `keys()`, `values()` et `items()` :
```py
monDictionnaire = {} # équivalent à monDictionnaire = dict()
monDictionnaire['maCle1'] = 'maValeur1'
monDictionnaire['maCle2'] = 'maValeur2'
monDictionnaire['maCle3'] = 'maValeur3'

# parcours des clés du dictionnaire
for cle in monDictionnaire.keys():
    print(cle) # affiche maCle2, puis sur la ligne suivante maCle1 puis maCle3

# parcours des valeurs du dictionnaire
for valeur in monDictionnaire.values():
    print(valeur) # affiche maValeur2, puis maValeur1 puis maValeur3

# parcours des clés et des valeurs renvoyées sous forme de tuple
for cle, valeur in monDictionnaire.items():
    print("La clé {cle} contient la valeur {valeur}".format(cle=cle, valeur=valeur))
```

- récupérer les paramètres nommés d'une fonction dans un dictionnaire, avec `**`
```py
def maFonction(**parametres_nommes):
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))

maFonction() # J'ai reçu en paramètres nommés : {}.
maFonction(p=4, j=8) # J'ai reçu en paramètres nommés : {'p': 4, 'j': 8}.
```

- pour avoir une fonction qui accepte des paramètres nommés et non nommés, il faut faire comme dans l'exemple ci-dessous. Les paramètres non nommés se retrouveront dans la variable *en_liste* et les paramètres nommés dans la variable *en_dictionnaire*.
```py
def maFonction(*en_liste, **en_dictionnaire):
```


## Les Set

Un Set est un conteneur semblable aux listes, sauf qu'il ne peut contenir deux objets identiques.

```py
monSet = {"toto", "tata", "toto"} # 2 éléments sont identiques, un seul des deux sera dans le set
print(monSet) # set(['tata', 'toto'])
print(type(monSet)) # <type 'set'>
```


## Le module OS

- les méthodes `getcwd()` (CWD = « Current Working Directory ») et `chdir()` (Change Directory) du module `os` permettent de savoir dans quel répertoire on se trouve et de changer de répertoire, grâce au déplacement relatif ou absolu

```py
import os

print(os.getcwd()) # /home/gaetan/depot-github/tutoriel-python
os.chdir("./scripts")
print(os.getcwd()) # /home/gaetan/depot-github/tutoriel-python/scripts
```

- la méthode `makedirs(nomDossier)` permet de créer un dossier

```py
# exemple de création d'une structure de dossier
import os

def creer_dossiers(dossiers):
    base = os.getcwd()
    for key, values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base, key, value)
            # makedirs créer le dossier parent avant le dossier enfant s'il n'existe pas
            os.makedirs(dossier)

structure = {
    "Musique": ["Rock", "Jazz", "Pop"],
    "Documents": ["Factures", "Travail"]
}

creer_dossiers(structure)
```

## Ecriture d'un fichier en JSON

- utilisation du module **json** pour écrire le dictionnaire au format json
- la méthode `dump()` permet d'écrire le dictionnaire en paramètre dans le fichier spécifié en paramètre

```py
import os
import json

def ecrire_json(fichier_json, dictionnaire):
    with open(fichier_json, 'w') as f:
        json.dump(dictionnaire, f, indent=4)

fichier_json = os.getcwd() + "/test_json.json"
ecrire_json(fichier_json, structure)
```


## Les fichiers

- la méthode `open()` permet d'ouvrir un fichier
    - avec le nom du fichier en paramètre (absolu ou relatif)
    - et le mode d'ouverture (`r` en lecture,  `w` en écriture en écrasant le fichier, et `a` (append) en écriture en écrivant à la fin du fichier sans écraser l'ancien contenu). On peut ajouter à tous ces modes le signe `b` pour ouvrir le fichier en mode binaire
    - la méthode crée un objet de la classe `TextIoWrapper`, nous allons utiliser des méthodes de cette classe pour interagir avec le fichier
- la méthode `read()` renvoie tout le contenu du fichier, que l'on capture dans une chaîne de caractères
- la méthode `readlines()` renvoie le contenu du fichier dans une liste ou chaque ligne est un élément de la liste
- la méthode `readline()` lit le fichier ligne à ligne. A chaque fois, qu'on apelle la méthode, il renvoie la ligne suivante
- la méthode `write('chaîne a écrire')` permet d'écrire une chaîne de caractère dans le fichier. Elle retourne le nombre de caractères écrit. Si on souhaite écrire un autre type que le string, il faut les convertir en chaîne de caractères
- la méthode `close()` ferme le fichier, ce qui rendra l'accès au fichier à d'autres applications
- certains attributs permettent d'avoir des informations sur le fichier :
    - `closed` : True/False si le fichier est ouvert ou fermé
    - `mode` : 'r', 'w' ou 'a'
    - `name` : qui renvoie le chemin du fichier

exemple de lecture d'un fichier :
```py
monFichier = open('/home/gaetan/depot-github/tutoriel-python/scripts/fichierALire.txt', 'r')
contenu = monFichier.read()
print(monFichier)
# <_io.TextIOWrapper name='/home/gaetan/depot-github/tutoriel-python/scripts/fichierALire.txt' mode='r' encoding='UTF-8'>
print(contenu)
# contenu de mon fichier
# je m'appelle Gaëtan
monFichier.close()

lignes = contenu.split('\n') # découpage du fichier ligne par ligne dans un tableau
print(lignes) # ['contenu de mon fichier', "je m'appelle Gaëtan"]
```

```py
f = open('/home/gaetan/depot-github/tutoriel-python/scripts/fichierALire.txt', 'r')
line = ' '
while line:
    line = f.readline()
    print(line)
f.close()
```

exemple d'écriture dans un fichier :
```py
# Création d'un fichier fichierEcrit.txt avec comme contenu "Hello World !"
monFichier = open('/home/gaetan/depot-github/tutoriel-python/scripts/fichierEcrit.txt',  'w')
monFichier.write('Hello World !')
monFichier.close()
```

- le mot clé `with` crée un *context manager* qui vérifie que le fichier est ouvert et fermé même si des erreurs se produisent pendant le bloc. Il n'y a plus besoin d'appeler la méthode `close()`
```py
with open('/home/gaetan/depot-github/tutoriel-python/scripts/fichierALire.txt', 'r') as monFichier:
    contenu = monFichier.read()
    print(monFichier.closed) # affiche False car le fichier est encore ouvert
print(contenu) # affiche le contenu du fichier
print(monFichier.closed) # affiche True car le fichier a été fermé
```

- le module `pickle` permet d'enregistrer des objets dans un fichier en binaire, avec les classes **Pickler** pour enregistrer des objets dans un fichier et **Unpickler** pour lire des objets dans un fichier
```py
import pickle

liste = ['Paris', 'Lyon', 'Marseille']

# écriture dans le fichier fichierAvecUnObjet au format binaire (wb)
with open('/home/gaetan/depot-github/tutoriel-python/scripts/fichierAvecUnObjet', 'wb') as fichier:
    # création de l'objet Pickler en lui passant en paramètre le fichier dans lequel écrire
    pickler = pickle.Pickler(fichier)
    # la méthode dump du pickler permet d'enregistrer l'objet passé en paramètre
    pickler.dump(liste)
```

```py
import pickle

# lecture dans le fichier fichierAvecUnObjet au format binaire (rb)
with open('/home/gaetan/depot-github/tutoriel-python/scripts/fichierAvecUnObjet', 'rb') as fichier:
    # création de l'objet Unpickler en lui passant en paramètre le fichier dans lequel lire
    unpickler = pickle.Unpickler(fichier)
    # la méthode load renvoie le premier objet qui a été lu. S'il y en a plusieurs, il faut l'appeler plusieurs fois
    premierObjet = unpickler.load()
print(premierObjet) # ['Paris', 'Lyon', 'Marseille']
```


## La portée des variables

- une variable définie dans une fonction n'est pas accessible en dehors de celle-ci
- une variable définie en amont d'une fonction est accessible dans la fonction
- Python cherche d'abord dans l'espace local de la fonction, et si la variable n'existe pas, il va chercher dans l'espace local dans lequel la fonction a été appelé. A éviter, il vaut mieux passer par des variables globales
- concernant l'accès aux variables extérieures à l'espace local, Python peut les lire mais **ne peut pas les modifier par affectation**. Si on essaie de modifier une variable extérieure à l'espace local, une nouvelle variable est en fait créé dans l'espace local :
```py
toto = "azerty"

def maFonction(param1):
    toto = "qwerty"
    print(toto) # affiche qwerty
    return param1 * param1

maFonction(5)
print(toto) # affiche azerty
```
- en revanche, il est possible de modifier un objet en appelant une méthode de celui-ci :
```py
maListe = ['a','b','c']

def ajouterElement(element):
    maListe.append(element)

print(maListe) # ['a', 'b', 'c']
ajouterElement('d')
print(maListe) # ['a', 'b', 'c', 'd']
```

## Les références d'objets

- une variable est un nom identifiant pointant vers une référence d'un objet, qui est en quelque sorte sa position en mémoire. **Deux variables peuvent donc pointer sur un même objet**
- la fonction `id(objet)` renvoie la position de l'objet dans la mémoire Python sous la forme d'un entier
- le mot clé `is` compare les id des objets alors que `==` compare le contenu des objets
```py
maListe = [1, 2, 3]
maListe2 = maListe
maListe2.append(4)
print(maListe) # [1, 2, 3, 4]
print(maListe2) # [1, 2, 3, 4]
print(id(maListe)) # 140574641334408
print(id(maListe2)) # 140574641334408
print(maListe == maListe2) # True
print(maListe is maListe2) # True
```
*maListe* et *maListe2* contiennent une référence vers le même objet : si on modifie l'objet depuis une des deux variables, le changement sera visible depuis les deux variables.

- pour créer une variable qui ne pointe pas vers le même objet, le plus simple est de passer par le constructeur :
```py
maListe = [1, 2, 3]
maListe2 = list(maListe)
print(maListe == maListe2) # True
print(maListe is maListe2) # False
maListe2.append(4)
print(maListe) # [1, 2, 3]
print(maListe2) # [1, 2, 3, 4]
```

- cela ne fonctionne pas avec les entiers, les flottants, les chaînes de caractères. Ils n'ont aucune méthode travaillant sur l'objet lui-même. Les chaînes de caractères ne modifient pas l'objet mais renvoie un nouvel objet modifié


## Les variables globales
- les variables globales permettent de modifier par affectation des variables définies en dehors de l'espace local
- en précisant `global` devant une variable, Python permet l'accès en lecture et en écriture à cette variable, ce qui signifie qu'on  peut changer sa valeur par affectation
```py
toto = "azerty"

def maFonction(param1):
    global toto # Python recherche totos en dehors de l'espace local de la fonction
    toto = "qwerty"
    print(toto) # affiche qwerty
    return param1 * param1

maFonction(5)
print(toto) # affiche qwerty
```
