#!/usr/bin/python2
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>

import random 
from WSconstantes import *


########### Class


class Score():
    """
    Class construisant une chaine de charactère pour afficher le score du joueur
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

class Lecture():
    """
    Class lisant un fichier pour en extraire les lignes et les incorporer à la liste 'tableau'
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
    index= -1                               # index a -1 pour demarrer à zéro lors de l'instanciation de l'objet
    def __init__(self):                     # appel de la méthode constructeur
        self.victoire = False               # initialisation de la variable d'instance victoire à false
        Lettre.index += 1
        if Lettre.index == Mot.maximum:
            Lettre.index= -1
            self.victoire=True
        self.lettre = Mot.mot[Lettre.index]# Valeur contenue dans la liste mot à l'index deffinie affécté à la var d'instance lettre 

    def reinit(self):
        """ Methode de réinitialisation de l'index """
        Lettre.index = -1

    def alteration(self):
        """  Methode d'alteration du mot à trouver. Split la chaine pour colorier en rouge la première partie """
        self.sample1 = Mot.mot[Lettre.index:]
        self.sample2 = Mot.mot[:Lettre.index]

class Construction(Lettre):  ### Super héritage pour récuperer facilement l'index de la lettre
    """
    Class dont le role est de construire une chaine 'artefact' identique à la chaine 'mot' mais dont les charactères sont remplacés par des asterix (*)
    Et aussi de restituer les lettre à 'artefact' pour reconstruire le mot proposé par le joueur.
    """
    def __init__(self, mot):
        self.artefact = []
        for i in mot:
            self.artefact += '*'  # Construction de la liste 'artefact'
    def tetris(self ,lettre):
        """ Methode reconstruisant artefact en substituant les asterix par la lettre trouvée"""
        self.artefact[Lettre.index] = lettre       


class Vitesse(Score):
    """
    Class renvoyant un indice de vitesse en fonction du score ^(;,,;)^ et ia ia Cthulhu...
    """
    vitesse=40
    def __init__(self):
        if Score.score < 100:
            self.vitesse = Vitesse.vitesse        
        elif Score.score >= 100:
            self.vitesse = 80
        elif Score.score >= 200:
            self.vitesse = 125 
        elif Score.score >= 300:
            self.vitesse = 150 
        elif Score.score >= 400:
            self.vitesse = 200 
        elif Score.score >= 500:
            self.vitesse = 250      
        elif Score.score >= 600:
            self.vitesse = 300  


class Selecteur():
    """
    Class utilisée pour selectionner l'entrée utilisateur au menu principale.
    """
    tableau=['Start','Scores','Credits']
    index = 0
    def __init__(self):
        if Selecteur.index > 2:   ## En fonction du nombre d'éléments du tableau
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



