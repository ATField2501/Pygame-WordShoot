#!/usr/bin/python2
# -*- coding: utf8 

                               ###########################
                               #       WordShoot         #
                               #   auteur: cagliostro    #
                               # <atfield2501@gmail.com> #
                               #      Licence GPL        #
                               ###########################

import random
import pygame
import time
import sys
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

intrologo= pygame.image.load(intro).convert()
ecran1=pygame.image.load(ecran1).convert()
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
bip = pygame.mixer.Sound(bip)
bipp = pygame.mixer.Sound(bipp)
click = pygame.mixer.Sound(click)
zero_un = pygame.mixer.Sound(zero_un)
zero_deux = pygame.mixer.Sound(zero_deux)
zero_trois = pygame.mixer.Sound(zero_trois)
zero_quatre = pygame.mixer.Sound(zero_quatre)
zero_cinq = pygame.mixer.Sound(zero_cinq)
zero_six = pygame.mixer.Sound(zero_six)
zero_sept = pygame.mixer.Sound(zero_sept)
zero_huit = pygame.mixer.Sound(zero_huit)
zero_neuf = pygame.mixer.Sound(zero_neuf)
niveau_fini = pygame.mixer.Sound(niveau_fini)

########### fonctions et pocédures
def son_vitesse(score, supra):
    if score == 100:
        print ' -- 0.1 --'
        zero_un.play()
        supra.add_vie()
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
    objet=Score() # Construction du score
    score= Score.score
    obj= Lecture() # Lecture du fichier
    obj= Selecteur() # Première instance sans parametre 
    selection= obj.selecteur

    supra= Vie_Joueur()

    # Démarage de la musique de fond
#    pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)
#    pygame.mixer.music.play()
    c= 1
    continuer= True
    while continuer:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30) # 30 fps
        obj=Selecteur() # Première instance sans parametre 
