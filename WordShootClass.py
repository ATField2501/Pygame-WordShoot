#!/usr/bin/python2
# coding: utf8 
# auteur: <atfield2501@gmail.com>

""" Module de Pygame-Wordshoot - cagliostro - """


import pickle
import random
from WSconstantes import *




class Score():
    """ Class construisant une chaine de charactère pour afficher 
        le score du joueur Et tenant à jour la page des reccords  """
    score= 0
    def __init__(self):
        Score.score=0
    def score_forme(self):
        self.score_en_forme= str(Score.score) + 'Pts'
    def score_plus(self):
        Score.score += 10
    def score_moins(self):
        Score.score -= 10
    def verif_reccord(self , nicknamu='Neant'):
        try:
            self.mnemo=pickle.load(open(path_shadows,'rb'))
        # Si pas de fichier pickle    
        except IOError:
            nnn= 1
            mnemo={}
            while nnn <= 10:
                mnemo[nnn]=0
                nnn += 1
            self.mnemo=mnemo
            pickle.dump(self.mnemo,open(path_shadows,'wb'))
            pass

        ## Je verifie si le score est plus grand qu'une valeur du dico    
        for keys,value in self.mnemo.items():
            victory=False   
            # j'ecris le score du joueur
            self.ecriture_score(nicknamu, keys)
        # je construis la liste des scores
        self.vrac = pickle.load(open(path_shadows,'rb')) 
        #### snippet MrGecko (tri un dico par valeurs en mode reverse) 
        f = lambda dico : sorted(self.vrac.items(),lambda a,b: cmp(a[1],b[1]),reverse=True)
        ####################   
        tmp=f(self.vrac)  

        # je verifis la présence d'un reccord
        for i,e in tmp:
            if e < Score.score:
                victory = True

        if victory == False:
            bidule='Aucun reccord'
        elif victory == True:
            bidule='Nouveau Reccord'
        return bidule

    def ecriture_score(self, nicknamu , keys):
        self.mnemo=pickle.load(open(path_shadows,'rb'))
        print(self.mnemo)
        # insertion du nouveau reccord
        self.mnemo[nicknamu]=Score.score
        pickle.dump(self.mnemo,open(path_shadows,'wb'))


    def lecture_score(self):
        try:
            self.vrac = pickle.load(open(path_shadows,'rb'))
            print(self.vrac)
            ecran_reccords=[]
            #### snippet MrGecko (tri un dico par valeurs en mode reverse) 
            f = lambda dico : sorted(self.vrac.items(),lambda a,b: cmp(a[1],b[1]),reverse=True)
            ##############################################################   
            tmp=f(self.vrac)  
            nb=1
            # je n'affiche que les dix premiers résultats
            for e in tmp: 
                ecran_reccords.append(str(nb)+' - '+str(e[0])+' - '+str(e[1])+' Pts')
                nb +=1
                if nb == 11:
                    break
            print(ecran_reccords)
#            print(tmp)
        except IOError:
            ecran_reccords=self.verif_reccord()
        return ecran_reccords


class Lecture():
    """ Lecture du fichier pour en extraire les lignes 
        et les incorporées à la liste 'tableau' """
    tableau=[]
    def __init__(self, tableau = []):
        self.tableau = tableau
        with open(path+"/base_text/WS_informatique.txt", "r") as fichier:
            for ligne in fichier:
                self.tableau.append(ligne)
                Lecture.tableau= self.tableau
        self.long = len(tableau)



class Mot(Lecture):
    """  Selection d'un mot au 'hasards' dans la liste 'tableau'  """
    mot=''
    maximum=0
    def __init__(self):
        Mot.mot = random.choice(Lecture.tableau) 
        # suppresion des characteres de fin de lignes(\n)
        Mot.mot = Mot.mot.strip() 
        Mot.maximum = len(Mot.mot) 
        



class Lettre(Mot):
    """ Class renvoyant un objet construit sur le mot à trouver et 
        représentant la lettre à trouver (dans le bon ordre) """ 
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
    def destructiveKomando(self):
        Lettre.index = 0

    def alteration(self, suprem=False):
        """ Methode d'alteration du mot à trouver. 
            Split la chaine pour colorier en rouge la première partie """
        if suprem == True:
            self.sample2 = Mot.mot
        else:
            self.sample1 = Mot.mot[Lettre.index:]
            self.sample2 = Mot.mot[:Lettre.index]



class Construction(Lettre): # Super héritage pour récuperer l'index de la lettre
    """ Class dont le role est de construire une chaine 'artefact' identique 
        à la chaine 'mot' mais dont les charactères sont remplacés par des asterix (*)
        Et aussi de restituer les lettre à 'artefact' pour reconstruire 
        le mot proposé par le joueur."""
    def __init__(self, mot):
        self.artefact = []
        for i in mot:
            self.artefact += '_'  # Construction de la liste 'artefact'
    def tetris(self ,lettre):
        """ Methode reconstruisant artefact en substituant 
            les asterix par la lettre trouvée """
        self.artefact[Lettre.index] = lettre       




class Vitesse(Score):
    """ Class renvoyant un indice de vitesse en fonction du score 
                  ^(;,,;)^ et ia ia Cthulhu...                """
    vitesse=60              
    def __init__(self): 
        if Score.score >= 100:
             Vitesse.vitesse = 100
        if Score.score >= 200:
            Vitesse.vitesse = 149
        if Score.score >= 300:
            Vitesse.vitesse = 200
        if Score.score >= 400:
            Vitesse.vitesse = 300 
        if Score.score >= 500:
            Vitesse.vitesse = 400      
        if Score.score >= 600:
            Vitesse.vitesse = 500  
        self.vitesse = Vitesse.vitesse
    def vitesse_reinit(self):
        Vitesse.vitesse = 60

