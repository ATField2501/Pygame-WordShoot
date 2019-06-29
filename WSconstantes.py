# -*- coding: utf8
""" Constantes du jeu WordShoot """

import os

path= os.popen('pwd').read()
path = path.strip()
path_shadows=path+'/shadows'

titre_fenetre=' '*15+" * Caglio Word Shooting *"
logo1='WorldShoot'

# Images du jeu
intro= path+"/Caglio-WShoot_images/intro01.png"
ecran1= path+"/Caglio-WShoot_images/ecran2.png"
ecran_jeu= path+"/Caglio-WShoot_images/linux2.jpg"

# Musiques du jeu
music1= path+"/WorldShoot-Musik/atfield05.ogg"
music2= path+"/WorldShoot-Musik/afx02.ogg"


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
