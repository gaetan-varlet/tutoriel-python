# Premiers pas en Python

## Lancer Python sous Linux

```bash
python # ouvre l'interpréteur Python 2
python3 # Python 3 (première version sortie en 2009)
# `Ctrl + D` permet de fermer la ligne de commande Python
```

```bash
python monScript.py # exécute le script en python 2
python3 monScript.py # exécute le script en python 3
```

## Exécuter un script sous windows

ouvrir un script avec **IDLE** et faire `run` ou `F5`

----

## Les différences Python2 vs Python3

- **l'encodage** : en Python2, pour écrire des caractères accentués, il faut ajouter sur la première ligne du script la commande suivante, ce qui n'est pas nécessaire en Python3
```py
# -*- coding: utf-8 -*-
print('Hello')
```
- **la division de nombres entiers**
```py
5/2 = 2 # python2
5/2 = 2.5 # python3
```
- **la fonction input()** interprète le contenu saisie de l'utilisateur et renvoi le type correspondant en Python2, par exemple `int` alors qu'en Python3, elle retourne toujours un string
```py
python2 = input("Veuillez saisir un nombre : ") # 3, la variable sera un int
python3 = input("Veuillez saisir un nombre : ") # 3, la variable sera un string
```

## Les opérations

```py
1 + 2 # 3
1 - 2 # -1
3.11 + 2.08 # 5.1899999999999995 au lieu de 5.19
4.56 * 5.3 # 24.167999999999996 au lieu de 24.168
10 / 5 # 2.0
10 // 3 # 3, partie entière de la division
10 % 3 # 1, modulo : reste de la division entière
5 ** 2 # 25, puissance
```

## Les variables

```py
nomVariable = valeur
```
- les nombres entiers (**int**) : `25`
- les nombres flottants (**float**) : `25.0`
- les chaînes de caractères (**string**), entre simples quotes, doubles quotes, ou triples doubles quotes : `"""Hello World"""`
- les booléens (**bool**) qui vallent *True* ou *False*

Quelques astuces :
```py
v += 1 # est égal à var = var + 1 (incrémentation)
# il existe aussi -= *= /=
a,b = b,a # permutation
```

## Quelques fonctions utiles

La fonction `print()` :
```py
 # en utilisant la virgule comme séparateur, les paramètres sont séparés par un espace
a = 5
print("a",a) # donne `a 5`

# la concaténation (avec le +) ne fonctionne qu'avec des variables de type string et n'ajoute pas d'espace
b='6'
print("b"+b) # donne b6
```

la fonction `type(nomVariable)` donne le type de la variable.  
La fonction `input()` permet de récupérer la saisie de l'utilisateur au format string.  
Le fonction `int(texte)` permet de convertir une donnée en entier.  
Le fonction `float(texte)` permet de convertir une donnée en float.  
Le fonction `str(texte)` permet de convertir une donnée en string.  
```py
texte = input("Veuillez saisir un nombre : ") # 2019
type(texte) # str
annee = int(texte)
type(annee) # int
```
La fonction `randint(a,b)` de la librairie `random` permet de générer un nombre entier aléatoire entre a et b inclus
```py
import random
nombreAleatoire = random.randint(1,5)
print(nombreAleatoire) # 1, 2, 3, 4 ou 5


from random import randint
nombreAleatoire = randint(1,5)
print(nombreAleatoire)
```

La fonction `isinstance(var, nomClasse)` permet de savoir si un objet est une instance d'une classe ou d'une de ses classes filles
```py
a = 'toto'
print(isinstance(a, object))  # True
print(isinstance(a, str))  # True
print(isinstance(a, int))  #  False
b = [1, 2, 3]
print(isinstance(b, list))  # True
```

La fonction `issubclass(var, nomClasse)` permet de savoir si une classe est sous-classe d'une autre
```py
print(issubclass(str, object))  # True
print(issubclass(object, str))  # False
```

## Les conditions

```py
if nb > 0:
    print("nb est positif")
elif nb < 0:
    print("nb est négatif")
else:
    print("nb est nul")
```

Les opérateurs de comparaison sont :
- `<`
- `>`
- `<=`
- `>=`
- `==`
- `!=`