class Vie_Joueur():
    """ Gestion des points de vie du joueur """
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
    """ Class utilisée pour selectionner l'entrée utilisateur au menu principale."""
    tableau=['  Start','Scores','Credits',' config','   quit', '  Test']
    index = 0
    def __init__(self):
        # En fonction du nombre d'éléments du tableau
        if Selecteur.index > 5:   
            Selecteur.index = 0
        if Selecteur.index < 0:
            Selecteur.index = 5
        self.selecteur = Selecteur.tableau[Selecteur.index]
    def deplace_plus(self):
        """ Methode de modification positive de l'index du selecteur  """
        Selecteur.index += 1
    def deplace_moins(self):
        """ Methode de modification négative de l'index du selecteur  """
        Selecteur.index -= 1

class Deplacement_config():
    """ Déplacement dans la fenêtre de configuration"""
    index = 0
    chakazulu = [(775,145),(775,175),(775,205),(775,235),(775,265)]
    zulu = chakazulu[0]

    def __init__(self):
        """ constructeur """
        self.blade = Memoire()
    def deplace_up(self):
        """ Methode de modification positive de l'index du selecteur  """
        Deplacement_config.index -= 1
        if Deplacement_config.index < 0:
            Deplacement_config.index = 4 
        Deplacement_config.zulu = Deplacement_config.chakazulu[Deplacement_config.index]
    def deplace_down(self):
        """ Methode de modification négative de l'index du selecteur  """
        Deplacement_config.index += 1
        if Deplacement_config.index > 4:
            Deplacement_config.index = 0 
        Deplacement_config.zulu = Deplacement_config.chakazulu[Deplacement_config.index]
    def deplace_d(self):
        self.blade.modificateur_plus() 
    def deplace_g(self):
        self.blade.modificateur_moins() 
 

class Memoire(Deplacement_config):
    """ Garde en mémoire les règlages du jeu """
    # Elements de réglage    
    elem_tab1 = ['1','2','3','4','5','6','7','8','9','10']
    elem_tab2 = ["on","off"]
    elem_tab3 = ["Normal","Difficile"]
    elem_tab4 = ["Musique ","effet audio","Niveau","Piste","volume"]  
    indice1 = 0 # musique
    indice2 = 0 # son
    indice3 = 0 # niveau difficulté
    indice4 = 0 # piste
    indice5 = 0 # volume
    titre = ' (;,,;)'
    # Element test
    test = False
    def __init__(self):
        """ """
        self.index = Deplacement_config.index
        
        # Valeurs des éléments
        self.musique = Memoire.elem_tab2[Memoire.indice1]
        self.son = Memoire.elem_tab2[Memoire.indice2]
        self.niveau = Memoire.elem_tab3[Memoire.indice3]
        self.piste = Memoire.elem_tab1[Memoire.indice4]
        self.volume = Memoire.elem_tab1[Memoire.indice5]
   
    def Test():
        Memoire.test = True

    def maj_index(self):
        """ Gestion depassement d'index """
        # gestion des index
        if Memoire.indice1 > 1:
            Memoire.indice1 = 0
        if Memoire.indice1 < 0:
            Memoire.indice1 = 1 
        if Memoire.indice2 > 1:
            Memoire.indice2 = 0
        if Memoire.indice2 < 0:
            Memoire.indice2 = 1
        if Memoire.indice3 > 1:
            Memoire.indice3 = 0
        if Memoire.indice3 < 0:
            Memoire.indice3 = 1
        if Memoire.indice4 > 3:
            Memoire.indice4 = 0
        if Memoire.indice4 < 0:
            Memoire.indice4 = 3
        if Memoire.indice5 > 9:
            Memoire.indice5 = 0 
        if Memoire.indice5 < 0:
            Memoire.indice5 = 9
        if Memoire.indice4 == 0:
            Memoire.titre = ATF1
        if Memoire.indice4 == 1:
            Memoire.titre = aaa1
        if Memoire.indice4 == 2:
            Memoire.titre = Cets1
        if Memoire.indice4 == 3:
            Memoire.titre = Cets2
        # Pour logs    
        print('indice1 = '+str(self.indice1))
        print('indice2 = '+str(self.indice2))
        print('indice3 = '+str(self.indice3))
        print('indice4 = '+str(self.indice4))
        print('indice5 = '+str(self.indice5))

#        print('musique: '+str(Memoire.musique))
    
    def modificateur_plus(self):        
        print(str(self.index)+'   '+str(Deplacement_config.index))

  
        if Deplacement_config.index == 0: 
            Memoire.indice1 -= 1
        if Deplacement_config.index == 1: 
            Memoire.indice2 -= 1
        if Deplacement_config.index == 2: 
            Memoire.indice3 -= 1
        if Deplacement_config.index == 3: 
            Memoire.indice4 -= 1
        if Deplacement_config.index == 4: 
            Memoire.indice5 -= 1
        self.maj_index()
 
 
    def modificateur_moins(self):
        print(str(self.index)+'   '+str(Deplacement_config.index))       
         # Gestion des valeurs
        if Deplacement_config.index == 0: # musique
            Memoire.indice1 += 1
        if Deplacement_config.index == 1: # son
            Memoire.indice2 += 1
        if Deplacement_config.index == 2: # niveau
            Memoire.indice3 += 1
        if Deplacement_config.index == 3: # piste
            Memoire.indice4 += 1
        if Deplacement_config.index == 4: # volume
            Memoire.indice5 += 1

        self.maj_index()
  
