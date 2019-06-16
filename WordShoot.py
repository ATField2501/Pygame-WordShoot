#!/usr/bin/python2
# coding: utf8 

                               ###########################
                               #       WordShoot         #
                               #   auteur: cagliostro    #
                               # <atfield2501@gmail.com> #
                               #      Licence GPL        #
                               ###########################

import string
import random
import pygame
import time
import sys
from threading import Thread,RLock
from pygame.locals import *
from WSconstantes import *
from WordShootClass import *


################################ Initialisation de la bibliothèque Pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.mixer.init()
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
# Initialise police de charactère
font=pygame.font.Font(None, 29) 
font2=pygame.font.Font(None, 55)


def son_vitesse(score, supra):
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
        supra.add_vie()
    
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

verrou= RLock()

class Gestion_volumetrik(Thread):
    """ Gère la gestion des évennements au menu principale"""
    def __init__(self,phidor):
        Thread.__init__(self)
        self.phidor=phidor
    def run(self):
        # RLock
        with verrou:
            if self.phidor == 55:
                self.phidor = 56
                print(self.phidor)
                time.sleep(0.7)
            if self.phidor == 56:
                self.phidor = 55
                print(self.phidor)
                time.sleep(0.7)
            
class Gestion_Ev_menu():
    c=True
    def __init__(self): 
        """ """ 
        obj1=Selecteur()
        self.selection=obj1.selecteur
        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    click.play()
                    Gestion_Ev_menu.c= False
                if event.key == K_ESCAPE:
                    bipp.play()
                    sys.exit(0)
                if event.key == K_LEFT:
                    print('yo yo LEFT !!')
                    bipp.play()
                    obj1.deplace_moins() 
                    obj1=Selecteur()  
                    self.selection=obj1.selecteur
                    Gestion_Ev_menu.choix = True
                if event.key == K_RIGHT:
                    print('yo yo RIGHT !!')
                    bipp.play()
                    obj1.deplace_plus() 
                    obj1=Selecteur() 
                    self.selection=obj1.selecteur
                    Gestion_Ev_menu.choix = True           


class Gestion_Ev_nickname():
    long_nickname=0
    formalite=True
    def __init__(self,nickname):
        self.nickname=nickname
        for event in pygame.event.get():
            # Si un de ces événements est de type QUIT
            if event.type == QUIT:     
                Gestion_Ev_nickname.formalite = False

            # Si un de ces éléments est de type clavier
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    Gestion_Ev_nickname.long_nickname=12
                if event.key == K_BACKSPACE:
                    try:
                        if Gestion_Ev_nickname.long_nickname != 0:
                            del self.nickname[-1]
                            Gestion_Ev_nickname.long_nickname -= 1
                            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
                            stone22= font.render(''.join(self.nickname),2,(80,241,0)) 
                            fenetre.blit(stone22,(50,350))
                            pygame.display.flip()
                        else:
                            self.nickname= ['nickname: ']
                            stone= font.render(''.join(self.nickname),2,(80,241,0))
                            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))

                            fenetre.blit(stone,(50,350))
                            pygame.display.flip()
                 
                    except  IndexError:
                        self.nickname= ['nickname: ']
                        Gestion_Ev_nickname.long_nickname = 0
                        pygame.display.flip()
                
                if event.key == K_a:
                    self.nickname.append('a')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_b:
                    self.nickname.append('b')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_c:
                    self.nickname.append('c')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_d:
                    self.nickname.append('d')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_e:
                    self.nickname.append('e')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_f:
                    self.nickname.append('f')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_g:
                    self.nickname.append('g')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_h:
                    self.nickname.append('h')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_i:
                    self.nickname.append('i')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_j:
                    self.nickname.append('j')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_k:
                    self.nickname.append('k')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_l:
                    self.nickname.append('l')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_m:
                    self.nickname.append('m')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_n:
                    self.nickname.append('n')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_o:
                    self.nickname.append('o')
                    Gestion_Ev_nickname.long_nickname += 1                            
                if event.key == K_p:
                    self.nickname.append('p')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_q:
                    self.nickname.append('q')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_r:
                    self.nickname.append('r')
                    Gestion_Ev_nickname.long_nickname += 1
                if event.key == K_s:
                    self.nickname.append('s')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_t:
                    self.nickname.append('t')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_u:
                    self.nickname.append('u')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_v:
                    self.nickname.append('v')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_w:
                    self.nickname.append('w')
                    Gestion_Ev_nickname.long_nickname += 1                 
                if event.key == K_x:
                    self.nickname.append('x')
                    Gestion_Ev_nickname.long_nickname += 1 
                if event.key == K_y:
                    self.nickname.append('y')
                    Gestion_Ev_nickname.long_nickname += 1                
                if event.key == K_z:
                    self.nickname.append('z')
                    Gestion_Ev_nickname.long_nickname += 1
                 

