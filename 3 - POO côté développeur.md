# la Programmation Orientée Objet côté développeur

## La notion de classe

Une classe est un modèle suivant lequel on va créer des objets. Dans la classe seront définis les attributs et les méthodes.
- Python a définit certaines classes : les nombres, les chaînes, les listes... Il est également possible d'en créer d'autres avec le mot clé `class`
- il faut définir le constructeur avec `def __init__(self)`, *self* étant l'objet en train de se créer. Il est possible de passer d'autres paramètres pour remplir les attributs de l'objet
- on instancie un objet de la classe en appelant le constructeur
- on peut modifier la valeur d'un attribut en faisant `monObjet.attribut = nouvelleValeur`
- il est possible de créer des attributs de classe. Cet attribut n'appartient pas à l'objet mais est partagé entre tous les objets de cette classe. Il se déclare avant le constructeur, et son accès se fait sous la forme `NomClasse.nomAttributClasse`

```py
class Person:
    personnesCrees = 0
    def __init__(self, nom, prenom):
        Person.personnesCrees += 1
        self.nom = nom
        self.prenom = prenom
        self.age = 30
        self.ville = 'Paris'

print(Person.personnesCrees) # 0
moi = Person('Varlet', 'Gaëtan')
print(Person.personnesCrees) # 1
print(moi.prenom) # Gaëtan
print(moi.age) # 30
# un an plus tard
moi.age = 31
print(moi.age) # 31
```

- les méthodes d'instances (propre à chaque objet) sont des actions agissant sur l'objet, et se déclarent dans la classe sous la forme `def nomMethode(self, autresParams):`
- le mot clé `self` correspond à l'objet qui appelle la méthode. Faire `monObjet.maMethode(param)` est donc équivalent à `MaClass.maMethode(monObjet, param)`

```py
# ajout d'une méthode dans la classe
def demenager(self, ville):
    self.ville = ville

# appel de la méthode déménager qui change la ville
print(moi.ville) # Paris
moi.demenager('Montrouge')
print(moi.ville) # Montrouge

Person.demenager(moi,'Vanves') # équivalent de moi.demenager('Vanves')
print(moi.ville) # Vanves
```

- il existe des **méthodes de classe**, qui ne travaille pas sur l'instance `self` mais sur la classe. Il faut utiliser le mot clé `cls` à la place de `self`. De plus, pour que Python reconnaisse qu'il s'agit d'une méthode de classe, il faut appeler la fonction `classmethod` qui prend en paramètre la méthode que l'on veut convertir et renvoie la méthode convertie
```py
# déclaration de la méthode de classe dans la classe
def nbPersonnes(cls):
    print("{} personnes ont été créées".format(cls.personnesCrees))
nbPersonnes = classmethod(nbPersonnes)

# appel de la méthode de classe depuis la classe ou depuis l'objet
Person.nbPersonnes() # 1 personnes ont été créées
moi.nbPersonnes() # 1 personnes ont été créées
```

- on peut aussi définir des **méthodes statiques**, proches des méthodes de classe, mais ne prennent **ni self ni cls** en paramètre. Elles sont donc indépendantes de toute donnée appartenant à l'instance de l'objet ou à la classe
```py
# déclaration de la méthode statique dans la classe
def coucou():
    print('ceci est une méthode statique')
coucou = staticmethod(coucou)

# appel de la méthode statique depuis la classe ou depuis l'objet
Person.coucou() # ceci est une méthode statique
moi.coucou() # ceci est une méthode statique
```

- la fonction `dir` renvoie une liste comprenant le nom des attributs et méthodes de l'objet qu'on lui passe en paramètre. En plus de nos méthodes, il y a des **méthodes spéciales** utiles à Python :
```py
print(dir(moi)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'coucou', 'demenager', 'nbPersonnes', 'nom', 'personnesCrees', 'prenom', 'ville']
```

- l'attribut spécial **__dict__** qui est un attribut spécial créé par Python qui est un dictionnaire contenant en clés les noms des attributs de l'objet et en valeur la valeur des attributs. Il est possible de le modifier, cela modifiera également les attributs :
```py
print(moi.__dict__) # {'prenom': 'Gaëtan', 'ville': 'Vanves', 'age': 31, 'nom': 'Varlet'}
moi.__dict__['ville'] = 'Montrouge'
print(moi.ville) # Montrouge
print(moi.__dict__) # {'nom': 'Varlet', 'age': 31, 'prenom': 'Gaëtan', 'ville': 'Montrouge'}
```


## Les propriétés

- l'**encapsulation** est un principe qui consiste à **cacher ou protéger certaines données** de notre objet : dans la plupart des langages objets, on ne peut pas faire depuis l'extérieur de la classe `monObjet.monAttribut`, il faut passer par des **accesseurs** et **mutateurs**
- Python a une philosophie un peu différente : il n'y a pas d'attributs privés, tout est public. En comportement classique, on pourra donc accéder et modifier les attributs en faisant `monObjet.monAttribut`. Dans certains cas, on créera des **propriétés** pour faire respecter l'encapsulation propre au langage, de manière transparente pour l'utilisateur. Cela peut peut être utile si une action particulière doit être menée lors de l'accès ou la modification à un attribut
- une propriété se crée dans le corps de la classe
    - d'abord, dans le constructeur, ajout d'un `_` devant l'attribut, par exemple `_age`. La convention veut qu'on n'accède pas depuis l'extérieur de la classe à un attribut commençant pour `_`
    - création de méthodes commençant par `_get` et `_set`, auxquelles on ne doit également pas accéder de l'extérieur (convention)
    - il faut ensuite déclarer la proriété sans `_` en lui donnant en paramètre : getter (accès à l'attribut), setter (maj de l'attribut), méthode pour supprimer l'attribut, méthode pour demander de l'aide sur l'attribut. Les 2 premières méthodes sont souvent utilisées, les autres moins : `age = property(_getAge, _setAge)`
    - quand on accède à l'attribut age ou qu'on veut modifier le modifier, Python sachant que c'est une proriété nous redirige vers le getter ou le setter

```py
class Person:
    personnesCrees = 0
    def __init__(self, nom, prenom):
        Person.personnesCrees += 1
        self.nom = nom
        self.prenom = prenom
        self._age = 30
        self.ville = 'Paris'
    
    def _getAge(self):
        print("accès à l'âge")
        return self._age
    
    def _setAge(self, nouvelAge):
        print("maj de l'âge")
        self._age = nouvelAge
    
    age = property(_getAge, _setAge)


moi = Person('Varlet', 'Gaëtan')
print(moi.age) # 30
moi.age = 31
print(moi.age) # 31
```


## Les méthodes spéciales
