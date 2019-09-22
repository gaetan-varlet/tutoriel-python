# La Data Science avec Python

Tuto openclassrooms : https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science

## Jupyter Notebook

- Jupyter Notebook est un outil très pratique qui permet d'avoir le code source et la sortie au même endroit
- pour lancer Jupyter Notebook, lancer la commande `jupyter notebook`
- un notebook est un fichier au format JSON avec l'extension `ipynb`
- un notebook contient des cellules qui peut contenir du code que l'on peut exécuter
- il est aussi possible d'écrire du markdown pour mettre en forme le notebook

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
prenom,age,taille,poids
gaetan,30,183,65
florine,28,157,43
louis,1,80,10
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

- il existe 2 méthodes pour accéder au dataframe : `iloc`, qui fonctionne avec les index des lignes et colonnes, et `loc` qui fonctionne avec les labels
- la méthode `head(n)` affiche les *n* premières lignes du tableau

```py
# afficher la 2eme ligne et la 3e colonne
df.iloc[1,2] # 43
# afficher la 3e ligne
df.iloc[2,:]
# afficher uniquement la 3e colonne pour toutes les lignes
df.iloc[:,2]
# afficher la taille de gaetan
df.loc['gaetan', 'taille']
# afficher toutes les informations sur gaetan
df.loc['gaetan',:]
# afficher toutes les tailles
df.loc[:,'taille']
# afficher les colonnes taille et poids pour tous les individus
df.loc[:,['taille', 'poids']]
df.iloc[:, [1,2]]
df.iloc[:,1:3]
# afficher les 2 premières lignes
df.iloc[0:2,:]
df.head(2)
```

### Ajouter/supprimer des colonnes d'un dataframe

```py
# création d'une colonne à partir d'autres colonnes
imc = df['poids']/(df['taille']*df['taille']/10000)
# affectation de cette colonne au dataframe
df['imc']=imc
print(df)
# suppression de cette colonne
df = df.drop(['imc'], axis=1) # axis=1 permet de dire que l'on travaille sur les colonnes
print(df)
```

### Manipuler un dataframe

```py
# connaître le nombre de lignes et de colonnes d'un dataframe
df.shape # (3, 4)
# connaître le nom des colonnes d'un dataframe
df.columns # Index(['prenom', 'age', 'taille', 'poids'], dtype='object')

# connaître le nombre de valeurs manquantes pour une colonne
df['taille'].isna() # renvoie True ou False pour chaque ligne
df['taille'].isna().sum() # renvoie 1 car il y a une valeur manquante dans la colonne taille
df.isna() # même chose pour tout le tableau
df.isna().sum() # indique pour chaque colonne le nombre de valeurs manquantes

# supprimer toutes les lignes où il y a au moins une valeur manquante
dfSansNa = df.dropna() # le tableau ne contient plusq que 2 lignes sur les 3
df.shape # (2, 4)

# trier un tableau selin une variable (de manière croissante par défaut)
df = df.sort_values(by='poids')

# obtenir le type des variables
df.dtypes
# prenom     object
# age         int64
# taille    float64
# poids       int64
# dtype: object

# obtenir des informations sur les variables numériques
df.describe()

# obtenir des infos sur toutes les variables, cela permet d'avoir quelques informations sur les variables qualitatives
df.describe(include='all')

# permet d'obtenir le nombre d'occurences de chaque modalité d'une variable qualitative
df['prenom'].value_counts()

# modifier le contenu du dataframe
# transformer les 'g' minuscules en majuscules
df['prenom'] = df['prenom'].apply(lambda x: x.replace('g', 'G'))
# transformer une variable int en chaîne de caractères
df['taille'] = df['taille'].apply(lambda x: str(x))
df.dtypes # permet de vérifier le type des variables
```

### Filtrer un Dataframe selon des conditions

```py
# récupérer les individus pesant plus de 40kg
df.loc[df['poids']>40,:]

# trouver le nombre de personne avec le prenom louis
len(df.loc[df['prenom']=='louis',:])

# trouver les louis qui pèsent plus de 15kg
df.loc[(df['prenom']=='louis') & (df['poids']>15)]
```

### Grouper un dataframe sur une ou plusieurs colonnes (group by)

```py
# permet d'obtenir des statistiques sur les variables quantitatives par modalité d'une variable qualitative
# on va par exemple voir la taille moyenne et le poids moyen pour les hommes et par les femmes
df2.groupby('sexe').describe()
# même chose avec 2 variables qualitatives dans le group by
df2.groupby(['sexe','prenom']).describe()
```

## Matplotlib et Seaborn pour visualiser les données

- *Matplotlib* est la bibliothèque la plus utilisée en Python pour visualiser les données
- *Seaborn* est une autre bibliothèque de visualisation de données basé sur *Matplotlib*

### Création d'un premier graphique

