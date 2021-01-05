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
import random

class gui():
    def __init__(self):
        self.__main = ""    #Definition de la fenetre principale
        self.__main_len = "1000"    #longueur de la fenetre
        self.__main_hei = "1000"    #largeur de la fenetre

        self.__coeff_aleatoire = 100; #Regler ici la probabilite qu'un alien tire ex si = 10, l'alien a 1 chance sur 10 de tirer

        self.__score = 0    #Definition du score
        self.__vies = 3
        self.__vies_label= ""

        self.__canvas = ""  #Defintion du canvas
        self.__canvas_len = "700"   #Definition de la longueur du canvas
        self.__canvas_hei = "700"   #Definition de la hauteur du canvas

        self.__nombre_aliens = 5    #Nombre d'aliens par colonnes

        #Creation des caracteristiques de l'alien
        

        self.__aliens_att=[]
        self.__aliens_deff=[]

        self.__corps_aliens_att=[]
        self.__corps_aliens_deff=[]


        #Creation des caracteristiques du vaisseau
        self.__vaisseau = vaisseau(self.__canvas_len,self.__canvas_hei)
        self.__corps_vaisseau = ""

        self.__projectile = ""
        self.__corps_projectile = ""
        self.__projectiles = []
        self.__corps_projectiles = []

    

    def AfficherFenetre(self):
        self.__main = tk.Tk()

        self.__main.geometry(self.__main_len+"x"+self.__main_hei)

        
        #Ici le canvas

        self.__canvas = tk.Canvas(self.__main, width = self.__canvas_len, height = self.__canvas_hei, bg = "black")
        self.__canvas.pack()

        self.GenererAliens()     #Genere les aliens
        self.GenererVaisseau()  #Genere le vaisseau

        #Lie les touches du clavier au canvas:
        self.__main.bind("<Left>", self.__vaisseau.MoveLeft)
        self.__main.bind("<Right>", self.__vaisseau.MoveRight)
        self.__main.bind("<space>", self.GenererTirAmi)      

        #Ici la zone de score
        score=0
        Score=tk.Label(self.__main , text="Score : "+ str(score) )
        Score.pack(side=tk.RIGHT)

        #ici la zone de vie
        self.__vies_label=tk.Label(self.__main , text = "Vies : "+ str(self.__vies))
        self.__vies_label.pack(side=tk.RIGHT)

        #ici le bouton quitter

        bouton1 = tk.Button(self.__main , text='Quitter',command=self.__main.quit)
        bouton1.pack()

        #Ici le bouton demarer

        bouton2 = tk.Button(self.__main , text='Play' )
        bouton2.pack()


        #Permet de deplacer les objets
        

        #permet d'actualiser les positions
        self.deplacer()
        self.__main.mainloop()
    
    def deplacer(self):
        #Permet de deplacer les differents objects et de mettre a jour le texte
        #______________________________________________________________________

        #Mise a jour du nombre de vies
        self.__vies_label['text'] = "Vies : " + str(self.__vies) 


        #Verifie si le projectile existe, et si il est rentre en collisionle detruit
        if self.VerifCoord():
            for i,projectile in enumerate(self.__projectiles):
                if projectile != "":
                    if not projectile.GetEtat():
                        self.SupprimerProjectile(projectile,i)
            
            #Mettre ici la fonctionn qui permet de modifier les coordonnes
            self.__alienAtt.ModifierCoord()
            self.__alienDeff.ModifierCoord()

            #Mettre ici les fonctions qui permettent a l'alien de tirer
            if self.__projectile == "":
                self.__random = random.randint(0,self.__coeff_aleatoire)
                if self.__random == 1:
                    x,y = self.__alienAtt.CalculerCentre()
                    self.GenererProjectile(False,x,y)

            #Mettre ici la modification de l'objet du canvas
            #_______________________________________________

            #Deplacement de l'alien
            self.__canvas.coords(self.__corps_alienAtt,self.__alienAtt.Getx1(),self.__alienAtt.Gety1(),self.__alienAtt.Getx2(),self.__alienAtt.Gety2()) 
            self.__canvas.coords(self.__corps_alienDeff,self.__alienDeff.Getx1(),self.__alienDeff.Gety1(),self.__alienDeff.Getx2(),self.__alienDeff.Gety2()) 

            #Deplacement du vaisseau
            self.__canvas.coords(self.__corps_vaisseau,self.__vaisseau.Getx1(),self.__vaisseau.Gety1(),self.__vaisseau.Getx2(),self.__vaisseau.Gety2())  
            
            #Deplacement du projectile
            for i,projectile in enumerate(self.__projectiles):
                    projectile.ModifierCoord()  #Possible erreur ici due a une mauvaise mise a jour des coordonnes
                    self.__canvas.coords(self.__corps_projectiles[i],projectile.Getx1(),projectile.Gety1(),projectile.Getx2(),projectile.Gety2())
                
        
        #Realiser les deplacements
        self.__main.after(20, self.deplacer)


    #Mettre ici les fonctions afficher
    #______________________

    def GenererAlien(self):

        '''Genere les aliens de defense et d'attaque'''
        #______________________________________________

        #Etablit les positions de l'axe y ou ils commencent:
        y1_att = 100
        y2_att = 200

        y1_def = 300
        y2_def = 400

        for i in range(self.__nombre_aliens):

            #Etablit les limites des cadres dans lequelles les aliens peuvent circuler

            mini = (self.__canvas_len/self.__nombre_aliens)*i
            maxi = (self.__canvas_len/self.__nombre_aliens)*(i+1)

            xinf = mini + (maxi-mini)/3 #Position initiale du point x1
            xsup = mini + ((maxi-mini)*2)/3


            alien_att = alien(self.__canvas_len,self.__canvas_hei,xinf,y1_def,xsup,200,"pink",mini,maxi)
            alien_deff = alien(self.__canvas_len,self.__canvas_hei,xinf,y1_def,xsup,y2_def,"green",mini,maxi)

            corps_alienDeff = self.__canvas.create_rectangle(alien_deff.Getx1(),alien_deff.Gety1(),alien_deff.Getx2(),alien_deff.Gety2(), fill = alien_deff.GetColor())
            corps_alienAtt = self.__canvas.create_rectangle(alien_att.Getx1(),alien_att.Gety1(),alien_att.Getx2(),alien_att.Gety2(), fill = alien_att.GetColor())

    def GenererVaisseau(self):
        self.__corps_vaisseau = self.__canvas.create_rectangle(self.__vaisseau.Getx1(),self.__vaisseau.Gety1(),self.__vaisseau.Getx2(),self.__vaisseau.Gety2(), fill=self.__vaisseau.GetColor())
    
    def GenererProjectile(self,tir_ami,x,y):
        projectile1 = projectile(self.__canvas_len,self.__canvas_hei,x,y, tir_ami)
        corps_projectile = self.__canvas.create_rectangle(projectile1.Getx1(),projectile1.Gety1(),projectile1.Getx2(),projectile1.Gety2(), fill=projectile1.GetColor())

        #Rajoute les projectiles a la liste
        self.__projectiles.append(projectile1)
        self.__corps_projectiles.append(corps_projectile)
    
    def GenererTirAmi(self,event):
        x,y = self.__vaisseau.GetCentre()
        self.GenererProjectile(True,x,y)


    #Mettre ici les fonction detruisant les objets
    #_____________________________


    def SupprimerProjectile(self,projectile,i):
        self.__canvas.delete(self.__corps_projectiles[i])
        del self.__projectiles[i]
        del self.__corps_projectiles[i]

    def SupprimerAlien(self,):
        self.__canvas.delete(self.__corps_alien)
        self.__alien = ''
        self.__corps_alien = ''

    #Fonction de verification des coordonnes: Permet de savoir si c'est perdu
    #____________________

    def VerifCoord(self):
        if self.__projectiles != []:
            for i,projectile in enumerate(self.__projectiles):
                x,y = projectile.CalculerCentre()

                if projectile.GetEkip():    #Si le projectile est un tir ami

                    if (self.__alien.Gety2() >= projectile.Gety1()) and ((x >= self.__alien.Getx1()) and (x <= self.__alien.Getx2())):  #Si le projectile est dans la zone de l'alien
                        self.SupprimerAlien()
                        self.SupprimerProjectile(projectile,i)
                        
                    return True

                else:   #Sinon le tir est ennemis

                    if (self.__vaisseau.Gety1() <= projectile.Gety2()) and ((x >= self.__vaisseau.Getx1()) and (x <= self.__vaisseau.Getx2())): #Si est dans la zone du vaisseau
                        if self.__vies > 0:     #Si le vaisseau a assez de vies
                            self.__vies += -1
                            self.SupprimerProjectile(projectile,i)
                            return True
                        else:   #Si le vaisseau n'as plus de vie, arreter le jeu et afficher perdu
                            self.__canvas.create_text(int(self.__canvas_hei)/2,int(self.__canvas_len)/2,fill="red",font="Times 50 italic bold",text="PERDU")
                            return False
                    else:
                        return True
        else:
            return True

