

monDictionnaire = {} # monDictionnaire = dict()
monDictionnaire['maCle1'] = 'maValeur1'
monDictionnaire['maCle2'] = 'maValeur2'
print(monDictionnaire) # {'maCle1': 'maValeur1', 'maCle2': 'maValeur2'}
valSup = monDictionnaire.pop('maCle1')
print(monDictionnaire) # {'maCle2': 'maValeur2'}
print(valSup) # maValeur1