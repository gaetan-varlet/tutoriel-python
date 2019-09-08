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
print(tabConc)
```

- il est possible de faire un empilement vertical ou horizontal avec `vstack()` et `hstack()` :

```py
tab3 = numpy.array([5, 6])
tabV = numpy.vstack([tab1, tab3])
print(tabV)
tab4 = numpy.array([[7],[8]])
tabH = numpy.hstack([tab3, tab4])
print(tabH)
```

### Split de tableaux

il est possible de couper un tableau grâce à fonctions :
- `numpy.split()`
- `numpy.vsplit()` et `numpy.hsplit()` qui ne fonctionnent que pour les tableaux à 2 dimensions

```py
tab = numpy.array([2,4,6,8,10,12])
tabSplit = numpy.split(tab,[2,3])
print(tabSplit)
tabS1,tabS2, tabS3 = numpy.split(tab,[2,3])
print(tabS1, tabS2, tabS3)

tableau = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
tableauV1, tableauV2 = numpy.vsplit(tableau, [2])
print(tableauV1)
print(tableauV2)

tableauH1, tableauH2 = numpy.hsplit(tableau, [1])
print(tableauH1)
print(tableauH2)
```

### Calculs sur les tableaux

```py
tab = numpy.random.randint(100, size=(10,8))
print(tab)
# ajouter une valeur à tous les éléments d'un tableau
tab2 = tab+2
print(tab2)
print(tab*3)
# faire une opération sur une ligne ou colonne particulière, par exemple sur la première colonne
print(tab[:,0] / 10)

# utilisation des fonctions propres à Numpy
numpy.add(tab, 2)
numpy.subtract(tab, 5)
numpy.multiply(tab, 3)
numpy.divide(tab, 6)

# calcul de la moyenne en utilisant la fonction de numpy
numpy.mean(tab)
# calcul de la moyenne en utilisant la méthode de ndarray
tab.mean()
tab.min()
tab.max()
# calcul de la moyenne par colonne
numpy.mean(tab, axis=0)
# calcul de la moyenne par ligne
numpy.mean(tab, axis=1)
```

### Lecture d'un fichier CSV

```py
# lecture d'un fichier texte
tab = numpy.genfromtxt("fichier.csv", delimiter=",", dtype=int)
print(tab)
# mise à jour de la première colonne
tab[:,0] = tab[:,0] * 0.85
# mise à jour de la deuxième colonne jusqu'à la dernière
tab[:,1:] = tab[:,1:] * 0.09
print(tab)
# nombre de lignes dans la 3e colonne est supérieure à 1000
len(tab[tab[:,2]>1000])
# somme de la première colonne
numpy.sum(tab[:,0])
```


## Pandas

- amène une structure de données : le **Dataframe**
- tableau de type Excel
- possibilité d'avoir des noms de colonnes et de lignes
- possibilité de mélanger les types de données
- créé pour le langage R, puis adapté dans Python dans la bibliothèque Pandas
- possibilité de créer un dataframe depuis un dictionnaire ou une liste

### Les séries avec Pandas


### Les dataframes avec Pandas


### Lire et écrire un fichier


### Accéder aux éléments d'un dataframe


### Ajouter/supprimer des colonnes d'un dataframe


### Explorer un dataframe


### Filtrer un Dataframe selon des conditions


### Grouper un dataframe sur une ou plusieurs colonnes (group by)



## Matplotlib et Seaborn pour visualiser les données
