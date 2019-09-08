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


### Split de tableaux


### Calculs sur les tableaux


## Pandas

## Matplotlib et Seaborn pour visualiser les données