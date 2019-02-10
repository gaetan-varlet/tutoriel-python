monDictionnaire = {} # monDictionnaire = dict()
monDictionnaire['maCle1'] = 'maValeur1'
monDictionnaire['maCle2'] = 'maValeur2'
print(monDictionnaire) # {'maCle1': 'maValeur1', 'maCle2': 'maValeur2'}
monDictionnaire['maCle1'] = 'maValeur3' # maj de la valeur de maCle1
print(monDictionnaire) # {'maCle1': 'maValeur3', 'maCle2': 'maValeur2'}
print(monDictionnaire['maCle1']) # maValeur3