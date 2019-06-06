#!/usr/bin/python2
# coding: utf8 
# auteur: <atfield2501@gmail.com>

""" Module de Pygame-Wordshoot - cagliostro - """


import pickle
import random 
from WSconstantes import *



class Score():
    """
    Class construisant une chaine de charactère pour afficher le score du joueur
    Et tenant à jour la page des reccords
    """
    score= 0
    def __init__(self):
        """ """
    def score_forme(self):
        self.score_en_forme= str(Score.score) + 'Pts'
    def score_plus(self):
        Score.score += 10
    def score_moins(self):
        Score.score -= 10
    def verif_reccord(self , nickname='Neant'):
        self.nickname=nickname
        try:
            self.mnemo=pickle.load(open(path_shadows,'rb'))
        except IOError:
            nnn= 1
            mnemo={}
            while nnn <= 10:
                mnemo[nnn]=(self.nickname,0)
                nnn += 1
            self.mnemo=mnemo
            pickle.dump(self.mnemo,open(path_shadows,'wb'))
    
        ## Je verifie si le score est plus grand qu'une valeur du dico    
        for keys,value in self.mnemo.items():
            victory=False
            if Score.score > value[1]:
                self.ecriture_score(self.nickname, keys)
                victory=True
            if victory == False:
                bidule='Aucun reccord'
            elif victory == True:
                bidule='Nouveau Reccord'
        return bidule

    def ecriture_score(self, nickname , keys):
        self.mnemo=pickle.load(open(path_shadows,'rb'))
        for i,e in enumerate(self.mnemo):
            self.mnemo[i]=(self.nickname,Score.score)
            break
        pickle.dump(self.mnemo,open(path_shadows,'wb'))

    def lecture_score(self):
        try:
            self.vrac = pickle.load(open(path_shadows,'rb'))
            ecran_reccords=[]
            for keys,values in self.vrac.items(): 
                ecran_reccords.append(str(keys)+' - '+str(values)+'Pts')
            return ecran_reccords
        except IOError:
            ecran_reccords=self.verif_reccord()
            return ecran_reccords


class Lecture():
    """
    Class lisant un fichier pour en extraire les lignes 
    et les incorporer à la liste 'tableau'
    """
    tableau=[]
    def __init__(self, tableau = []):
        self.tableau = tableau
        with open(path+"base_text/WS_informatique.txt", "r") as fichier:
            for ligne in fichier:
                self.tableau.append(ligne)
                Lecture.tableau= self.tableau
        self.long = len(tableau)



class Mot(Lecture):
    """
    Class ayant la charge de selectionner un mot au 'hasards' dans la liste 'tableau' 
    """
    mot=''
    maximum=0
    def __init__(self):
        Mot.mot = random.choice(Lecture.tableau) ######### Super methode random
        Mot.mot = Mot.mot.strip() # suppresion des characteres de fin de lignes(\n)
        Mot.maximum = len(Mot.mot) 
        


class Lettre(Mot):
    """
    Class renvoyant un objet construit sur le mot à trouver et représentant la lettre à trouver (dans le bon ordre) 
    """ 
    # index a -1 pour demarrer à zéro 
    index= -1                               
    def __init__(self):                     
        self.victoire = False               
        Lettre.index += 1
        if Lettre.index == Mot.maximum:
            Lettre.index= -1
            self.victoire=True
        # Valeur contenue dans la liste mot à l'index deffinie 
        self.lettre = Mot.mot[Lettre.index]
    def reinit(self):
        """ Methode de réinitialisation de l'index """
        Lettre.index = -1

    def alteration(self):
        """  Methode d'alteration du mot à trouver. Split la chaine pour colorier en rouge la première partie """
        self.sample1 = Mot.mot[Lettre.index:]
        self.sample2 = Mot.mot[:Lettre.index]

class Construction(Lettre): # Super héritage pour récuperer facilement l'index de la lettre
    """
    Class dont le role est de construire une chaine 'artefact' identique à la chaine 'mot' mais dont les charactères sont remplacés par des asterix (*)
    Et aussi de restituer les lettre à 'artefact' pour reconstruire le mot proposé par le joueur.
    """
    def __init__(self, mot):
        self.artefact = []
        for i in mot:
            self.artefact += '_'  # Construction de la liste 'artefact'
    def tetris(self ,lettre):
        """ Methode reconstruisant artefact en substituant les asterix par la lettre trouvée"""
        self.artefact[Lettre.index] = lettre       


class Vitesse(Score):
    """
    Class renvoyant un indice de vitesse en fonction du score ^(;,,;)^ et ia ia Cthulhu...
    """
    def __init__(self):
        
        if Score.score < 100:
            self.vitesse= 40
        if Score.score >= 100:
             self.vitesse = 60
        if Score.score >= 200:
            self.vitesse = 70
        if Score.score >= 300:
            self.vitesse = 80 
        if Score.score >= 400:
            self.vitesse = 90 
        if Score.score >= 500:
            self.vitesse = 100      
        if Score.score >= 600:
            self.vitesse = 110  
       



class Vie_Joueur():
    vie_joueur=3
    def __init__(self):
        self.vue_sur_vie_joueur='* '*Vie_Joueur.vie_joueur
        
    def add_vie(self):
        """ Ajoute une vie au total du joueur"""
        Vie_Joueur.vie_joueur += 1
        self.vue_sur_vie_joueur='* '*Vie_Joueur.vie_joueur     
    def enlev_vie(self):
        """ Enlève une vie au total du joueur"""
        Vie_Joueur.vie_joueur -= 1
        if Vie_Joueur.vie_joueur <= 0:
            self.vue_sur_vie_joueur=looser
            sauvegarde = True
            return sauvegarde
        else:    
            self.vue_sur_vie_joueur='* '*Vie_Joueur.vie_joueur
    def reinit_vie(self):
        """ Réinitialise le nombre de vie """
        Vie_Joueur.vie_joueur=3



class Selecteur():
    """
    Class utilisée pour selectionner l'entrée utilisateur au menu principale.
    """
    tableau=['Start','Scores','Credits']
    index = 0
    def __init__(self):
        # En fonction du nombre d'éléments du tableau
        if Selecteur.index > 2:   
            Selecteur.index = 0
        if Selecteur.index < 0:
            Selecteur.index = 2
        self.selecteur = Selecteur.tableau[Selecteur.index]
    def deplace_plus(self):
        """ Methode de modification positive de l'index du selecteur  """
        Selecteur.index += 1
    def deplace_moins(self):
        """ Methode de modification négative de l'index du selecteur  """
        Selecteur.index -= 1



