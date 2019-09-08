# La Data Science avec Python

Tuto openclassrooms : https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science

## Jupyter Notebook

## NumPy

- NumPy signifie **Numerical Python**
- ensemble de fonctions très performantes (écrit en C) pour manipuler les tableaux
- utilisé dans tous les projets de calculs numériques
- structure de données principale : **ndarray** pour **N-dimensional array** : tableau à une dimension (vecteur), tableau à 2 dimensions, à 3 dimensions...
- ndarray se manipule comme les listes mais ne peut contenir qu'un seul type de données.

### Création d'un ndarray

- les ndarrays sont modifiables
- `numpy.array(liste)` permet de créer un tableau

```py
import numpy

# tableau à une dimension
tableau = numpy.array([1, 2, 3])
print(tableau) # [1 2 3]
print(type(tableau)) # <class 'numpy.ndarray'>

# tableau à deux dimensions : le 1er sous-tableau correspond à la 1ere ligne, le 2ème à la 2ème ligne...
tableau2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(tableau2)
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
print(type(tableau2))  # <class 'numpy.ndarray'>
```

### Notion de vue et de copie d'un tableau

- il est possible d'extraire un sous-ensemble d'un tableau, sans le copier, ce qui fait que lorsqu'on modifie une valeur de ce sous-tableau, cela modifie également le tableau d'origine
- il est possible de faire la même chose sous forme de copie pour ne pas modifier le tableau d'origine lorsqu'on modifie le sous-tableau

```py
tableau = numpy.array([1, 2, 3, 4, 5])
tab2 = tableau[0:2]
print(tab2) # [1 2]
tab2[0]=5
print(tab2) # [5 2]
print(tableau) # [5 2 3 4 5]

tableau = numpy.array([1, 2, 3, 4, 5])
tab2 = tableau[0:2].copy()
print(tab2) # [1 2]
tab2[0]=5
print(tab2) # [5 2]
print(tableau) # [1 2 3 4 5]
```

### Accéder aux éléments d'un tableau

- pour les tableaux unidimentionnels, le fonctionnement est le même que pour les listes
- pour les tableaux bidimensionnels, la logique reste la même

```py
tableau2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# afficher l'élément sur la 2e ligne et la 3e colonne
print(tableau2[1,2]) # 6
print(tableau2[1,-1]) # 6
# afficher la première ligne
print(tableau2[0,:]) # [1 2 3]
# afficher la première colonne
print(tableau2[:,0]) # [1 4 7]
# afficher la première ligne, et les deux premières colonnes
print(tableau2[0,0:2]) # [1 2]
```

### Explorer et filtrer un tableau bidimensionnel

```py
# création d'un tableau de 3 lignes et 2 colonnes avec des entiers aléatoires entre 0 et 100
tab = numpy.random.randint(100, size=(3,2))
print(tab) #[[77 31] [47 56] [99 62]]
# remplace chaque valeur du tableau par True ou False en fonction de la condition
print(tab>50) # [[True False] [False True] [True True]]
# filtre le tableau en fonction de la condition
tab[tab>50] # array([77, 56, 99, 62])
tab[(tab>=50) & (tab<=70)] # array([56, 62])
tab[(tab>80) | (tab <30)] # array([99])
```


### Concaténation de tableaux

- il est possible de concaténer N tableaux avec la fonction `concatenate()` lorsque les tableaux ont la même taille :

```py
tab1 = numpy.array([[1, 2], [3, 4]])
tab2 = numpy.array([[5, 6], [7, 8]])
tabConc = numpy.concatenate([tab1, tab2])
print(tabConc) # [[1 2] [3 4] [5 6] [7 8]]
```

- il est possible de faire un empilement vertical ou horizontal avec `vstack()` et `hstack()` :

```py
tab3 = numpy.array([5, 6])
tabV = numpy.vstack([tab1, tab3])
print(tabV) # [[1 2] [3 4] [5 6]]

tab4 = numpy.array([[7],[8]])
tabH = numpy.hstack([tab1, tab4])
print(tabH) # [[1 2 7] [3 4 8]]
```

### Split de tableaux

il est possible de couper un tableau grâce à fonctions :
- `numpy.split()`
- `numpy.vsplit()` et `numpy.hsplit()` qui ne fonctionnent que pour les tableaux à 2 dimensions