```py
# import du module pyplot qui suffit à faire des visualisations
import matplotlib.pyplot

# initialisation d'un graphique vide à 2 axes
pyplot.plot()
# permet de supprimer les crochets au dessus du graphique
pyplot.draw()

# création d'un graphique qui trace la courbe sans montrer les points
# les coordonnées des points sont données dans 2 tableaux pour l'axe des abcisses puis l'axe des ordonnées
pyplot.plot([1,2,3,4,5], [1,4,9,16,25])
pyplot.draw()

# affichage des points
pyplot.plot([1,2,3,4,5], [1,4,9,16,25], marker='o')

# affichage des points sans la ligne
pyplot.plot([1,2,3,4,5], [1,4,9,16,25], marker='o', linestyle='')
```

### Ajout d'un titre et de labels aux axes

```py
pyplot.plot([1,2,3,4,5], [1,4,9,16,25], marker='o', linestyle='')
pyplot.xlabel('Axe des abcisses')
pyplot.ylabel('Axe des ordonnées')
pyplot.title('Titre du graphique')
pyplot.draw()

# possibilité de déplacer les titres, par exemple pour remonter légèrement le titre
pyplot.title('Titre du graphique', y=1.05)
```

### Changez les couleurs

```py
# création d'un nuage de points avec scatter à la place de plot. Scatter crée directement un nuage de points sans tracer la courbe
# figure.figsize permet de redimensionner le graphique
pyplot.rcParams['figure.figsize']=[8,5]
pyplot.scatter([1,2,3,4,5], [1,4,9,16,25])
pyplot.draw()

# l'option c=list() permet de colorer les points différemments selon leur valeur, en utilisant les couleurs par défaut de scatter
pyplot.scatter([1,2,3,4,5], [1,4,9,16,25], c=list([1, 4, 9, 16, 25]))

# l'option c=list() permet de colorer les points différemments selon leur valeur, en utilisant l'échelle de couleur seismic (du bleu vers le rouge)

pyplot.scatter([1,2,3,4,5], [1,4,9,16,25], c=list([1, 4, 9, 16, 25]), cmap='seismic')
# colorbar() permet de mettre en légende la barre des couleurs
pyplot.colorbar()
```

### Changer la taille ou la forme des points

```py
# marker permet de changer le type de point, par exemple une croix
# s permet de changer la taille des points sur le graphique
pyplot.scatter([1,2,3,4,5], [1,4,9,16,25], marker='x', s=100)
```

### Enregistrer un graphique

```py
# savefig() permet d'enregistrer un graphique
# bbox_inches='tight' permet de réduire les blancs autour du graphique
pyplot.savefig('monGraphique2.png', bbox_inches='tight')
```

### Les différents types de graphiques

- les nuages de point : `plot()` et  `scatter()`
- les diagrammes en bâton : `bar()`
- les boîtes à moustaches : `boxplot()`
- les diagrammes circulaires : `pie()`

```py
# exemple d'un  diagramme en bâtons
pyplot.bar(['Hommes', 'Femmes'], [60, 40])
pyplot.draw()
# changement des couleurs du diagramme en bâtons
pyplot.bar(['Hommes', 'Femmes'], [60, 40], color=['blue', 'red'])
# les options pour le titre et les labels des axes sont les mêmes que pour le plot()

# exemple de boîtes à moustaches
pyplot.boxplot([1,2,3,4,5,6,7,8,9,10,16,7,8,12])
pyplot.draw()
# modification du label en dessous la boite à moustache (1 par défaut)
pyplot.boxplot([1,2,3,4,5,6,7,8,9,10,16,7,8,12])
pyplot.xticks([1], ["Ventes"])

# exemple de diagramme circulaire
pyplot.pie([60, 40], labels=['Hommes', 'Femmes'])
# l'option autopct='%1.1f%%' permet d'afficher les pourcentages sur le graphique (avec 1 chiffre après la virgule)
# l'option shadow=True permet de faire un léger effet d'ombre sur le graphique
pyplot.pie([60.11, 39.89], labels=['Hommes', 'Femmes'], autopct='%1.1f%%', shadow=True)
```

### Combiner plusieurs graphiques

`subplot()` permet de créer des sous-graphiques pour mettre plusieurs graphiques dans un seul graphique

```py
pyplot.rcParams['figure.figsize']=[6,6]
# il y a 3 paramètres pour subplot : nombre de lignes, nombre de colonnes, et l'emplacement sur lequel mettre la figure
# placement du premier graphique
pyplot.subplot(211)
pyplot.bar(achats_clients.keys(), achats_clients.values())
# placement du deuxième graphique
pyplot.subplot(212)
pyplot.pie([60.11, 39.89], labels=['Hommes', 'Femmes'], autopct='%1.1f%%', shadow=True)
pyplot.tight_layout()
pyplot.draw()
```

