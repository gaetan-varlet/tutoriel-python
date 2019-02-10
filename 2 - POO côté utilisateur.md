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

- création d'une liste et accès aux éléments
```py
liste = [1, "deux", ["a", "b"]]
print(liste[0]) # 1
print(liste[1]) # deux
print(liste[2]) # ['a', 'b']
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

- supprimer un élément avec son indice avec `del`
```py
texte = "toto"
del texte # supprime la variable

liste = [1, 2, 3]
del liste[1] # supprime l'élément à l'indice 1
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


## Les tuples

Les tuples sont des listes immuables, qu'on ne peut modifier. Un tuple se définit comme une liste, sauf qu'on utilise comme délimiteur des parenthèses au lieu des crochets.

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

- l'étoile `*` permet dans une définition de fonction qu'un nombre de paramètres variables soient capturés dans un tuple.
```py
def maFonction(*param):
     print("Les paramètres sont : {}.".format(param))

maFonction() # maFonction("a", "b")
maFonction("a") # Les paramètres sont : ('a',).
maFonction("a", "b") # Les paramètres sont : ('a', 'b').
```

- l'étoile permet aussi dans l'appel d'une fonction de décomposer un tuple en paramètres envoyé à la fonction
```py
monTuple = ('a', 'b', 'c')
print(monTuple) # ('a', 'b', 'c')
print(*monTuple) # a b c
```

- `sort()` permet de trier les listes
```py
liste1 = [0, 3, 2, 1, 4]
liste1.sort()
print(liste1) # [0, 1, 2, 3, 4]
liste1.sort(reverse=True)
print(liste1) # [4, 3, 2, 1, 0]
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


## Les dictionnaires

Les dictionnaires sont des objets en contenant d'autres, où chaque objet est associé à une clé. Un dictionnaire n'est pas ordonné.

- création d'un dictionnaire
```py
monDictionnaire = {} # monDictionnaire = dict()
print(type(monDictionnaire)) # <class 'dict'>
print(monDictionnaire) # {}
```

- ajouter des valeurs au dictionnaire et accès à la valeur d'une clé
```py
monDictionnaire = {} # monDictionnaire = dict()
monDictionnaire['maCle1'] = 'maValeur1'
monDictionnaire['maCle2'] = 'maValeur2'
print(monDictionnaire) # {'maCle1': 'maValeur1', 'maCle2': 'maValeur2'}
monDictionnaire['maCle1'] = 'maValeur3' # maj de la valeur de maCle1
print(monDictionnaire) # {'maCle1': 'maValeur3', 'maCle2': 'maValeur2'}
print(monDictionnaire['maCle1']) # maValeur3
```