```py
tab = numpy.array([2,4,6,8,10,12])
tabSplit = numpy.split(tab,[2,3])
print(tabSplit) # [array([2, 4]), array([6]), array([ 8, 10, 12])]
# ​même chose en spécifiant les tableaux splités
tabS1,tabS2, tabS3 = numpy.split(tab,[2,3])
print(tabS1, tabS2, tabS3) # [2 4] [6] [ 8 10 12]

tableau = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
tableauV1, tableauV2 = numpy.vsplit(tableau, [2])
print(tableauV1) # [[1 2 3] [4 5 6]]
print(tableauV2) # [[7 8 9]]

tableauH1, tableauH2 = numpy.hsplit(tableau, [1])
print(tableauH1) # [[1] [4] [7]]
print(tableauH2) # [[2 3] [5 6] [8 9]]
```

### Calculs sur les tableaux

```py
tab = numpy.random.randint(100, size=(10,8))
print(tab)
# [[85 87 48 68 65 91 19 91]
# [ 5 90 79 75 38 71 80 62]
# [82 66  9  5 87 79 98  2]
# [25 44 23 94 23 88 91 13]
# [86 41 12 79 63 65 77 35]
# [23 25 87 87 14 89  5 82]
# [ 2 28 94  3 63 67 52 78]
# [47 24 63 13  4 77 40 17]
# [70 94 39 89 23 93 26 94]
# [58 30 83 43 16 73 82 21]]

# ajouter une valeur à tous les éléments d'un tableau
tab2 = tab+2
print(tab2)
print(tab*3)
# faire une opération sur une ligne ou colonne particulière, par exemple sur la première colonne
print(tab[:,0] / 10) # [8.5 0.5 8.2 2.5 8.6 2.3 0.2 4.7 7.  5.8]

# utilisation des fonctions propres à Numpy
numpy.add(tab, 2)
numpy.subtract(tab, 5)
numpy.multiply(tab, 3)
numpy.divide(tab, 6)

# calcul de la somme
numpy.sum(tab) # 4300
# calcul de la moyenne en utilisant la fonction de numpy
numpy.mean(tab) # 53.75
# calcul de la moyenne en utilisant la méthode de ndarray
tab.mean()
tab.min()
tab.max()
tab.sum()
tab.std()
# calcul de la moyenne par colonne
numpy.mean(tab, axis=0)
# calcul de la moyenne par ligne
numpy.mean(tab, axis=1)
```

### Lecture d'un fichier CSV

```py
# lecture d'un fichier texte
tab = numpy.genfromtxt("fichier.csv", delimiter=",", dtype=int)
print(tab) # [[ 30 183  65] [ 28 157  43] [  1  80  10]]

# mise à jour de la première colonne
tab[:,0] = tab[:,0] + 2
print(tab) # [[ 32 183  65] [ 30 157  43] [  3  80  10]]
# mise à jour de la deuxième colonne jusqu'à la dernière
tab[:,1:] = tab[:,1:] * 1.2
tab # array([[ 32, 219,  78], [ 30, 188,  51], [  3,  96,  12]])

# nombre de lignes
len(tab) # 3
# nombre de colonnes dans la première ligne
len(tab[0])
# nombre de lignes dont la 3e colonne est supérieure à 50
len(tab[tab[:,2]>50]) # 2
# somme de la première colonne
numpy.sum(tab[:,0]) # 65
tab[:,0].sum() # 65
```


## Pandas

- amène une structure de données : le **Dataframe**
- correspond à un tableau de type Excel
- possibilité d'avoir des noms de colonnes et de lignes
- possibilité de mélanger les types de données
- créé pour le langage R, puis adapté dans Python dans la bibliothèque Pandas
- possibilité de créer un dataframe depuis un fichier, un dictionnaire, une liste, ou encore un ndarray numpy

### Les séries avec Pandas

une série est un objet unidimensionnel
- variables quantitatives
- variables qualitatives

```py
import pandas

serie = pandas.Series([29, 31, 1, 40, 24, 60, 54])
print(type(serie)) # <class 'pandas.core.series.Series'>
print(serie)
# 0    29
# 1    31
# 2     1
# 3    40
# 4    24
# 5    60
# 6    54
# dtype: int64

serie = pandas.Series([29, 31, 1, 29, 24, 60, 54], index=["Florine", "Gaëtan", "Louis", "Kévin", "Thibaut", "Papa", "Maman"])
print(serie)
# Florine    29
# Gaëtan     31
# Louis       1
# Kévin      29
# Thibaut    24
# Papa       60
# Maman      54
# dtype: int64
print(serie["Louis"]) # 1
print(serie[2]) # 1
print(serie[["Florine","Louis"]])
# Florine    29
# Louis       1
# dtype: int64
print(serie[serie>35])
# Papa     60
# Maman    54
# dtype: int64

# obtenir des informations sur la distribution de la série
serie.describe() # donne des informations, sur la distribution de la série (moyenne, écart-type, nombre d'éléments...)
serie.sum()
```