### Exemple Matplotlib avec un jeu de données
```py
import pandas
# lecture du fichier CSV
black_friday = pandas.read_csv('./donnees_data_science/BlackFriday.csv')
# visualisation des premières lignes
black_friday.head(10)
# analyse du type des variables, du nombre de lignes et de colonnes
black_friday.info()

# création d'un DataFrameGroupBy pour faire un graphique sur les dépenses par catégorie d'âge
age_groupes = black_friday.groupby('Age')
# création d'un dictionnaire où l'on va stocker pour chaque groupe, la somme des achats
achats_clients=dict()
# age correspond à la catégorie d'âge, group est un dataframe qui contient toutes les valeurs de la catégorie d'âge courante
for age, group in age_groupes:
    achats_clients[age]=sum(group["Purchase"])

# création d'un diagramme en bâtons pour visualiser les dépenses total par catégorie d'âge
pyplot.bar(achats_clients.keys(), achats_clients.values())
pyplot.draw()
```

### Créer des graphiques avec Seaborn

*Seaborn* est une bibliothèque basé sur *Matplotlib*, plus puissante que cette dernière

```py
# import de Seaborn
import seaborn

# création d'une boîte à moustaches horizontale
seaborn.boxplot([1,2,3,4,5,6,7,8,9,10,16,7,8,12])
# création d'une boîte à moustaches verticale
seaborn.boxplot(y=[1,2,3,4,5,6,7,8,9,10,16,7,8,12])

# création d'une boîte à moustaches à partir d'un dataframe (sur la variable des ventes)
seaborn.boxplot(y="Purchase", data=black_friday)
# même chose en faisant une boîte à moustache par sexe
seaborn.boxplot(x='Gender', y="Purchase", data=black_friday)
# possibilité d'utiliser des options de pyplot comme le titre
pyplot.title('Analyse des ventes par sexe')
pyplot.draw()


# boîte à moustaches par sexe x tranche d'âge
# une légende est ajouté pour les tranches d'âge
# les labels sont automatiquement mis par Seaborn avec le nom des colonnes
seaborn.boxplot(x='Gender', y="Purchase", data=black_friday, hue='Age')
# la légende est mal placée, il faut la déplacer pour que le graphique soit bien mis en forme
# l'option loc=2 met la légende en haut à gauche
# l'option bbox_to_anchor=(1.05,1) permet de décaler la légende
# l'option borderaxespad=0. permet de gérer de ldécalage par rapport au haut du graphique
pyplot.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
pyplot.draw()

# diagramme en bâtons pour connaître le nombre d'hommes et de femmes par catégorie d'âge
seaborn.countplot(x="Age", hue="Gender", data=black_friday)


# sample() permet de récupérer aléatoirement un sous-ensemble dans le jeu de données initial
subset = black_friday.sample(3000)
# représentation pour chaque observation par un point dans la bonne catégorie
# ça ressemble à une boîte à moustache sauf que tous les points sont tracés
seaborn.catplot(x='Age', y='Purchase', data=subset)
# l'option kind='swarm' permet de ne pas superposer les points sur le graphique
seaborn.catplot(x='Age', y='Purchase', data=subset, kind="swarm")

# coloration des points selon le sexe
seaborn.catplot(x='Age', y='Purchase', data=subset, kind="swarm", hue='Gender')

# création de subplot comme avec pyplot
pyplot.subplot(121)
seaborn.countplot(x="Age", hue="Gender", data=black_friday)
pyplot.subplot(122)
seaborn.boxplot(x='Gender', y="Purchase", data=black_friday)
pyplot.draw()
```

### Analyse d'un jeu de données avec Seaborn

```py
import seaborn
import matplotlib.pyplot
# chargement d'un jeu de données présent dans seaborn
tips = seaborn.load_dataset("tips")

# visualisation des premières lignes du jeu de données
tips.head()
# analyse rapide du jeu de données : il y a 244 lignes et 7 variables
tips.info()
# analyse de la distribution des variables
tips.describe(include='all')
# analyse de la distribution par sexe
tips.groupby('sex').describe()

# représentation du nombre d'additions payé par les hommes et par les femmes avec un diagramme en bâtons
seaborn.countplot(x="sex", data=tips)

# analyser graphiquement les relations entre les variables numériques (croisement de toutes les variables numériques)
seaborn.pairplot(tips)

# graphique représentant la distribution de la variable total_bill
# boîte à moustaches
seaborn.boxplot(y='total_bill', data=tips)
# histogramme
seaborn.distplot(tips['total_bill'])
# suppression de la courbe tracée sur l'histogramme
seaborn.distplot(tips['total_bill'], kde=False)

# analyse de la variable total_bill par sexe
# boîtes à moustaches
seaborn.boxplot(x='sex', y='total_bill', data=tips)
# diagrammmes à bâton représentant la moyenne
seaborn.barplot(x='sex', y='total_bill', data=tips)

# représenter avec un nuage de points la variable total_bill sur l'axe des abcisses et la variable tip sur l'axe des ordonnées afin de voir la corrélation entre les 2
seaborn.jointplot(x='total_bill', y='tip', data=tips)
# ajout de l'option kind='reg' pour tracer la relation linéaire entre les 2 variables
seaborn.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
```