Les mots clés `and`, `or` et `not` permettent d'enrichir les prédicats des conditions. Il est possible d'utiliser des parenthèses pour définir de manière précises les priorités.
`not` est plus fort que `and` qui lui-même est plus fort que `or`. On peut mettre des parenthèses pour changer cet ordre naturel.
```py
if var>5 and var<10:
if var==5 or var==10:
if not a==5: # équivalent à a!=5
True and False or True # True car (False or True)
False and (False or True)  # False car (False and True)
```
Le mot clé `is` teste l'égalité de la référence d'une valeur
```py
homme = True
if homme is not True:
    print('Vous êtes une femme')
else:
    print('Vous êtes un homme')
```

## Les boucles


### La boucle while
```py
while condition:
    # instruction 1
    # instruction 2
```

exemple :
```py
i = 0
while i<10:
    print("tour de boucle",i) # affiche de 0 à 9
    i+=1
```


### La boucle for

elle permet de parcourir des séquences de plusieurs données
```py
for element in sequence:
```

exemple qui affiche `H` puis `e` puis `l` puis `l` et `o`
```py
chaine = "Hello"
for lettre in chaine:
    print(lettre)
```
Il est possible d'utiliser `in` dans une condition. Autre exemple qui affiche `* e * * o`
```py
chaine = "Hello"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else:
        print("*")
```

exemple en itérant de i allant de 1 à 5
```py
for i in range(1, 6):
  print(i) # affiche i de 1 à 5
```
- `range(n)` crée un tableau de n éléments allant de 0 à n-1
- si on lui passe 2 paramètres, on lui dit à quel chiffre commencer au lieu de 0 : `range(1, 6)`
- on peut lui passer un troisième paramètre qui est le pas : `range(0,7,2)` va avoir comme valeur 0, 2, 4 et 6

### Les mots-clés break et continue

- **break** permet d'interrompre une boucle
- **continue** permet de passer au tour de boucle suivant sans terminer le tour de boucle en cours

exemples :
```py
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break
```

## Les fonctions

```py
def nomDeLaFonction(parametre1, parametre2, parametre3, parametreN): # def pour define
    # Bloc d'instructions

nomDeLaFonction('toto', 'tata') # appel de la fonction
```

- on peut mettre des valeurs par défaut
- on peut appeler une fonction en nommant les paramètres, ce qui est utile quand plusieurs ont une valeur par défaut
```py
def fonc(a=1, b=2, c=3, d=4, e=5):

fonc(b=8, d=5) # a = 1, b = 8, c = 3, d = 5, e = 5
```
- on peut créer une documentation à la fonction appelée **docstring** entre triple guillemets que l'on retrouve avec la commande `help(nom_de_la_fonction)`
```py
def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    
    (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
```

