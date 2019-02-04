import random
import math

cagnotte = int(input('Définissez un montant que vous souhaiter jouer : '))

jouerEncore = 'o'
while(jouerEncore == 'o'):
    numeroAleatoire = random.randrange(50) # entre 0 et 49 inclus
    print('numeroAleatoire',numeroAleatoire)

    numeroMise = int(input('Choisissez un numéro sur lequel miser : '))
    montantMise = int(input('Choisissez une mise pour ce numéro : '))

    if(numeroAleatoire == numeroMise):
        cagnotte += math.ceil(3*montantMise)
    elif(numeroMise%2 == numeroAleatoire%2): # paire ou impaire tous les deux
        cagnotte += math.ceil(0.5*montantMise)
    else:
        cagnotte -= montantMise
    
    texte = "Il faut reste "+ str(cagnotte)+"€. Voulez-vous rejouer (o/n) ?"
    jouerEncore = input(texte)

print("Fin du jeu")

