# -*- coding: utf8
""" Constantes du jeu WordShoot """

import os

path = os.getcwd()
#path= os.popen('pwd').read()
#path = path.strip()
path_shadows=path+'/shadows'

titre_fenetre=' '*15+" * Caglio Word Shooting *"
logo1='WordShoot'

# Images du jeu
intro= path+"/Caglio-WShoot_images/intro01.png"
ecran1= path+"/Caglio-WShoot_images/ecran2.png"
ecran_jeu= path+"/Caglio-WShoot_images/linux2.jpg"

# Musiques du jeu
music1= path+"/WorldShoot-Musik/atfield05.ogg"
music2= path+"/WorldShoot-Musik/4dimension1.mp3"
music3= path+"/WorldShoot-Musik/impro-acid120.mp3"
music4= path+"/WorldShoot-Musik/Cets1.mp3"
 
# titres
ATF1="AT Field - Mystere et Boule de Gomme."
aaa1 ='Quatrieme Dimension - Attaches ta cravate.'
Cets1='Cets - Impro-Acid 120'
Cets2='Cets - Crazy Alarm Clock v01'

# Bruitages du jeu
umi_no_koto = path+"/WorldShoot-Musik/Umi_no_Koto.wav"
baleine = path+ "/WorldShoot-Musik/Baleine01.ogg"
son01 = path+"/WorldShoot-Musik/excelent0001.ogg"
son02 = path+"/WorldShoot-Musik/loose.ogg"
bip = path+"/WorldShoot-Musik/beep03.ogg"
bipp = path+"/WorldShoot-Musik/beep01.ogg"
click = path+"/WorldShoot-Musik/click02.ogg"
zero_un = path+"/WorldShoot-Musik/zero_1.ogg"
zero_deux = path+"/WorldShoot-Musik/zero_2.ogg"
zero_trois = path+"/WorldShoot-Musik/zero_3.ogg"
zero_quatre = path+"/WorldShoot-Musik/zero_4.ogg"
zero_cinq = path+"/WorldShoot-Musik/zero_5.ogg"
zero_six = path+"/WorldShoot-Musik/zero_6.ogg"
zero_sept = path+"/WorldShoot-Musik/zero_7.ogg"
zero_huit = path+"/WorldShoot-Musik/zero_8.ogg"
zero_neuf = path+"/WorldShoot-Musik/zero_9.ogg"
niveau_fini = path+"/WorldShoot-Musik/niveau_fini.ogg"
clock = path+"/WorldShoot-Musik/clock.ogg"
ligne='________________________________________________________________________'

## Code couleurs
ROUGE = (245, 5, 5)
NOIR = (0, 0, 0)
VERT = (0, 55, 0)
ORANGE = (255, 100, 0)
BLEU = (0, 200, 255)

# Liste alphabeta représentant les touches du clavier virtuel.
alphabeta=['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n',',',';',':','!']

## Mes ptits booléens
musique = True
son = True
hard = False
choix = False
continuer = True
sauvegarde= False
formalite = True
aleph = False
vie_symbole=u"\u262F"
looser=" You Loose T.T"

## Coordonnées
x=255
y=255

phidor=55