- en Python, la signature d'une fonction est tout simplement son nom. Cela signifie qu'on ne peut définir deux fonctions du même nom (l'ancienne définition serait écrasée par la nouvelle)
- certaines fonctions ne renvoient rien. Si on veut retourner une valeur, il faut utiliser le mot clé **return**. Cette instruction arrête le déroulement de la fonction, le code situé après le `return` ne s'exécutera pas
```py
def carre(valeur):
    return valeur * valeur

variable = carre(5) # contient 25
```

## Les fonctions lambda

```py
lambda arg1, arg2,… : instruction de retour
```
Il faut stocker la fonction lambda dans une variable pour pouvoir l'appeler
```py
carre = lambda x: x * x

variable = carre(5) # contient 25
```
```py
somme = lambda x, y: x + y

var = somme(5,2) # contient 7
```

## Les modules

Un module est un bout de code dans un fichier contenant des fonctions et variables. Pour l'utiliser, il faut l'**importer**. Il y a plein de modules disponibles avec Python sans qu'il soit nécessaire d'installer des bibliothèques supplémentaires.
```py
import math # importation du module math
import os

# __file__ permet de savoir où se trouve le fichier
print(os.__file__)  #  /usr/lib/python3.8/os.py

math.sqrt(16) # appel d'une fonction du module nomDuModule.nomFonction

help(math) # renvoie la documentation du module math
help(math.sqrt) # renvoie la documentation de la fonction sqrt
```

Il est possible de changer l'espace de nom du module importé :
```py
import math as mathematiques
mathematiques.sqrt(25)
```

Il est aussi possible de n'importer qu'une fonction d'un module au lieu de tout le module complet
```py
from math import fabs
res = fabs(-5) # retourne la valeur absolue 5
```
Il n'est plus nécessaire de préfixer avec `math.`, la méthode est chargé par **from** dans l'interpréteur au même niveau que les fonctions existantes comme *print*.
```py
from math import * # importe toutes les fonctions dans l'espace de nom principal
```

## Créer des modules et les utiliser

```py
# module calculs.py
carre = lambda x: x * x
```
```py
# fichier test.py dans le même répertoire que calculs.py
import calculs
res = calculs.carre(5) # contient 25
```

## Tester le module

il est possible de tester le module dans le module lui-même sans que ce test ne s'exécute quand le module est appelé dans un autre fichier. Dans l'exemple ci-dessous, le test ne s'exécutera que si le module *calculs.py* est exécuté directement.
```py
# module calculs.py
carre = lambda x: x * x

# test de la fonction carre
if __name__ == "__main__":
    a = carre(4)
    print(a)
```
La variable **__name__** est une variable de l'interpréteur. Si elle vaut **__main__**, cela signifie que le fichier appelé est lancé directement comme exécutable. Si elle vaut autre chose, le fichier est appelé comme module d'un autre fichier.

## Les packages

On peut regrouper des modules dans des packages, qui sont des répertoires qui contiennent d'autres répertoires (packages) ou des fichiers (modules)

Exemple où l'on crée un package **monPackage** dans lequel on place **calculs.py**. Au même niveau que le package, on a **test.py** qui va appeler la méthode *carre* de *calculs.py*
```py
# fichier test.py
import monPackage.calculs
res = monPackage.calculs.carre(5) # contient 25
```

```py
# autre possibilité
from monPackage import calculs
res = calculs.carre(5) # contient 25
```

```py
## troisième possibilité
from monPackage.calculs import carre
res = carre(5) # contient 25
```

## Les exceptions

Une exception est une erreur que peut rencontrer Python en exécutant le programme. La gestion des exceptions permet de récupèrer l'erreur pour éviter l'arrêt du programme.

```py
File "test.py", line 1, in <module>
    from monPackage import carre
ImportError: cannot import name 'carre'
```
L'interpréteur précise le type d'erreur (`ImportError`), un message permettant de comprendre l'erreur qui vient de se produire (`cannot import name 'carre'`) et la ligne concernée par l'erreur (ligne 1 du module `carre`)

Syntaxe minimaliste :
```py
try:
    # Bloc à essayer
except:
    # Bloc qui sera exécuté en cas d'erreur
```

- il est possible d'exécuter le bloc except pour un type d'exception précis, de les enchainer
- il est possible de récupérer le message d'erreur renvoyé par l'exception pour l'afficher
- le mot-clé **else** va permettre d'exécuter une action si aucune erreur ne survient dans le bloc. Il est possible de s'en passer et de mettre le contenu du else dans le bloc try directement
- le mot-clé **finally** permet d'exécuter du code après un bloc try, quel que soit le résultat de l'exécution du dit bloc
```py
try:
    resultat = numerateur / denominateur
except NameError as exception_retournee:
    print("Voici l'erreur :", exception_retournee) # correspond au message renvoyé par l'exception
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)
finally:
    # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
    print("coucou")
```

Le mot-clé **pass** permet de ne rien faire dans le bloc *except*. En effet, on est obligé de mettre un bloc catch après le bloc try.
```py
try:
    a = 5/0
except: # Rien ne doit se passer en cas d'erreur
    pass

print('hello')
```
`pass` n'est pas un mot-clé propre aux exceptions : on le trouve aussi dans des conditions ou dans des fonctions que l'on souhaite laisser vide

## Les assertions

Les assertions permettent de faire des vérications, généralement dans un bloc try...except. Le mot-clé **assert** teste la condition. S'il renvoie `True`, l'exécution se poursuit normalement, sinon une **AssertionError** est levée :
```py
annee = input("Saisissez une année supérieure à 0 :\n")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
```

## Lever une exception

**raise** permet de lever une exception

exemple ou on lève une exception de type `ValueError` si l'utilisateur saisit une année négative ou nulle :
```py
annee = input() # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
```

Dans cette exemple, l'erreur est interceptée immédiatement ce qui limite l'intérêt, mais il sera possible de l'intercepter à d'autres niveaux si on le souhaite.
