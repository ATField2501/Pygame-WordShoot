#!/usr/bin/python2
# coding: utf8 

                               ###########################
                               #       WordShoot         #
                               #   auteur: cagliostro    #
                               # <atfield2501@gmail.com> #
                               #      Licence GPL        #
                               ###########################

#import string
import random
import pygame
import time
import sys
from threading import Thread,RLock
from pygame.locals import *
from WSconstantes import *
from WordShootClass import *


################################ Initialisation de la bibliothèque Pygame
# Initialisation du buffer audio
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

# info
a = pygame.display.Info()
## coordonnées
x = a.current_w/2
y = a.current_h/2
#
#print(x)
#print(y)
#
## test
#size = (0,0)
#
# log
print(a)




# Création de la fenêtre
fenetre = pygame.display.set_mode((a.current_w, a.current_h), RESIZABLE)
dd = a.current_w/2 , a.current_h/2
#size, x, y = (0,0), a.current_w/2, a.current_h/2

# Connaître dimension fenêtre
size = fenetre.get_size()
print(size,x,y)
print(a.current_w/2, a.current_h/2)
pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, x , y ))

# Pour fonction appui long
#pygame.key.set_repeat(400, 30)

intrologo= pygame.image.load(intro).convert()
ecran1=pygame.image.load(ecran1).convert()
neo = pygame.image.load(ecran_jeu).convert()
#fond.fill((0,0,0)) # Remplissage avec du noir 
# Titre fenetre
pygame.display.set_caption(titre_fenetre)

#Rafraîchissement de l'écran
pygame.display.flip()

# Chargement de la playlist
try:
    pygame.mixer_music.load(music1)
    pygame.mixer_music.queue(music2)
    pygame.mixer_music.queue(music3)
    pygame.mixer_music.queue(music4)
    pygame.mixer_music.set_volume(0.8)
except:
    pass


# Chargement des bruitage de jeu
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
clockout = pygame.mixer.Sound(clock)
# Initialise police de charactère
font=pygame.font.Font(None, 29) 
font2=pygame.font.Font(None, 55)
font22=pygame.font.Font(None, 35)
font222=pygame.font.Font(None, 30)
font3=pygame.font.Font(path+'/Quantum.otf', 125)
font4=pygame.font.Font(path+'/Quantum.otf', 81)
font5=pygame.font.Font(path+'/Quantum.otf', 82)
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
    """ Gère la taille de la fenêtre dans un flux parallèle """
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        print('thread ---> OK!')
        # RLock
        with verrou:
           for event in pygame.event.get():   
               if event.type == pygame.VIDEORESIZE: # Redimentionnement de la fenetre
                   size, x, y = event.size, event.w, event.h
                   #fond = pygame.transform.scale(fond, (x, y)) ## SUPER TRANSFORMATION IMAGE
                   print size, x, y
                    
          


class Gestion_Parametres():
    """ Gère les paramètres du jeu """
    def __init__(self):
        self.objet_volume = 1
        if Memoire.indice1 == 0:
            pygame.mixer_music.play()
            # Selection piste
            if Memoire.indice4 == 0:
                pygame.mixer_music.load(music1)
                pygame.mixer_music.play()
            if Memoire.indice4 == 1:
                pygame.mixer_music.load(music2)
                pygame.mixer_music.play()
            if Memoire.indice4 == 2:
                pygame.mixer_music.load(music3)
                pygame.mixer_music.play()
            if Memoire.indice4 == 3:
                pygame.mixer_music.load(music4)
                pygame.mixer_music.play()

            # reglage volume
            if Memoire.indice5 > self.objet_volume:
                vol = Memoire.indice5-self.objet_volume
                supra = Memoire.indice5 * 0.1
                print(supra)
                pygame.mixer_music.stop()
                pygame.mixer_music.set_volume(supra+0.1)
                pygame.mixer_music.play()
                a = pygame.mixer_music.get_volume()
                print("volume:{}".format(str(a)))
            if Memoire.indice5 < self.objet_volume:
                vol = self.objet_volume - Memoire.indice5
                supra = Memoire.indice5 * 0.1
                print(supra)
                pygame.mixer_music.stop()
                pygame.mixer_music.set_volume(supra+0.1) 
                pygame.mixer_music.play()
                a = pygame.mixer_music.get_volume()
                print("volume:{}".format(str(a)))
        if Memoire.indice1 == 1:
            pygame.mixer_music.stop()



