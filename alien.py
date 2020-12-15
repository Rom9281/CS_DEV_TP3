import tkinter as tk

class alien():
    def __init__(self, canvas_len, canvas_hei):
        self.__canvas_len = canvas_len  #Recupere la longueur du canvas
        self.__canvas_hei = canvas_hei  #Recupere la hauteur du canvas

        #Corps de l'alien
        self.__corps_alien = ""

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.__x1 = 0
        self.__y1 = 100
        self.__x2 = 200
        self.__y2 = 200
        self.__color_fill = "pink"

        #Deplacement de l'alien
        self.__positif = True
        self.__vit_deplacer = 10

    
    def AfficherAlien(self,main):
        self.__corps_alien = main.create_rectangle(self.__x1,self.__y1,self.__x2,self.__y2, fill = self.__color_fill)
        print("ok")
    
    def ModifierCoord(self,main):
        if self.__positif:
            if int(self.__canvas_len) > (self.__x2 + self.__vit_deplacer):
                self.DeplacerDroit()
            else:
                self.__positif = False
                self.DeplacerGauche()
        else:
            if 0 < (self.__x1 - self.__vit_deplacer):
                self.DeplacerGauche()
            else:
                self.__positif = True
                self.DeplacerDroit()
        
        main.coords(self.__corps_alien,self.__x1,self.__y1,self.__x2,self.__y2)
            
    
    def DeplacerDroit(self):
        self.__x1 += self.__vit_deplacer
        self.__x2 += self.__vit_deplacer
    
    def DeplacerGauche(self):
        self.__x1 += -self.__vit_deplacer
        self.__x2 += -self.__vit_deplacer