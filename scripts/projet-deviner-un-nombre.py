from random import randint

nombre_a_deviner = randint(1,100)
print(nombre_a_deviner)


nombre_essais = range(1,6)
for i in nombre_essais:
    essai = int(input('Entrer un nombre ({0} essai) : '.format(i)))
    if essai == nombre_a_deviner:
        print('Bravo, vous avez gagné en ',i,'essais !')
        break
    elif essai < nombre_a_deviner:
        print('Le nombre à deviner est plus grand que',essai)
    else:
        print('Le nombre à deviner est plus petit que',essai)

if essai != nombre_a_deviner:
    print('Vous avez perdu !')
    print('Le nombre a deviner était',nombre_a_deviner)

print('Fin de jeu')