class Gestion_Ev_menu():
    """ Gestion des évennement au menu principale """
    c=True
    def __init__(self): 
        """ """
        pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
        obj1=Selecteur()
        self.selection=obj1.selecteur
        for event in pygame.event.get():
        # gestion fenetre
  
            if event.type == pygame.VIDEORESIZE: # Redimentionnement de la fenetre
                size, x, y = event.size, event.w, event.h
        #fond = pygame.transform.scale(fond, (x, y)) ## SUPER TRANSFORMATION IMAGE
                print size, x, y


            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    click.play()
                    Gestion_Ev_menu.c= False
                if event.key == K_ESCAPE:
                    bipp.play()
                    #sys.exit(0)
                if event.key == K_LEFT:
                    print('yo yo LEFT !!')
                    bipp.play()
                    obj1.deplace_moins() 
                    obj1=Selecteur()  
                    self.selection=obj1.selecteur
                if event.key == K_RIGHT:
                    print('yo yo RIGHT !!')
                    bipp.play()
                    obj1.deplace_plus() 
                    obj1=Selecteur() 
                    self.selection=obj1.selecteur
       


class Gestion_Ev_nickname(Gestion_Ev_menu):
    """ Gère l'entrée utilisateur pour le nickname """
    def __init__(self,nickname):
        ## attribut de class definits dans l'objet 
        ## pour être reinitialisé à chaques instances
        Gestion_Ev_nickname.long_nickname = len(nickname)
        Gestion_Ev_nickname.formalite = True
        # variable d'instance
        self.nickname = nickname
        for event in pygame.event.get():
            # Si un de ces événements est de type QUIT
            if event.type == QUIT:     
                Gestion_Ev_nickname.formalite = False

            # Si un de ces éléments est de type clavier
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    Gestion_Ev_nickname.long_nickname = 12
                if event.key == K_BACKSPACE:
                    print("top top")
                    try:
                        if Gestion_Ev_nickname.long_nickname != 0:
                            del self.nickname[-1]
                            Gestion_Ev_nickname.long_nickname -= 1
                            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
                        else:
                            self.nickname= ['nickname: ']
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
#                if event.key == K_a + K_LSHIFT or K_a + K_RSHIFT:
#                    self.nickname.append('A')
#                    Gestion_Ev_nickname.long_nickname += 1
#

class Gestion_Ev_jeux(Gestion_Ev_nickname):
    """ Gère la capture des touches pendant le jeux  """
    def __init__(self,sujet,objA,objet,aaaa,max,destruct,aleph):
       """ """
       self.sujet = sujet
       self.aaaa = aaaa
       self.max = max
       self.destruct = destruct
       self.aleph = aleph
       self.Pause = False
       # Procédure test
       if Memoire.test == True:
           time.sleep(0.1)
           click.play() 
           objA.tetris(sujet.lettre)
           self.sujet = Lettre()
           sujet.lettre = self.sujet.lettre
           print(Lettre.index)
           print(Mot.maximum)
#           if hard == True:
#            sujet.destructiveKomando()
       # On parcours la liste de tous les événements reçus
       for event in pygame.event.get():   
#           if event.type == pygame.VIDEORESIZE: # Redimentionnement de la fenetre
#               size, x, y = event.size, event.w, event.h
#               #fond = pygame.transform.scale(fond, (x, y)) ## SUPER TRANSFORMATION IMAGE
#               print size, x, y


           # Si un de ces éléments est de type clavier
           if event.type == KEYDOWN:       
               # Sortie du jeu
               if event.key == K_ESCAPE:
                   bipp.play()