class WordShoot():
    """ Pygame - Worshoot - Classe Principale """
    ############################# Debut prog
    fenetre.blit(intrologo, (0,0))
    pygame.display.flip()
    bal.play()
    time.sleep(3)
    ligne1 = font.render(ligne,2,( 251, 8, 8 )) # Ligne de fin de chute des mots
    objet=Score() # Construction du score
    score= Score.score
    obj = Lecture() # Lecture du fichier
    
    # Démarage de la musique de fond
#    pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)
#    pygame.mixer.music.play()
    
    while continuer:
        ## Initialisation du capital de points de vie
        supra= Vie_Joueur()
        ##### Ecran Principale
        c = True
        while c:            
            truc=Gestion_Ev_menu()
            selection = truc.selection
            c = Gestion_Ev_menu.c 
            font3=pygame.font.Font(path+'Horst___.ttf', phidor)    
            ## Ecran de depart
            fenetre.blit(ecran1,(0,0))
            ## Element du tableau Selecteur 
            select=font.render(selection,2,( 80, 241, 0 ))
            fenetre.blit(select,(362,390))      
            ## Titre du Jeu
            titre=font3.render(logo1,2,(241,255,68))
            fenetre.blit(titre,(200,300))
           
            pygame.display.flip()
                  
        if selection == Selecteur.tableau[0]:      
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            ### Entrée du nom du joueur
            nickname= ['nickname: ']
#            stone= font.render(''.join(nickname),2,(80,241,0))
#            fenetre.blit(stone,(50,350))
            pygame.display.flip()
            long_standart=len(nickname[0])
            long_nickname=0
            # je limite la longueur du self.nickname 12
            while formalite == True and long_nickname < 12:
                bidule=Gestion_Ev_nickname(nickname)
                formalite=bidule.formalite       
                long_nickname=bidule.long_nickname         
                pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
                stone= font.render(''.join(bidule.nickname),2,(80,241,0))
                fenetre.blit(stone,(50,350))
                pygame.display.flip()
            while aleph == False:
                # on cree une instance de la class Mot
                obj = Mot()
                # on affecte l'attribut 'mot' de la class Mot à la variable mot
                mot = obj.mot           
                # on cree une instance en passant en parametre mot 
                objA = Construction(mot)
                # on affect l'attribut artefact à la variable artefact
                artefact = objA.artefact    
                # on cree une instance, l'objet sera le charactère à trouver 
                sujet = Lettre()      
                lettre = sujet.lettre # Affectation
                index = Lettre.index +1 # pour log

                ########### Construction fenetres
                text = font.render(mot,2,( 80, 241, 0 ))
                # On tire au hasard le point d'apparition du mot sur l'axe horizontale
                aaaa=random.randint(1,720)  
                fenetre.blit(text, (aaaa,1))
                objet.score_forme()
                sCore = font.render(str(objet.score_en_forme),2,( 80, 241, 0 ))
                nick = font.render(str(''.join(nickname[1:])),2,(255,162,0))    
                vie = font2.render(str(supra.vue_sur_vie_joueur),2,( 120, 94, 246 ))
                ### LOGs
                print "le mot est: {}".format(mot)
                print "la lettre n°: {} est: {}".format(index , lettre)
                print "voici l'artefact: {}".format(artefact)
                obj_v=Vitesse()                
                destruct = False
                max=1
                while max < 455 and destruct == False:
                    # son_vitesse(score, supra)  # Appel de la procédure son_vitesse 
#############
                    pygame.time.Clock().tick(obj_v.vitesse)
                    fenetre.blit(text, (aaaa,max))   # affichage text tombant  
                    max +=1   
                    # Affectation de la variable d'instance score
                    score=Score.score 
                    # Appel de la methode alteration de la class Lettre
                    sujet.alteration() 
                    sample2=sujet.sample2
#                    sample1=sujet.sample1
                    text1 = font.render(sample2,2,( 255, 0, 0 ))
#                    text2 = font.render(sample1,2,( 255, 0, 0 ))
                    fenetre.blit(text1, (aaaa,max))