### Les dataframes avec Pandas

Création d'un dataframe à partir d'une liste et d'un dictionnaire

```py
personnes = [('Gaëtan', 'Varlet', 1988), ('Florine', 'Greciet', 1990)]
labels = ['Prénom', 'Nom', 'Année de naissance']
df1 = pandas.DataFrame.from_records(personnes, columns=labels)
print(type(df1)) # <class 'pandas.core.frame.DataFrame'>
print(df1)
#     Prénom      Nom  Année de naissance
# 0   Gaëtan   Varlet                1988
# 1  Florine  Greciet                1990

personnes2 = [{'Prénom':'Gaëtan', 'Nom':'Varlet', 'Année de naissance':1988},{'Prénom':'Louis', 'Nom':'Varlet', 'Année de naissance':2018}]
df2 = pandas.DataFrame(personnes2)
print(df2)
#    Année de naissance     Nom  Prénom
# 0                1988  Varlet  Gaëtan
# 1                2018  Varlet   Louis
```

Création d'un dataframe à partir d'un tableau Numpy

```py
tableau = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
dataframe = pandas.DataFrame(tableau, columns=["col 1", "col 2", "col 3"])
print(dataframe)
#    col 1  col 2  col 3
# 0      1      2      3
# 1      4      5      6
# 2      7      8      9
```

Création d'un dataframe à partir de séries Pandas

```py
serie1 = pandas.Series([29, 31, 1, 29, 24, 60, 54], index=["Florine", "Gaëtan", "Louis", "Kévin", "Thibaut", "Papa", "Maman"])
serie2 = pandas.Series([30, 32, 2, 32], index=["Florine", "Gaëtan", "Louis", "Aurélien"])
df = pandas.DataFrame({"Groupe 1" : serie1, "Groupe 2" : serie2})
print(df)
#           Groupe 1  Groupe 2
# Aurélien       NaN      32.0
# Florine       29.0      30.0
# Gaëtan        31.0      32.0
# Kévin         29.0       NaN
# Louis          1.0       2.0
# Maman         54.0       NaN
# Papa          60.0       NaN
# Thibaut       24.0       NaN
```

### Lire et écrire un fichier

- pour lire un fichier texte, on peut utiliser les méthodes `read_table()` ou `read_csv()`
- pour écrire un dataframe dans un fichier, il faut utiliser la méthode `to_csv()`
- il existe des méthodes `read_excel()` et `to_excel()` pour travailler avec les fichiers Excel

```py
# récupération d'un jeu de données sur https://www.kaggle.com/
df = pandas.read_table("nom_fichier", sep=",")
df = pandas.read_csv("nom_fichier")
# écriture du dataframe dans un fichier CSV
df.to_csv("nom_fichier.csv", index=False)
```

fichier source :

```
prenom, age, taille, poids
gaetan, 30, 183, 65
florine, 28, 157, 43
louis, 1, 80, 10
```

```py
df = pandas.read_csv("dataframe.csv")
#     prenom   age   taille   poids
# 0   gaetan    30      183      65
# 1  florine    28      157      43
# 2    louis     1       80      10
```

### Accéder aux éléments d'un dataframe

- il est possible de remplacer l'index des lignes (1, 2, 3...) par une colonne. Cela va permettre de sélectionner une ligne par son index via la valeur de cette colonne

```py
# il faut assigner le résultat à une variable si on souhaite le stocker car set_index ne modifie pas le dataframe sur lequel il s'applique
df = df.set_index("prenom")
#           age   taille   poids
# prenom                        
# gaetan     30      183      65
# florine    28      157      43
# louis       1       80      10
```


### Ajouter/supprimer des colonnes d'un dataframe


### Explorer un dataframe


### Filtrer un Dataframe selon des conditions


### Grouper un dataframe sur une ou plusieurs colonnes (group by)



## Matplotlib et Seaborn pour visualiser les données