#                   pygame.mixer_music.stop()
#                   a , b, c, d =  0, 0, 900, 666
#                   pygame.draw.rect(fenetre, BLEU, (a, b, c, d))  
#                   if event.type == KEYDOWN:
#                       if event.key == K_o:
                           # Reinit  de l'index pour detruire le sujet
                   self.sujet.reinit()
                   self.destruct = True
                   self.max = 455
                   self.aleph = True
                   print('ok')
                   Gestion_Ev_menu.c = True
               
               # Pause
               if event.key == K_SPACE:
                   bipp.play()
                   self.Pause = True  

               if event.key == K_a:
                   if 'a' == sujet.lettre:
                       print '** UP **'
                       click.play() 
                       # Methode tetris qui modifie la liste artefact
                       objA.tetris(sujet.lettre)
                       # On passe à la lettre suivante
                       self.sujet = Lettre()    
                       sujet.lettre = self.sujet.lettre 
                       # indice uniquement pour les logs...
                       index = Lettre.index + 1  
                   else:
                       print '** DOWN **'
                       clockout.play()
                       # Retour à zéro à la première erreur
                       if hard == True:
                           sujet.destructiveKomando()

               if event.key == K_b:
                   if 'b' == sujet.lettre:
                       print '** UP **'
                       click.play() 
                       objA.tetris(sujet.lettre) 
                       self.sujet = Lettre()  
                       sujet.lettre = self.sujet.lettre 
                       index = Lettre.index + 1   
                   else:
                       print '** DOWN **'
                       clockout.play()
                       if hard == True:
                           sujet.destructiveKomando()
               if event.key == K_c:
                   if 'c' == sujet.lettre:
                       print '** UP **'
                       click.play() 
                       objA.tetris(sujet.lettre) 
                       self.sujet = Lettre()  
                       sujet.lettre = self.sujet.lettre 
                       index = Lettre.index + 1   
                   else:
                       print '** DOWN **'
                       clockout.play()
                       if hard == True:
                           sujet.destructiveKomando()
               if event.key == K_d:
                   if 'd' == sujet.lettre:
                       print '** UP **'
                       click.play() 
                       objA.tetris(sujet.lettre) 
                       self.sujet = Lettre()  
                       sujet.lettre = self.sujet.lettre 
                       index = Lettre.index + 1   
                   else:
                       print '** DOWN **'
                       clockout.play()
                       if hard == True:
                           sujet.destructiveKomando()          
               if event.key == K_e:
                   if 'e' == sujet.lettre:
                       print '** UP **'
                       click.play() 
                       objA.tetris(sujet.lettre) 
                       self.sujet = Lettre()  
                       sujet.lettre = self.sujet.lettre 
                       index = Lettre.index + 1   
                   else:
                       print '** DOWN **'
                       clockout.play()
                       if hard == True:
                           sujet.destructiveKomando()
               if event.key == K_f:
                   if 'f' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_g:
                   if 'g' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_h:
                   if 'h' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_i:
                   if 'i' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_j:
                   if 'j' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_k:
                   if 'k' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_l:
                   if 'l' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_m:
                   if 'm' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_n:
                   if 'n' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1  
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_o:
                   if 'o' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_p:
                   if 'p' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_q:
                   if 'q' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_r:
                   if 'r' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_s:
                   if 's' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_t:
                   if 't' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_u:
                   if 'u' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_v:
                   if 'v' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_w:
                   if 'w' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_x:
                   if 'x' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_y:
                   if 'y' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1   
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               if event.key == K_z:
                   if 'z' == sujet.lettre:
                        print '** UP **'
                        click.play() 
                        objA.tetris(sujet.lettre) 
                        self.sujet = Lettre()  
                        sujet.lettre = self.sujet.lettre 
                        index = Lettre.index + 1
                   else:
                        print '** DOWN **'
                        clockout.play()
                        if hard == True:
                            sujet.destructiveKomando()
               ### Test si le mot à été trouvé
               if self.sujet.victoire == True:
                   print '** VICTORY !! **'
                   excelent.play() 
                   objet.score_plus() # incrémente le score 
                   objet.score_forme() # je le remet en forme string
                   # Appel de la methode alteration de la class Lettre
                   self.sujet.alteration(suprem=True)                                
                   sample2=self.sujet.sample2
                   text1 = font.render(sample2,2,( 255, 0, 0 ))
                   fenetre.blit(text1, (self.aaaa,self.max))
                   self.max = 455     # On termine la boucle

