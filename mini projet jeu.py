from random import randint
amplitude= int(input('entrez le range du nombre a deviner: '))
a= int(input('entrez le nombre d"essai: '))

nbr_deviner = randint(1, amplitude)

nbr_essai= range(a)  #$ git config --global user.name "John Doe"
                    #$ git config --global user.email johndoe@example.com
nbr_essai= range(a)
for i in nbr_essai:

	essai = int(input("entrez un nombre {0} essai: ". format(i+1)))
	if essai < nbr_deviner:
		print('plus grand que {0}'.format(essai))
	elif essai > nbr_deviner:
		print('plus petit que {0}'.format(essai))
	else:
		print('vous aviez gagner en {0} essai\n'.format(i+1))
		break
if essai!=nbr_deviner:
	print('vous aviez perdu')
	print('le nombre etait: {0}'.format(nbr_deviner))

print('fin du jeu')