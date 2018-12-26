#!/usr/bin/python2
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>
# word shoot

import random
import pygame
import time
from pygame.locals import *
from WSconstantes import *
from WordShootClass import *

################################ Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((800, 600), RESIZABLE)
size, x, y = (0,0), 800, 600

# Pour fonction appui long
pygame.key.set_repeat(400, 30)

# Création d'un rectangle noir pour le fond
#pygame.draw.rect(fenetre, (180, 20, 150), (0, 0, 2000 , 1100 ))
#pygame.display.flip()
intrologo= pygame.image.load(intro).convert()
neo = pygame.image.load(ecran_jeu).convert()
#fond.fill((0,0,0)) # Remplissage avec du noir

 
# Titre fenetre
pygame.display.set_caption(titre_fenetre)

#Rafraîchissement de l'écran
pygame.display.flip()

# Chargement des musiques de jeu
pygame.mixer.music.load(music1)
#pygame.mixer.music.queue(music2)
#pygame.mixer.music.queue("WorldShoot-Musik/afx03.ogg")

victoire = pygame.mixer.Sound(umi_no_koto)
excelent = pygame.mixer.Sound(son01)
loose = pygame.mixer.Sound(son02)
bal= pygame.mixer.Sound(baleine)
bip = pygame.mixer.Sound("WorldShoot-Musik/beep03.ogg")
bipp = pygame.mixer.Sound("WorldShoot-Musik/beep01.ogg")
click = pygame.mixer.Sound("WorldShoot-Musik/click01.wav")
zero_un = pygame.mixer.Sound("WorldShoot-Musik/zero_1.ogg")
zero_deux = pygame.mixer.Sound("WorldShoot-Musik/zero_2.ogg")
zero_trois = pygame.mixer.Sound("WorldShoot-Musik/zero_3.ogg")
zero_quatre = pygame.mixer.Sound("WorldShoot-Musik/zero_4.ogg")
zero_cinq = pygame.mixer.Sound("WorldShoot-Musik/zero_5.ogg")
zero_six = pygame.mixer.Sound("WorldShoot-Musik/zero_6.ogg")
zero_sept = pygame.mixer.Sound("WorldShoot-Musik/zero_7.ogg")
zero_huit = pygame.mixer.Sound("WorldShoot-Musik/zero_8.ogg")
zero_neuf = pygame.mixer.Sound("WorldShoot-Musik/zero_9.ogg")
niveau_fini = pygame.mixer.Sound("WorldShoot-Musik/niveau_fini.ogg")

ligne='___________________________________________________________________________'

########### fonctions et pocédures
def son_vitesse(score):
    if score == 100:
        print ' -- 0.1 --'
        zero_un.play()
    elif score == 200:
        print ' -- 0.2 --'
        zero_deux.play()
    elif score == 300:
        print ' -- 0.3 --'
        zero_trois.play()
    elif score == 400:
        print ' -- 0.4 --'
        zero_quatre.play()
    elif score == 500:
        print ' -- 0.5 --'
        zero_cinq.play()
    elif score == 600:
        print ' -- 0.6 --'
        zero_six.play()
    elif score == 700:
        print ' -- 0.7 --'
        zero_sept.play()
    elif score == 800:
        print ' -- 0.8 --'
        zero_huit.play()
    elif score == 900:
        print ' -- 0.9 --'
        zero_neuf.play()
    elif score == 1000:
        print ' -- Niveau Complété --'
        niveau_fini.play()


class Game():

    font=pygame.font.Font(None, 29) # Initialise police de charactère
    font2=pygame.font.Font(None, 55)

############################# Debut prog

    fenetre.blit(intrologo, (0,0))
    pygame.display.flip()
    bal.play()
    time.sleep(3)

    ligne1= font.render(ligne,2,( 251, 8, 8 )) # Ligne de fin de chute des mots

    obj= Score() # Construction du score
    score1=obj.score
    score=Score.score
    
    obj = Lecture() # Lecture du fichier


    # Démarage de la musique de fond
#    pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)
#    pygame.mixer.music.play()

    continuer = 1
    while continuer:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30) # 30 fps

        ########### instances du module WordShootClass
        obj = Mot() # on cree une instance de la class Mot
        mot = obj.mot # on affecte l'attribut 'mot' de la class Mot à la variable mot

        obj1= Vitesse() # on cree une instance de la class Vitesse
        vitesse = obj1.vitesse  # on affecte l'attribut vitesse de la class Vitesse à la variable vitesse

        objA = Construction(mot) # on cree une instance de la class Construction en lui passant le parametre mot 
        artefact = objA.artefact # on affect l'attribut artefact de la class Construction à la variable artefact


        sujet = Lettre() # Enfin, on cree une instance de la class lettre, l'objet sera le charactère à trouver de la chaine mot
        lettre = sujet.lettre # Affectation

        index = Lettre.index +1 # pour log



        ########### Construction fenetres
        text = font.render(mot,2,( 80, 241, 0 ))
        aaaa=random.randint(1,720)   # On tire au hasard le point d'apparition du mot sur l'axe horizontale
        fenetre.blit(text, (aaaa,1)) 
        sCore = font.render(score1,2,( 80, 241, 0 ))

        ### LOGs
        print "le mot est: {}".format(mot)
        print "la lettre n°: {} est: {}".format(index , lettre)
        print "voici l'artefact: {}".format(artefact)