class Gestion_Ev_config():
    """ Gestion des évennements clavier sur page de configuration """
    unedeplus = True
    c = True
    def __init__(self):
        chaka = Deplacement_config()
        for event in pygame.event.get():  
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    click.play()
                    Gestion_Ev_menu.c = True
                    Gestion_Ev_config.unedeplus = False
                if event.key == K_ESCAPE:
                    bipp.play()
                    Gestion_Ev_menu.c = True 
                    Gestion_Ev_config.unedeplus = False   
                if event.key == K_LEFT:
                    print('yo yo LEFT !!')
                    bipp.play()
                    chaka.deplace_d()
                    Gestion_Parametres()         
                if event.key == K_RIGHT:
                    print('yo yo RIGHT !!')
                    bipp.play()
                    chaka.deplace_g()
                    Gestion_Parametres()         
                if event.key == K_UP:
                    print('yo yo UP !!')
                    bipp.play()
                    chaka.deplace_up()               
                if event.key == K_DOWN:
                    print('yo yo DOWN !!')
                    bipp.play()
                    chaka.deplace_down()
                    Gestion_Parametres()         

class Gestion_Score():
    def __init__(self,objet):
        """ """
        # Création d'un rectangle noir pour le fond
        pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
        pygame.display.flip()
        ecran_reccords=objet.lecture_score()
        babylone=ecran_reccords
        like=200
        score = 'Scores'
        titre = font5.render(score,1,(255,124,5))
        fenetre.blit(titre,(x/1.3,10))
        unedeplus = True
        while unedeplus:
            for event in pygame.event.get():   
                if event.type == KEYDOWN: 
                    if event.key == K_ESCAPE:
                        bipp.play()
                        Gestion_Ev_menu.c = True
                        unedeplus = False
            try:
                for e in babylone:
                    nervure=font.render(e,2,(250,250,0))
                    fenetre.blit(nervure,(x/1.2,like))
                    pygame.display.flip()   
                    click.play()
                    like += 45         
                    time.sleep(0.5)     
                        
            # Si le fichier n'existe pas                       
            except TypeError:
                pass
            time.sleep(10)
            Gestion_Ev_menu.c = True
            unedeplus = False

class Gestion_Credit():
    def __init__(self):
        """ """
        # Création d'un rectangle noir pour le fond
        pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
        pygame.display.flip()
        unedeplus = True
        while unedeplus:
            ether=[]
            with open(path+"/Caglio_credits.txt", "r") as fichier:
                for ligne in fichier:
                    ether.append(ligne)
                    max = 1
                    
                for index, i in enumerate(ether):
                    pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))

                    B=random.randint(0,255)
                    R=random.randint(0,255)
                    G=random.randint(0,255)
                    yin = i.strip()
                    credit = font.render(yin,2,( B, 255, G ))
                    longg= len(ether[index])
                    balthazar=(x)-(longg*5)
                    fenetre.blit(credit, (balthazar,max)) 
                    pygame.display.flip() # Rafraichissement
                    max += 35
                    time.sleep(0.1)
                max = 1    
                for index, i in enumerate(ether):
                    B=random.randint(0,255)
                    R=random.randint(0,255)
                    G=random.randint(0,255)
                    yin = i.strip()
                    credit = font.render(yin,2,( B, 255, G ))
                    longg= len(ether[index])
                    balthazar=(x)-(longg*5)
                    fenetre.blit(credit, (balthazar,max)) 
                    pygame.display.flip() # Rafraichissement
                    max += 35
                    time.sleep(0.5)

                    for event in pygame.event.get():
                        if event.type == KEYDOWN: 
                            if event.key == K_ESCAPE:
                                bipp.play()
                              #  continuer = False
                                unedeplus = False        
                                Gestion_Ev_menu.c = True

