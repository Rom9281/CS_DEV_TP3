#   CPE Lyon - 3ETI

#   Auteurs : Lucas ROTH | Romain GAUD

#   Date : 1/5/2021

#   Matiere : CS DEV

#   TP : 3

#   Objectif : Creer une classe qui permet d'afficher le jeu grace a TKinter et aussi gerer les evenements tels que les collisions...

import tkinter as tk
from alien import alien
from vaisseau import vaisseau
from projectile import projectile
from block import block
import random

class gui():
    def __init__(self):
        self.__main = ""                                #Definition de la fenetre principale
        self.__main_len = "1600"                        #longueur de la fenetre
        self.__main_hei = "900"                        #largeur de la fenetre

        #REGLAGES JEU
        self.__coeff_aleatoire = 150;                   #Regler ici la probabilite qu'un alien tire ex si = 10, l'alien a 1 chance sur 10 de tirer
        self.__mode_dur = False;                        #Activation du mode dur: il y a maintenant une probabilite que le tir ami se declanche
        self.__coeff_joueur = 2;                        #Probabilite que le tir se declanche    

        self.__limite_aliens = 30                       #Limite pour laquelle le jeu est perdu si l'alien la franchit: se calcule par Lim = Hauteur_Cadre - ce_coeff
        self.__score = 0                                #Definition du score
        self.__vies = 3                                 #Definition du nombre de vies
        self.__vies_label= ""                           #Definition du label ou est inscrit la vie
        self.__score_label = ""

        #CANVAS
        self.__canvas = ""                              #Defintion de la variable du canvas
        self.__canvas_len = "1400"                      #Definition de la longueur du canvas
        self.__canvas_hei = "700"                       #Definition de la hauteur du canvas

        self.__nombre_aliens = 8                       #Nombre d'aliens par lignes
        self.__nb_al_dep = 2*self.__nombre_aliens

        #Creation des dictionaires des esprits des aliens
        
        self.__aliens_att={}                            #Dictionnaire contennat tout les aliens d'attaque(peuvent tirer)
        self.__aliens_def={}                            #Dictionnaire contennat tout les aliens de defense (ne peuvent pas tirer)
        
        #Creation des dictionaires contenant les corps des aliens (corps au sens d'objets canvas)
        self.__corps_aliens_att={}
        self.__corps_aliens_def={}

        self.__proj_suppr = []                          #Les id des projectiles a supprimer
        self.__al_att_suppr = []                        #Les id des aliens d'attques a supprimer
        self.__al_def_suppr = []                        #Les id des aliens de def a supprimer
        self.__id_bl_suppr = []

        #Creation des dictionaires contenant les corps des aliens (corps au sens d'objets canvas)
        self.__nb_blocks = 25
        self.__blocks = {}
        self.__corps_blocks={}

        self.__coeff_block_inv = 3                      #Chance que le bloc soit invinsible

        #Hauteur des blocks
        self.__block_hei = 50

        #Definit la position y des blocks
        self.__y1_bl = int(self.__canvas_hei) - 100 - self.__block_hei
        self.__y2_bl = int(self.__canvas_hei) - 100

        #Creation des caracteristiques du vaisseau
        self.__vaisseau = vaisseau(self.__canvas_len,self.__canvas_hei)
        self.__corps_vaisseau = ""

        #Dictionaires des projectiles et de leur corps (obj canvas)
        self.__projectiles = {}
        self.__corps_projectiles = {}

        #Lancement du programme
        self.AfficherFenetre()

    
    def AfficherFenetre(self):
        """Commande d'affichage de la fentetre"""
        self.__main = tk.Tk()

        self.__main.geometry(self.__main_len+"x"+self.__main_hei)       #Definit la geometrie de la fenetre   

        #Ici le canvas

        self.__canvas = tk.Canvas(self.__main, width = self.__canvas_len, height = self.__canvas_hei, bg = "black")
        self.__canvas.pack()

        self.GenererAliens()                 #Genere les aliens
        self.GenererVaisseau()               #Genere le vaisseau
        self.GenererBlocks()

        #Lie les touches du clavier au canvas:
        self.__main.bind("<Left>", self.__vaisseau.MoveLeft)
        self.__main.bind("<Right>", self.__vaisseau.MoveRight)
        self.__main.bind("<KeyRelease-space>", self.GenererTirAmi)      

        #Ici la zone de score
        self.__score_label=tk.Label(self.__main , text="Score : "+ str(self.__score) )
        self.__score_label.pack(side=tk.RIGHT)

        #ici la zone de vie
        self.__vies_label=tk.Label(self.__main , text = "Vies : "+ str(self.__vies))
        self.__vies_label.pack(side=tk.RIGHT)

        #ici le bouton quitter

        bouton1 = tk.Button(self.__main , text='Quitter',command=self.quitter)
        bouton1.pack()

        #Ici le bouton demarer

        bouton2 = tk.Button(self.__main , text='Rejouer' , command=self.rejouer)
        bouton2.pack()

        #Permet de deplacer les objets
        

        #permet d'actualiser les positions
        self.deplacer()
        self.__main.mainloop()
    
    def deplacer(self):
        """Permet de deplacer les differents objects et de mettre a jour le texte"""
        #______________________________________________________________________

        #Mise a jour du nombre de vies et du score
        nb_aliens = len(self.__aliens_att) + len(self.__aliens_def)
        self.__score = abs(nb_aliens - self.__nb_al_dep)*100
        self.__vies_label['text'] = "Vies : " + str(self.__vies)
        self.__score_label['text'] = "Score : " + str(self.__score)

        if self.VerifCoord():                                                   #Si les coordonnes sont correctes, alors permet a l'esprit de dicter au corps comment bouger

            self.SupprimerMorts()                                               #Permet de supprimer les objets detruits
            
            #Mettre ici la fonctionn qui permet de modifier les coordonnes
            for id in self.__aliens_att.keys():
                self.__aliens_att[id].ModifierCoord()
            for id in self.__aliens_def.keys():
                self.__aliens_def[id].ModifierCoord()


            #Mettre ici les fonctions qui permettent a l'alien de tirer
            for id in self.__aliens_att.keys():
                self.__random = random.randint(0,self.__coeff_aleatoire)        #Genere un nombre aleatoire permettant de savoir si l'alien va tirer
                if self.__random == 1:
                    x,y = self.__aliens_att[id].CalculerCentre()
                    self.GenererProjectile(False,x,y,'red')


            #Mettre ici la modification de l'objet du canvas
            #_______________________________________________

            #Deplacement des aliens d'attaques
            for id in self.__aliens_att.keys():
                self.__canvas.coords(self.__corps_aliens_att[id],self.__aliens_att[id].Getx1(),self.__aliens_att[id].Gety1(),self.__aliens_att[id].Getx2(),self.__aliens_att[id].Gety2()) 
            
            #Deplacement des aaliens de defense
            for id in self.__aliens_def.keys():
                self.__canvas.coords(self.__corps_aliens_def[id],self.__aliens_def[id].Getx1(),self.__aliens_def[id].Gety1(),self.__aliens_def[id].Getx2(),self.__aliens_def[id].Gety2()) 

            #Deplacement du vaisseau
            self.__canvas.coords(self.__corps_vaisseau,self.__vaisseau.Getx1(),self.__vaisseau.Gety1(),self.__vaisseau.Getx2(),self.__vaisseau.Gety2())  
            
            #Deplacement du projectile
            if self.__projectiles != {}:
                for id in self.__projectiles.keys():
                    self.__projectiles[id].ModifierCoord()  #Possible erreur ici due a une mauvaise mise a jour des coordonnes
                    self.__canvas.coords(self.__corps_projectiles[id],self.__projectiles[id].Getx1(),self.__projectiles[id].Gety1(),self.__projectiles[id].Getx2(),self.__projectiles[id].Gety2())
        
            #Realiser les deplacements
            self.__main.after(10, self.deplacer)


    #Mettre ici les fonctions afficher
    #______________________
    def GenererBlocks(self):
    
        '''Genere les blocks de defense'''
        #_________________________________

        for i in range(self.__nb_blocks):
            posX1 = (int(self.__canvas_len)/self.__nb_blocks)*i
            posX2 = (int(self.__canvas_len)/self.__nb_blocks)*(i+1)

            self.__random = random.randint(0,self.__coeff_block_inv)        #Genere un nombre aleatoire permettant de savoir si l'alien va tirer
            if self.__random == 1:
                invincible = True
                color = 'brown'
            else:
                invincible = False
                color = 'yellow'

            block1 = block(posX1,self.__y1_bl,posX2,self.__y2_bl,invincible,color)
            corps_block = self.__canvas.create_rectangle(block1.Getx1(),block1.Gety1(),block1.Getx2(),block1.Gety2(),fill = block1.GetColor())
            
            #Genere l'identite du block
            id_blc = self.GenererId(self.__blocks)

            #Ajoute le blocks aux dictionaires
            self.__blocks[id_blc] = block1
            self.__corps_blocks[id_blc] = corps_block

    def GenererAliens(self):

        '''Genere les aliens de defense et d'attaque'''
        #______________________________________________

        #Etablit les positions de l'axe y ou ils commencent:
        y1_att = 0
        y2_att = 50

        y1_def = 100
        y2_def = 150

        for i in range(self.__nombre_aliens):

            #Etablit les limites des cadres dans lequelles les aliens peuvent circuler
            mini = (int(self.__canvas_len)/self.__nombre_aliens)*i
            maxi = (int(self.__canvas_len)/self.__nombre_aliens)*(i+1)

            xinf = mini + (maxi-mini)/3         #Position initiale du point x1
            xsup = mini + ((maxi-mini)*2)/3     #Position intitale du point x2

            #Genere l'esprit de l'alien
            alien_att = alien(self.__canvas_len,self.__canvas_hei,xinf,y1_att,xsup,y2_att,"pink",mini,maxi)
            alien_def = alien(self.__canvas_len,self.__canvas_hei,xinf,y1_def,xsup,y2_def,"green",mini,maxi)

            #Genere le corps de l'alien
            corps_alien_def = self.__canvas.create_rectangle(alien_def.Getx1(),alien_def.Gety1(),alien_def.Getx2(),alien_def.Gety2(), fill = alien_def.GetColor())
            corps_alien_att = self.__canvas.create_rectangle(alien_att.Getx1(),alien_att.Gety1(),alien_att.Getx2(),alien_att.Gety2(), fill = alien_att.GetColor())
            
            id_att = self.GenererId(self.__aliens_att)
            id_def = self.GenererId(self.__aliens_def)

            #Ajoute les differents aliens au dictionnaire des aliens
            self.__aliens_def[id_def] = alien_def
            self.__aliens_att[id_att] = alien_att

            #Ajoute les corps des differents aliens au dictionnaire des corps d'aliens
            self.__corps_aliens_att[id_att] = corps_alien_att
            self.__corps_aliens_def[id_def] = corps_alien_def

    def GenererVaisseau(self):
        """Genere le corps du vaisseau"""
        #________________________________

        self.__corps_vaisseau = self.__canvas.create_rectangle(self.__vaisseau.Getx1(),self.__vaisseau.Gety1(),self.__vaisseau.Getx2(),self.__vaisseau.Gety2(), fill=self.__vaisseau.GetColor())
    

    def GenererProjectile(self,tir_ami,x,y,color):
        """Genere les differentes composantes d'un projectile"""
        #_______________________________________________________

        #Genere un projectile sur le canvas
        projectile1 = projectile(self.__canvas_len,self.__canvas_hei,x,y, tir_ami,color)
        corps_projectile = self.__canvas.create_rectangle(projectile1.Getx1(),projectile1.Gety1(),projectile1.Getx2(),projectile1.Gety2(), fill=projectile1.GetColor())
        
        id_proj = self.GenererId(self.__projectiles)                                            #Genere l'id du projectile
        
        self.__projectiles[id_proj] = projectile1                                               #Ajoute l'esprit du projectile
        
        self.__corps_projectiles[id_proj] = corps_projectile   #Ajoute les corps du projectile
    
    def GenererTirAmi(self,event):

        """Evenement ou il y a un projetile amis"""
        if self.__mode_dur:
            self.__random = random.randint(0,self.__coeff_joueur)        #Genere un nombre aleatoire permettant de savoir si l'alien va tirer
            if self.__random == 1:
                x,y = self.__vaisseau.GetCentre()
                self.GenererProjectile(True,x,y,'green')
        else:
            x,y = self.__vaisseau.GetCentre()
            self.GenererProjectile(True,x,y,'green')

    

    #Mettre ici les fonction creant l'indentite de l'objet
    #_____________________________________________________

    def GenererId(self, dictionaire):

        """Genere une identite pour les projectiles, les aliens"""

        Boucle = True

        while Boucle:
            rand = random.randint(0,1000000)
            if rand not in dictionaire.keys():
                Boucle = False
                return rand

    #Mettre ici les fonction detruisant les objets
    #_____________________________________________


    def SupprimerProjectile(self,identite):
        self.__canvas.delete(self.__corps_projectiles[identite])        #On supprime d'abord le coprs du projectile de la carte
        self.__corps_projectiles.pop(identite)                          #On supprime ensuite son corps du dictionaire des corps
        self.__projectiles.pop(identite)                                #On supprime enfin son esprit du dictionaire des esprits
        
        #___AUTRE OPTION___
        #projectile.Detruire()
        #self.__canvas.itemconfigure(self.__corps_projectiles[i], state = "hidden")

    def SupprimerAlienAtt(self,identite):
        self.__canvas.delete(self.__corps_aliens_att[identite])
        self.__corps_aliens_att.pop(identite)
        self.__aliens_att.pop(identite)
    
    def SupprimerAlienDef(self,identite):
        self.__canvas.delete(self.__corps_aliens_def[identite])
        self.__corps_aliens_def.pop(identite)
        self.__aliens_def.pop(identite)

    def SupprimerBlock(self,identite):
        self.__canvas.delete(self.__corps_blocks[identite])
        self.__corps_blocks.pop(identite)
        self.__blocks.pop(identite)
    
    def SupprimerMorts(self):
        """Permet de supprimer les elements apres la verification de chacun d'entre eux"""
        #_________________________________________________________________________________
        #print(self.__proj_suppr,self.__al_att_suppr,self.__al_def_suppr)
        if self.__al_att_suppr != []:
            for id_al in self.__al_att_suppr:
                self.SupprimerAlienAtt(id_al)
            self.__al_att_suppr = []

        if self.__al_def_suppr != []:
            for id_al in self.__al_def_suppr:
                self.SupprimerAlienDef(id_al)
            self.__al_def_suppr = []

        if self.__proj_suppr != []:
            for id_proj in self.__proj_suppr:
                self.SupprimerProjectile(id_proj)
            self.__proj_suppr = []
        
        if self.__id_bl_suppr != []:
            for id_bl in self.__id_bl_suppr:
                self.SupprimerBlock(id_bl)
            self.__id_bl_suppr = []

    #Fonction de verification des coordonnes: Permet de savoir si c'est perdu
    #________________________________________________________________________

    def VerifCoord(self):

        if self.VerifGagne():   #Si on detruit tout les aliens on arrete le jeu
            self.__canvas.create_text(int(self.__canvas_len)/2,int(self.__canvas_hei)/2,fill="gold",font="Times 50 italic bold",text="Winner")
            return False
        elif self.VerifPositionAlien():
            self.__canvas.create_text(int(self.__canvas_len)/2,int(self.__canvas_hei)/2,fill="red",font="Times 50 italic bold",text="PERDU")
            return False
        elif self.__projectiles != {}:
            for id in self.__projectiles.keys():                                                #Appelle les identites de tous les projectiles
                if self.__projectiles[id].GetEtat():                                            #Si le projectile n'est pas sorti de la fenetre
                    x,y = self.__projectiles[id].CalculerCentre()

                    if self.__projectiles[id].GetEkip():                                        #Si le projectile est un tir ami

                        for id_al in self.__aliens_att.keys():                                  #Verifie si le tir touche un alien de defense
                            if self.__aliens_att[id_al].IsColliding(self.__projectiles[id].GetPoints()):
                                if id_al not in self.__al_att_suppr:
                                    self.__al_att_suppr.append(id_al)     
                                if id not in self.__proj_suppr:
                                    self.__proj_suppr.append(id) 
                        
                        for id_al in self.__aliens_def.keys():                                 #Verifie si le tir touche un alien de defense
                            if self.__aliens_def[id_al].IsColliding(self.__projectiles[id].GetPoints()):
                                if id_al not in self.__al_def_suppr:
                                    self.__al_def_suppr.append(id_al)
                                if id not in self.__proj_suppr:
                                    self.__proj_suppr.append(id) 

                    else:                                                                       #Sinon le tir est ennemis

                        for id_bl in self.__blocks.keys():
                            
                            if self.__blocks[id_bl].IsColliding(self.__projectiles[id].GetPoints()):
                                if not self.__blocks[id_bl].IsInvincible():
                                    if id_bl not in self.__id_bl_suppr:
                                        self.__id_bl_suppr.append(id_bl)
                                if id not in self.__proj_suppr:
                                    self.__proj_suppr.append(id) 
                        
                        #Verifie si le vaisseau est touche par un projectile
                        if self.__vaisseau.IsColliding(self.__projectiles[id].GetPoints()):     #Si est dans la zone du vaisseau
                            if self.__vies > 0:                                                 #Si le vaisseau a assez de vies le jeu continue
                                self.__vies += -1
                                if id not in self.__proj_suppr:
                                    self.__proj_suppr.append(id)

                            else:                                                                #Si le vaisseau n'as plus de vie, arreter le jeu et afficher perdu
                                #Ecriture du message perdu
                                self.__canvas.create_text(int(self.__canvas_len)/2,int(self.__canvas_hei)/2,fill="red",font="Times 50 italic bold",text="PERDU")
                                
                                return False                                                     #Arrete le jeu
                else:
                    if id not in self.__proj_suppr:
                        self.__proj_suppr.append(id)                                            #Si le projectile sort de la fenetre
            return True                                                                         #SI la verfication a ete faite et rien n'est mauvais, alors proceder
        else:
            return True
    
    def VerifPositionAlien(self):
        """Permet de savoir si l'alien a depasse la position autorisee"""

        for id_al in self.__aliens_att.keys():
            if self.__aliens_att[id_al].Gety2() >= (int(self.__canvas_hei) - self.__limite_aliens):
                return True                                                           #Si un alien depasse la limite return True
        for id_al in self.__aliens_def.keys():
            if self.__aliens_def[id_al].Gety2() >= (int(self.__canvas_hei) - self.__limite_aliens):
                return True 
        return False

    
    def VerifGagne(self):
        """Permet de savoir si le joueur a gagne"""

        if self.__aliens_att == {} and self.__aliens_def == {}:
            return True
        else:
            return False

    def rejouer(self):
        """Permet de relancer une partie"""
        self.__main.destroy()
        self.__init__()
        self.AfficherFenetre()
    
    def quitter(self):
        """Permet de quitter le jeu"""
        self.__canvas.delete("all")
        self.__main.destroy()
        exit()