#    obj.reinit()
        selection=obj.selecteur
        ##### Ecran Principale
        c = True
        while c:      
            fenetre.blit(ecran1,(0,0)) ## Ecran de depart

            select=font.render(selection,2,( 80, 241, 0 ))
            fenetre.blit(select,(362,390)) ## premier mot du tableau

            pygame.display.flip()
            for event in pygame.event.get(): 
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        click.play()
                        c= False
                    if event.key == K_ESCAPE:
                        bipp.play()
                        time.sleep(1)
                        sys.exit(0)
                    if event.key == K_DOWN:
                        bipp.play()
                        obj.deplace_moins() # Appel de la methode deplace_moins de la class Selecteur
                        obj=Selecteur() # Instance de la class Selecteur 
                        selection=obj.selecteur
                    if event.key == K_UP:
                        bipp.play()
                        obj.deplace_plus() # Appel de la methode deplace_plus de la class Selecteur
                        obj=Selecteur() # Instance de la class Selecteur
                        selection=obj.selecteur



        if selection == tableau[0]:                     
            while aleph == False:
                ########### instances du module WordShootClass
                obj = Mot() # on cree une instance de la class Mot
                mot = obj.mot # on affecte l'attribut 'mot' de la class Mot à la variable mot

           #     obje_V=Vitesse() # on cree une instance de la class Vitesse
                objA = Construction(mot) # on cree une instance de la class Construction en lui passant le parametre mot 
                artefact = objA.artefact # on affect l'attribut artefact de la class Construction à la variable artefact


                sujet = Lettre() # Enfin, on cree une instance de la class lettre, l'objet sera le charactère à trouver de la chaine mot
                lettre = sujet.lettre # Affectation

                index = Lettre.index +1 # pour log


                ########### Construction fenetres
                text = font.render(mot,2,( 80, 241, 0 ))
                aaaa=random.randint(1,720)   # On tire au hasard le point d'apparition du mot sur l'axe horizontale
                fenetre.blit(text, (aaaa,1))
                objet.score_forme()
                sCore = font.render(str(objet.score_en_forme),2,( 80, 241, 0 ))
                    
                vie = font2.render(str(supra.vue_sur_vie_joueur),2,( 120, 94, 246 ))
                ### LOGs
                print "le mot est: {}".format(mot)
                print "la lettre n°: {} est: {}".format(index , lettre)
                print "voici l'artefact: {}".format(artefact)

                destruct = False
                max=1
                while max < 455 and destruct == False:
                    obje_V=Vitesse() 
                    pygame.time.Clock().tick(obje_V.vitesse)
                    fenetre.blit(text, (aaaa,max))   # affichage text tombant  
                    max +=1   

                    score=Score.score  # Affectation de la variable d'instance score

                    sujet.alteration() # Appel de la methode alteration de la class Lettre
                    sample2=sujet.sample2
                    text1 = font.render(sample2,2,( 255, 0, 0 ))
                    fenetre.blit(text1, (aaaa,max))

                    # Petite vérifications
                    if max ==445:    # Son de fin de chute
                        loose.play() 
                        objet.score_forme()
                        sauvegarde = supra.enlev_vie()
                        sujet.reinit()

                 
                    simbad= ''.join(artefact)
                    ping = font2.render(simbad,22,( 240, 240, 4 )) # Affichage chaine de charactère contenue dans la liste 'artefact"

                    pygame.display.flip() # Rafraichissement
                    fenetre.blit(neo, (0,0))
                    fenetre.blit(ligne1, (0,450))
                    fenetre.blit(ping, (350,500))     
                    fenetre.blit(sCore, (700,550))
                    fenetre.blit(vie, (50,550))
         
                    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus


                        if event.type == QUIT:     #Si un de ces événements est de type QUIT
                            continuer = False
                            destruct = True

                        if event.type == KEYDOWN: # Si un de ces éléments est de type clavier
                            if event.key == K_ESCAPE:
                                bipp.play()
                                sujet.reinit() # Reinitialisation de l'index pour detruire complètement le sujet
                                destruct = True
                                max = 455
                                aleph = True


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
                                objet.score_plus() # incrémente le score
                                
                                objet.score_forme() # je le remet en forme string
                                max = 455     # On termine la boucle

                son_vitesse(score, supra)  # Appel de la procédure son_vitesse         

                pygame.display.flip() # Rafraichissement

                if sauvegarde == True:
                    nb=0
                    while nb <= 4:
                        time.sleep(1)
                        nb+=1
                        truc="You Loose T.T" 
                        ecran_sauvegarde=font2.render(truc,2,(80,241,0))
                        fenetre.blit(ecran_sauvegarde,(255+nb,255+nb))
                        
                        # Création d'un rectangle noir pour le fond
                 #        pygame.draw.rect(fenetre, (0, 0 , 0), (0, 0, 2000 , 1100 ))
                        pygame.display.flip()
                        # Vérification si le score est un reccord
                        #*****
                        # Si oui on demande de rentrer un nickname
                        #*****
                        # et on ecris le tous ^^
                        nickname='code2501'
                        objet.ecriture_score(nickname)               
                        aleph = True
                        destruct=True
                        max=445
        
        # Menu Scores
        if selection == tableau[1]:
            # Création d'un rectangle noir pour le fond
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            pygame.display.flip()
            ecran_reccords=objet.lecture_score()
            babylone=ecran_reccords[0]
            zygurate=ecran_reccords[1]
            nerve=babylone+'  --> '+str(zygurate)+'Pts'
            nervure=font.render(nerve,2,(125,125,0))
            durandale = True
            while durandale:
                fenetre.blit(nervure,(255,255))
                pygame.display.flip()
                time.sleep(1)
                for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                    if event.type == KEYDOWN: 
                        if event.key == K_ESCAPE:
                            bipp.play()
                            durandale = False


        # Menu Crédits
        if selection == tableau[2]:
            # Création d'un rectangle noir pour le fond
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            pygame.display.flip()
            ether=[]
            with open(path+"Caglio_credits.txt", "r") as fichier:
                for ligne in fichier:
                    ether.append(ligne)
                    long= len(ether)
                    max = 1
                    for index, i  in enumerate(ether):
                        yin = i.strip()
                        credit = font.render(yin,2,( 80, 241, 0 ))
                        fenetre.blit(credit, (125,max)) 
                        pygame.display.flip() # Rafraichissement
                        max +=35
                        time.sleep(0.1)
                    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                        if event.type == KEYDOWN: 
                            if event.key == K_ESCAPE:
                                bipp.play()
                                break



if __name__ == '__main__':
    Game()