class Gestion_Config():
    def __init__(self):
        oulaoups = 29
        unedeplus = True
        while unedeplus:
            # Création d'un rectangle noir pour le fond
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
            tt = Memoire() 
            separateur= " = "
            config = "config"
            x1 = 970
            x2 = 820
            x3 = 1010
            ## Eléments
            separ = font.render(separateur,2,(155,55,123))
            depart = font5.render(config,1,(255,124,5))
            element1 = font.render(Memoire.elem_tab4[0],2,(155,255,5)) # musique
            element2 = font.render(Memoire.elem_tab4[1],2,(155,255,5)) # son
            element3 = font.render(Memoire.elem_tab4[2],2,(155,255,5)) # niveau
            element4 = font.render(Memoire.elem_tab4[3],2,(155,255,5)) # piste
            element5 = font.render(Memoire.elem_tab4[4],2,(155,255,5)) # volume 
            titre = font22.render("Titre: {}".format(Memoire.titre),2,(155,255,5))
            ## Collage des éléments
            fenetre.blit(depart,(x-150,10))
            fenetre.blit(separ,(x1,150))
            fenetre.blit(element1,(x2,150))
            fenetre.blit(separ,(x1,180))
            fenetre.blit(element2,(x2,180))
            fenetre.blit(separ,(x1,210))
            fenetre.blit(element3,(x2,210))
            fenetre.blit(separ,(x1,240)) 
            fenetre.blit(element4,(x2,240))
            fenetre.blit(separ,(x1,270)) 
            fenetre.blit(element5,(x2,270))
            fenetre.blit(titre,(555,555))
            ## Valeur des éléments
            elem_val1 = font.render(tt.musique,2,(35,252,255)) 
            elem_val2 = font.render(tt.son,2,(35,252,255)) 
            elem_val3 = font.render(tt.niveau,2,(35,252,255)) 
            elem_val4 = font.render(tt.piste,2,(35,252,255))
            elem_val5 = font.render(tt.volume,2,(35,252,255))
            fenetre.blit(elem_val1,(x3,150))
            fenetre.blit(elem_val2,(x3,180))
            fenetre.blit(elem_val3,(x3,210))
            fenetre.blit(elem_val4,(x3,240))
            fenetre.blit(elem_val5,(x3,270)) 
            
            Gestion_Ev_config()
            unedeplus = Gestion_Ev_config.unedeplus
            fontx=pygame.font.Font(None, oulaoups) 
            visual1  = ">" 
            visualise = fontx.render(visual1,2,(155,255,5))  
            phidor = Deplacement_config.zulu
            fenetre.blit(visualise,(phidor))
            
            pygame.display.flip()
            oulaoups += 1
            phidor = oulaoups
            time.sleep(0.1)
            if oulaoups > 35:
                oulaoups = 29
        Gestion_Ev_menu.c = True               



class Gestion_Quit():
    def __init__(self):
        """ Gestion du méssage de fin et de la sortie du programme"""
        # Création d'un rectangle noir pour le fond
        pygame.draw.rect(fenetre, NOIR , (0, 0, a.current_w , a.current_h ))
        bye = "A BientOt"
        nb = 0
        nb1 = 1
        while nb < 35:
            pygame.draw.rect(fenetre, NOIR , (0, 0, a.current_w , a.current_h))
            font3=pygame.font.Font(path+'/Quantum.otf', 56+nb)
            depart=font3.render(bye,2,(241,255,68))
            fenetre.blit(depart,((x/2)+nb,y-nb))
            pygame.display.flip()
            nb += 1
               
        time.sleep(0.5)
        sys.exit(0)