#        son_vitesse(score)  # Appel de la procédure son_vitesse         

        destruct = 0
        max=1
        while max < 455 and destruct == 0:
            pygame.time.Clock().tick(vitesse)
            fenetre.blit(text, (aaaa,max))   # affichage text tombant  
            max +=1   

            obj1= Vitesse()  # Instance de la class Vitesse pour controle de la vitesse en fonction du score
            vitesse = obj1.vitesse # Affectation de la variable d'instance vitesse
            score=obj1.score  # Affectation de la variable d'instance score


            # Petite vérifications
            if max ==445:    # Son de fin de chute
                loose.play() 

            if max == 455: # Reinitialisation de l'index
                sujet.reinit()


            sujet.alteration() # Appel de la methode alteration de la class Lettre
            sample2=sujet.sample2
            text1 = font.render(sample2,2,( 255, 0, 0 ))
            fenetre.blit(text1, (aaaa,max))



            simbad = ""
            for index,e in enumerate(artefact):
                simbad += e
            ping = font2.render(simbad,22,( 240, 240, 4 )) # Affichage chaine de charactère contenue dans la liste 'artefact"

            pygame.display.flip() # Rafraichissement
            fenetre.blit(neo, (0,0))
            fenetre.blit(ligne1, (0,450))
            fenetre.blit(ping, (350,500))     
            fenetre.blit(sCore, (700,550))


            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus


                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    continuer = 0 
                    destruct = 0

                if event.type == KEYDOWN: # Si un de ces éléments est de type clavier
                    if event.key == K_ESCAPE:
                        bipp.play()
                        continuer = 0
                        destruct = 0
                        max = 455


                    if event.key == K_a:
                        if 'a' == lettre:
                            print '** UP **'
                            objA.tetris(lettre)  # appel de la methode tetris de la class Construction qui modifie la liste artefact
                            sujet = Lettre()     # On re-instancie l'objet sujet pour passer à la lettre suivante
                            lettre = sujet.lettre 
                            index = Lettre.index + 1  # indice uniquement pour les logs...
                        else:
                            print '** DOWN **'

                    if event.key == K_b:
                        if 'b' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_c:
                        if 'c' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_d:
                        if 'd' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_e:
                        if 'e' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_f:
                        if 'f' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_g:
                        if 'g' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_h:
                        if 'h' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
  
                        else:
                            print '** DOWN **'

                    if event.key == K_i:
                        if 'i' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_j:
                        if 'j' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_k:
                        if 'k' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
 
                        else:
                            print '** DOWN **'

                    if event.key == K_l:
                        if 'l' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                            print '** DOWN **'

                    if event.key == K_m:
                        if 'm' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_n:
                        if 'n' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1  
 
                        else:
                            print '** DOWN **'

                    if event.key == K_o:
                        if 'o' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_p:
                        if 'p' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   

                        else:
                            print '** DOWN **'

                    if event.key == K_q:
                        if 'q' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
     
                        else:
                            print '** DOWN **'

                    if event.key == K_r:
                        if 'r' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
      
                        else:
                            print '** DOWN **'

                    if event.key == K_s:
                        if 's' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
       
                        else:
                            print '** DOWN **'

                    if event.key == K_t:
                        if 't' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
               
                        else:
                            print '** DOWN **'

                    if event.key == K_u:
                        if 'u' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
                
                            print '** DOWN **'

                    if event.key == K_v:
                        if 'v' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
          
                        else:
                            print '** DOWN **'

                    if event.key == K_w:
                        if 'w' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
      
                        else:
                            print '** DOWN **'

                    if event.key == K_x:
                        if 'x' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
                
                        else:
                            print '** DOWN **'

                    if event.key == K_y:
                        if 'y' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
            
                        else:
                            print '** DOWN **'

                    if event.key == K_z:
                        if 'z' == lettre:
                            print '** UP **'
                            click.play() 
                            objA.tetris(lettre) 
                            sujet = Lettre()  
                            lettre = sujet.lettre 
                            index = Lettre.index + 1   
 
                        else:
                            print '** DOWN **'


                    if sujet.victoire == True:
                        print '** VICTORY !! **'
                        excelent.play() 
                        obj= Score()  # On refait une instance pour incrémenter le score
                        score1=obj.score
                        max = 455     # On termine la boucle

                son_vitesse(score)  # Appel de la procédure son_vitesse         

        pygame.display.flip() # Rafraichissement





if __name__ == '__main__':
    Game()






