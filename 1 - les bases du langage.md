# Les bases du langage

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

## Les opérations

```py
1 + 2 # 3
1 - 2 # -1
3.11 + 2.08 # 5.1899999999999995 au lieu de 5.19
4.56 * 5.3 # 24.167999999999996 au lieu de 24.168
10 / 5 # 2.0
10 // 3 # 3, partie entière de la division
10 % 3 # 1, modulo : reste de la division entière
```

## Les variables

```py
nomVariable = valeur
```
- les nombres entiers (**int**) : `25`
- les nombres flottants (**float**) : `25.0`
- les chaînes de caractères (**string**), entre simples quotes, doubles quotes, ou triples doubles quotes : `"""Hello World"""`
- les booléens (**bool**) qui vaut *True* ou *False*

la fonction `type(nomVariable)` donne le type de la variable

Quelques astuces :
```py
v += 1 # est égal à var = var + 1 (incrémentation)
# il existe aussi -= *= /=
a,b = b,a # permutation
```

La fonction `print()` :
```py
a=5
print("a",a) # donne `a 5`
# les paramètes sont séparés par un espace
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

Les opérateurs de comparaison sont `< > <= >= == !=`

Les mots clés `and`, `or` et `not` permettent d'enrichir les prédicats des conditions :
```py
if var>5 and var<10:
if var==5 or var==10:
if not a==5: # équivalent à a!=5
```