class Gestion_jeux(Gestion_Ev_jeux):
    def __init__(self,objet):
        """ Classe principale de gestion du nom du joueur et du déroulement
            de la partie """

        Gestion_Parametres() 
        victoire.play()
        # Ligne de fin de chute des mots
        ligne1 = font.render(ligne,2,( 251, 8, 8 )) 
        score= Score.score
        obj = Lecture() # Lecture du fichier 
        ## Initialisation du capital de points de vie
        supra= Vie_Joueur()
 
        pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1100 ))
        ### Entrée du nom du joueur
        nickname= ['nickname: ']
        pygame.display.flip()
        long_standart=len(nickname[0])
        long_nickname = 0
        formalite = True
        # je limite la longueur du self.nickname 12
        while formalite == True and long_nickname < 12:
            ## Procedure Test
            if Memoire.test == True:
                formalite == False
                long_nickname = 12
            else:    
                ## Appel du gestionnaire d'evennement
                bidule = Gestion_Ev_nickname(nickname)
                formalite = Gestion_Ev_nickname.formalite       
                long_nickname = Gestion_Ev_nickname.long_nickname  
                nickname = bidule.nickname
                pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1000 ))
                stone = font4.render(''.join(bidule.nickname),2,(80,241,0))
                fenetre.blit(stone,(450,350))
                pygame.display.flip()
                
        pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 2000 , 1000 ))
        pygame.draw.rect(fenetre, (156, 175, 175), (550, 0 , 802 , 604 ))
        # Lancement du jeu 
        aleph = False    
        while aleph == False:
            # on cree une instance de la class Mot
            obj = Mot()
            mot = obj.mot           
            # on cree une instance en passant en parametre mot 
            objA = Construction(mot)
            # on affect l'attribut artefact à la variable artefact
            artefact = objA.artefact    
            # on cree une instance, l'objet sera le charactère à trouver 
            sujet = Lettre()      
            lettre = sujet.lettre 
            index = Lettre.index +1 # pour log
            ########### Construction fenetres
            text = font.render(mot,2,( 80, 241, 0 ))
            # Quelque variables de bon cru
            x = 550
            # On tire au hasard le point d'apparition du mot sur l'axe horizontale
            aaaa=random.randint(x,720)  
            objet.score_forme()
            sCore = font.render(str(objet.score_en_forme),2,( 80, 241, 0 ))
            if Memoire.test == True:
                nick = font.render('WordShoot Test',2,(255,162,0))    
            else:    
                nick = font.render(str(''.join(nickname[1:])),2,(255,162,0))    
            vie = font2.render(str(supra.vue_sur_vie_joueur),2,( 120, 94, 246 ))
            ### LOGs
            print "le mot est: {}".format(mot)
            print "la sujet.lettre n°: {} est: {}".format(index , sujet.lettre)
            print "voici l'artefact: {}".format(artefact)
            obj_v=Vitesse()                
            destruct = False
            max=1
            while max < 455 and destruct == False:

                pygame.time.Clock().tick_busy_loop(obj_v.vitesse)
                fenetre.blit(text, (aaaa,max))   # affichage text tombant  
                max +=1   
                # Affectation de la variable d'instance score
                score=Score.score 
                # Appel de la methode alteration de la class Lettre
                sujet.alteration() 
                sample2=sujet.sample2
#                    sample1=self.sujet.sample1
                text1 = font.render(sample2,2,( 255, 0, 0 ))
#                    text2 = font.render(sample1,2,( 255, 0, 0 ))
                fenetre.blit(text1, (aaaa,max))
