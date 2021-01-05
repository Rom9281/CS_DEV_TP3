import tkinter as tk

class alien():
    def __init__(self,min,max,canvas_len,canvas_hei,posX1,posY1,posX2,posY2,color):
        self.__min= min
        self.__max= max
        self.__canvas_len = canvas_len  #Recupere la longueur du canvas
        self.__canvas_hei = canvas_hei  #Recupere la hauteur du canvas

        #Corps de l'alien
        self.__corps_alien = ""

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.__x1 = posX1
        self.__y1 = posY1
        self.__x2 = posX2
        self.__y2 = posY2
        self.__color_fill = color

        #Deplacement de l'alien
        self.__positif = True
        self.__vit_deplacer_hor = 5 #Vitesse de deplacement horizontal
        self.__vit_deplacer_ver = 20 #Vitesse de deplacement vertical

    def Getx1(self):
        return self.__x1
    
    def Getx2(self):
        return self.__x2

    def Gety1(self):
        return self.__y1
    
    def Gety2(self):
        return self.__y2

    def GetColor(self):
        return self.__color_fill

    def ModifierCoord(self) :
        if self.__positif:
            if int(self.__max) > (self.__x2 + self.__vit_deplacer_hor):
                self.DeplacerDroit()
            else:
                self.__positif = False
                self.DeplacerGauche()
        else:
            if self.__min < (self.__x1 - self.__vit_deplacer_hor):
                self.DeplacerGauche()
            else:
                self.__positif = True
                self.DeplacerDroit()
                if int(self.__canvas_hei) > (self.__y2 + self.__vit_deplacer_ver):
                    self.DeplacerBas()
                else:
                    print("perdu")
            
    def DeplacerDroit(self):
        self.__x1 += self.__vit_deplacer_hor
        self.__x2 += self.__vit_deplacer_hor
    
    def DeplacerGauche(self):
        self.__x1 += - self.__vit_deplacer_hor
        self.__x2 += - self.__vit_deplacer_hor
    
    def DeplacerBas(self):
        self.__y1 += self.__vit_deplacer_ver
        self.__y2 += self.__vit_deplacer_ver

    def CalculerCentre(self):
        return (self.__x1 + (self.__x2 - self.__x1)/2) , (self.__y1 + (self.__y2 - self.__y1)/2)