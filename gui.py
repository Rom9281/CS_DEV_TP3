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

        self.__canvas = ""  #Defintion du canvas
        self.__canvas_len = "700"   #Definition de la longueur du canvas
        self.__canvas_hei = "700"   #Definition de la hauteur du canvas

        #Creation des caracteristiques de l'alien
        self.__alien = alien(self.__canvas_len,self.__canvas_hei)
        self.__corps_alien = ""
        self.__corps_aliens = []    #liste a utiliser quand il y aura plusieurs aliens

        #Creation des caracteristiques du vaisseau
        self.__vaisseau = vaisseau(self.__canvas_len,self.__canvas_hei)
        self.__corps_vaisseau = ""

        self.__projectile = ""
        self.__corps_projectile = ""

    

    def AfficherFenetre(self):
        self.__main = tk.Tk()

        self.__main.geometry(self.__main_len+"x"+self.__main_hei)

        
        #Ici le canvas

        self.__canvas = tk.Canvas(self.__main, width = self.__canvas_len, height = self.__canvas_hei, bg = "black")
        self.__canvas.pack()

        self.GenererAlien()     #Genere les aliens
        self.GenererVaisseau()  #Genere le vaisseau
        

        #Ici la zone de score
        score=0
        Score=tk.Label(self.__main , text="Score : "+ str(score) )
        Score.pack(side=tk.RIGHT)

        #ici la zone de vie
        vie=0
        Vie=tk.Label(self.__main , text="Vies : "+ str(vie) )
        Vie.pack(side=tk.RIGHT)

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
        if self.__projectile != "":
            if not self.__projectile.GetEtat():
                self.__canvas.delete(self.__corps_projectile)
                self.__projectile = ""
                self.__corps_projectile = ""
        
        #Mettre ici la fonctionn qui permet de modifier les coordonnes
        self.__alien.ModifierCoord()

        #Mettre ici les fonctions qui permettent a l'alien de tirer
        if self.__projectile == "":
            self.__random = random.randint(0,self.__coeff_aleatoire)
            if self.__random == 1:
                x,y = self.__alien.CalculerCentre()
                self.GenererProjectile(False,x,y)


        #Mettre ici la modification de l'objet du canvas
        self.__canvas.coords(self.__corps_alien,self.__alien.Getx1(),self.__alien.Gety1(),self.__alien.Getx2(),self.__alien.Gety2())
        if self.__projectile != "":
            self.__projectile.ModifierCoord()
            self.__canvas.coords(self.__corps_projectile,self.__projectile.Getx1(),self.__projectile.Gety1(),self.__projectile.Getx2(),self.__projectile.Gety2())
        
        #Realiser les deplacements
        self.__main.after(20, self.deplacer)
    

    #Mettre ici les fonctions afficher
    def GenererAlien(self):
        self.__corps_alien = self.__canvas.create_rectangle(self.__alien.Getx1(),self.__alien.Gety1(),self.__alien.Getx2(),self.__alien.Gety2(), fill = self.__alien.GetColor())



    def GenererVaisseau(self):
        self.__corps_vaisseau = self.__canvas.create_rectangle(self.__vaisseau.Getx1(),self.__vaisseau.Gety1(),self.__vaisseau.Getx2(),self.__vaisseau.Gety2(), fill=self.__vaisseau.GetColor())
    
    def GenererProjectile(self,tir_ami,x,y):
        self.__projectile = projectile(self.__canvas_len,self.__canvas_hei,x,y, tir_ami)
        self.__corps_projectile = self.__canvas.create_rectangle(self.__projectile.Getx1(),self.__projectile.Gety1(),self.__projectile.Getx2(),self.__projectile.Gety2(), fill=self.__projectile.GetColor())