#                    fenetre.blit(text2, (aaaa,max))
                sauvegarde = False
                # Fin de chute
                if max ==453:    
                    loose.play() 
                    objet.score_forme()
                    sauvegarde = supra.enlev_vie()
                    sujet.reinit()
                    destruct = True
                pygame.display.flip() # Rafraichissement

                # Affichage chaine de charactère contenue dans la liste 'artefact'
                simbad= ''.join(artefact)
                ping = font2.render(simbad,22,( 240, 240, 4 )) 
                fenetre.blit(neo, (x+1,2))
                fenetre.blit(ligne1, (x,450)) 
                fenetre.blit(nick, (x+350,500))     
                fenetre.blit(sCore, (x+700,550))
                fenetre.blit(vie, (x+50,550))
                fenetre.blit(ping,(x+325,550))

                # Clavier virtuel auquel on passe en paramètre la position de la lettres
                Clavier_virtuel()
                # Appel Gestionnaire d'èvennement
                escargot = Gestion_Ev_jeux(sujet,objA,objet,aaaa,max,destruct,aleph)
                # Procedure d'appel de pause pour config
                if escargot.Pause == True:
                    Gestion_Config()
                max = escargot.max
                c = escargot.c
                destruct = escargot.destruct
                aleph = escargot.aleph
                
                # Fin de partie
                if sauvegarde == True:
                    nb=0
                    while nb <= 4:
                        time.sleep(1)
                        nb+=1
                        truc="You Loose T.T" 
                        ecran_sauvegarde=font2.render(truc,2,(80,241,0))
                        fenetre.blit(ecran_sauvegarde,((x+255)+nb,35+nb))
                        pygame.display.flip()
                 
                    nicknamu=''.join(nickname[1:])                          
                    # Vérification si le score est un reccord
                    bidule=objet.verif_reccord(nicknamu)
                    ecran_chouette=font2.render(bidule,2,(80,241,0))
                    fenetre.blit(ecran_chouette,(x+255,400))
                    pygame.display.flip()
                    time.sleep(3)     
                    ## Destruction du score
                    objet=Score()
                    ## Destruction du capitale points
                    supra.reinit_vie()
                    destruct = True 
                    aleph = True
                    Gestion_Ev_menu.c = True
                    # Réinitialisation de la vitesse
                    obj_v.vitesse_reinit()
            # Procédure son_vitesse en fonction de la vitesse (niveau)
            son_vitesse(score, supra)        
            pygame.display.flip() # Rafraichissement


class Clavier_virtuel(Gestion_Ev_jeux):

    def __init__(self, position = 0):
        """ Clavier Virtuel, Accepte en paramètre un nombre entier représentant la position de la lettre
            dans l'alphabet pour mettre en évidence la touche concernée """        
        # un trapeze positionné sous la base de l'ecran supèrieur
        angle = 0.436332

        
        position = Lettre.index
        couleur = VERT
        yoyo = 'a'
        sturm = font.render(yoyo,2,( 80, 241, 0 ))
        # initialisation d'un compteur
        nb_touche = 0 
        nnb = 0
        stupeur = 0
        # initialisation coordonnée de la première touche
        a , b, c, d =  480, 650, 90, 20
        # Construction de la lettre à colorer
        sample1 = Lettre.mot[Lettre.index]               
        # Comparaison de la lettre avec sa position dans la liste
        # alphabeta afin de récup index
        for i,e in enumerate(alphabeta):
            if e == sample1:
                stupeur = i
        # Première rangée de dix touches
        while nb_touche < 10:   
            # Vérification de la prsésence de la lettre dans la sequence
            if nb_touche == stupeur and stupeur < 10:
                couleur = BLEU
            else:
                couleur = VERT     
            # Rectangles
            pygame.draw.rect(fenetre, couleur, (a, b, c, d))    
            # Caractère alphabétique
            lettreAAAA = alphabeta[nb_touche] 
            tic = font222.render(lettreAAAA,2,(ROUGE))
            fenetre.blit(tic,(a+30,b))
            a += 100
            nb_touche +=1
        # Réinitialisation    
        a = 480
        couleur = VERT    
        # Deuxième rangée de dix touches
        while nb_touche < 20:   
            if nb_touche == stupeur and stupeur < 20 and stupeur > 9:
                couleur = BLEU
            else:
                couleur = VERT     
            pygame.draw.rect(fenetre, couleur, (a+10, b+25, c, d))           
            lettreAAAA = alphabeta[nb_touche] 
            tic = font222.render(lettreAAAA,2,(ROUGE))
            fenetre.blit(tic,(a+30,b+25))
            a += 100
            nb_touche +=1