#                    fenetre.blit(text2, (aaaa,max))
                    
                    # Petite vérifications
                    if max ==453:    # Son de fin de chute
                        loose.play() 
                        objet.score_forme()
                        sauvegarde = supra.enlev_vie()
                        sujet.reinit()
                        destruct = True

                    # Affichage chaine de charactère contenue dans la liste 'artefact"
                    simbad= ''.join(artefact)
                    ping = font2.render(simbad,22,( 240, 240, 4 )) 
                    pygame.display.flip() # Rafraichissement
                    fenetre.blit(neo, (0,0))
                    fenetre.blit(ligne1, (0,450))
                    fenetre.blit(nick, (350,500))     
                    fenetre.blit(sCore, (700,550))
                    fenetre.blit(vie, (50,550))
                    fenetre.blit(ping,(325,550))
                    
                    
                    #On parcours la liste de tous les événements reçus
                    for event in pygame.event.get():   
                        #Si un de ces événements est de type QUIT
                        if event.type == QUIT:        
                           # continuer = False
                            destruct = True
                            print('double-ok')
                        # Si un de ces éléments est de type clavier
                        if event.type == KEYDOWN:       
                            if event.key == K_ESCAPE:
                                bipp.play()
                                # Reinitialisation de l'index pour detruire complètement le sujet
                                sujet.reinit()
                           #     destruct = True
                                max = 455
                            #    aleph = True
                                print('ok')
                                  
                            if event.key == K_a:
                                if 'a' == lettre:
                                    print '** UP **'
                                    # appel de la methode tetris qui modifie la liste artefact
                                    objA.tetris(lettre)
                                    # On re-instancie l'objet sujet pour passer à la lettre suivante
                                    sujet = Lettre()    
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

                            ### Test si le mot à été trouvé
                            if sujet.victoire == True:
                                print '** VICTORY !! **'
                                excelent.play() 
                                objet.score_plus() # incrémente le score 
                                objet.score_forme() # je le remet en forme string
                                # Appel de la methode alteration de la class Lettre
                                sujet.alteration(suprem=True)                                
                                sample2=sujet.sample2
                                text1 = font.render(sample2,2,( 255, 0, 0 ))
                                fenetre.blit(text1, (aaaa,max))
                                # Appel de la procédure son_vitesse 
                                son_vitesse(score, supra)        
                                max = 455     # On termine la boucle
             
                pygame.display.flip() # Rafraichissement

                if sauvegarde == True:
                    nb=0
                    while nb <= 4:
                        time.sleep(1)
                        nb+=1
                        truc="You Loose T.T" 
                        ecran_sauvegarde=font2.render(truc,2,(80,241,0))
                        fenetre.blit(ecran_sauvegarde,(255+nb,35+nb))
                        
                        # Création d'un rectangle noir pour le fond
                 #        pygame.draw.rect(fenetre, (0, 0 , 0), (0, 0, 2000 , 1100 ))
                        pygame.display.flip()
                 
                    nicknamu=''.join(self.nickname[1:])
                       
                    # Vérification si le score est un reccord
                    bidule=objet.verif_reccord(nicknamu)
                    ecran_chouette=font2.render(bidule,2,(80,241,0))
                    fenetre.blit(ecran_chouette,(255,400))
                    pygame.display.flip()
                    time.sleep(3)
                    formalite = True                   
                    objet=Score() # Construction du score
                   
#                    destruct=True
                    sauvegarde = False
                    continuer = True
                    supra.reinit_vie()
                    aleph = True
    
        # Menu Scores
        if selection == Selecteur.tableau[1]:
            # Création d'un rectangle noir pour le fond
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            pygame.display.flip()
            ecran_reccords=objet.lecture_score()
            babylone=ecran_reccords
            like=25
            try:
                for e in babylone:
                    nervure=font.render(e,2,(250,250,0))
                    fenetre.blit(nervure,(155,like))
                    pygame.display.flip()   
                    time.sleep(0.4)
                    like += 35        
                time.sleep(5)
        
                for event in pygame.event.get():   
                    if event.type == KEYDOWN: 
                        if event.key == K_ESCAPE:
                            bipp.play()
                            
            except TypeError:
                pass
#            formalite = True
#            aleph = False
#            sauvegarde = False
            continuer = True
            selection = ' '
#            supra.reinit_vie()


        # Menu Crédits
        if selection == Selecteur.tableau[2]:
            # Création d'un rectangle noir pour le fond
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            pygame.display.flip()
            unedeplus= True
            while unedeplus:
                ether=[]
                with open(path+"Caglio_credits.txt", "r") as fichier:
                    for ligne in fichier:
                        ether.append(ligne)
                        max = 1
                        
                    for index, i in enumerate(ether):
                        B=random.randint(0,255)
                        R=random.randint(0,255)
                        G=random.randint(0,255)
                        yin = i.strip()
                        credit = font.render(yin,2,( B, 255, G ))
                        longg= len(ether[index])
                        balthazar=400-(longg*5)
                        fenetre.blit(credit, (balthazar,max)) 
                        pygame.display.flip() # Rafraichissement
                        max += 35
                        time.sleep(0.1)
                        for event in pygame.event.get():
                            if event.type == KEYDOWN: 
                                if event.key == K_ESCAPE:
                                    bipp.play()
                                    
                                    unedeplus = False        
                                     
        
        # menu quit 
        if selection == Selecteur.tableau[4]:
            # Création d'un rectangle noir pour le fond
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            bye="A BientOt"
            depart=font3.render(bye,2,(255,124,5))
            fenetre.blit(depart,(150,300))
            pygame.display.flip()
            time.sleep(1)
            sys.exit(0)



if __name__ == '__main__':
    WordShoot()
   