#        nb_touche = 0 
        a = 480
        couleur = VERT   
        # Troisième rangée de dix touches
        while nb_touche < 30:             
            if nb_touche == stupeur and stupeur < 30 and stupeur > 19:
                couleur = BLEU
            else:
                couleur = VERT     
            pygame.draw.rect(fenetre, couleur, (a+20, b+50, c, d))  
            lettreAAAA = alphabeta[nb_touche] 
            tic = font222.render(lettreAAAA,2,(ROUGE))
            fenetre.blit(tic,(a+30,b+50))
            a += 100
            nb_touche +=1
        print(' stupeur: {}'.format(stupeur))   
        print(' sample: {}'.format(sample1))



class Animation_intro():
    def __init__(self):
        """ Animation fondu enchaîné """
        bal.play()
        nb = 0 
        while nb < 200:
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, a.current_w,a.current_h ))
            intrologo.set_alpha(nb)
            pygame.Surface.convert_alpha(intrologo)
            # round() --> arrondir
            center = fenetre.get_rect()
            print(center.center)
            print(x/2,y/2)
            fenetre.blit(intrologo,(x-400,y-290))
            pygame.display.flip()  
            nb += 1
        nb1 = 200    
        while nb1 != 0:
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, a.current_w,a.current_h ))
            intrologo.set_alpha(nb1)
            pygame.Surface.convert_alpha(intrologo)
            fenetre.blit(intrologo,(x-400 , y-290))
            pygame.display.flip()  
            nb1 -= 1
        


class WordShoot():
    """ Pygame - Worshoot - Classe Principale """
    ## Appel du thread pour la gestion de la fenêtre
#    thread1 = Gestion_volumetrik()
#    thread1.run()

    Animation_intro()
    ## Appel de la mémoire du jeu
    musique = Memoire.indice1
    son = Memoire.indice2
    niveau = Memoire.indice3
    piste = Memoire.indice4
    test = Memoire.test 
    
    while continuer:
        pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, a.current_w,a.current_h ))
        ####### Ecran Principale
        c = True
        while c:
            objet=Score() # Construction du score
            ## Appel du gestionnaire d'èvennement
            truc = Gestion_Ev_menu()
            selection = truc.selection
            c = Gestion_Ev_menu.c
            # # # #  
#            x , y = x/2 , y/2 
            ## Ecran de depart
            fenetre.blit(ecran1,(x/2,y/5))
            ## Element du tableau Selecteur 
            select=font22.render(selection,2,( 80, 241, 0 ))
            fenetre.blit(select,(x-50,y+250))
            ## Titre du Jeu
            titre=font3.render(logo1,2,(241,255,68))
            fenetre.blit(titre,(x/2.4,y+100)) 
            pygame.display.flip()
        # Menu jeux          
        if  selection == Selecteur.tableau[0]:      
            Gestion_jeux(objet) 
        # Menu Scores
        if selection == Selecteur.tableau[1]: 
            Gestion_Score(objet)
        # Menu Crédits
        if selection == Selecteur.tableau[2]:
            Gestion_Credit()                        
        # menu config 
        if selection == Selecteur.tableau[3]:
            Gestion_Config()  
        # menu quit 
        if selection == Selecteur.tableau[4]:
            Gestion_Quit()
        # menu Test 
        if selection == Selecteur.tableau[5]:
            Memoire.test = True
            Gestion_jeux(objet)

if __name__ == '__main__':
    WordShoot()
    # terminer le thread
#    thread1.join()
 
