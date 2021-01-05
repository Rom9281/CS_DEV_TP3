#   CPE Lyon - 3ETI

#   Auteurs : Lucas ROTH | Romain GAUD

#   Date : 1/5/2021

#   Matiere : CS DEV

#   TP : 3

#   Objectif : Creer une classe qui gere les coordonnes du vaisseau

import tkinter as tk

class vaisseau():
    def __init__(self, canvas_len, canvas_hei):
        self.__canvas_len = int(canvas_len)  #Recupere la longueur du canvas
        self.__canvas_hei = int(canvas_hei)  #Recupere la hauteur du canvas

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.__x1 = 400
        self.__y1 = 650
        self.__x2 = 500
        self.__y2 = 600

        self.__len = self.__x2 - self.__x1
        self.__hei = self.__y2 - self.__y1
        
        self.__color_fill = "blue"

        #Vitesse de delacement du vaisseau
        self.__vit_hor = 20 #Vitesse de deplacement horitontal
      

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
    
    def GetCentre(self):
        x,y = self.__x1 +(self.__x2/2), self.__y1 +(self.__y2/2)
        return x,y

    def MoveRight(self,event):
        if self.__canvas_len > (self.__x2 + self.__vit_hor):
            self.__x2 = self.__x2 + self.__vit_hor
            self.__x1 = self.__x1 + self.__vit_hor
        else:
            pass

    def MoveLeft(self,event):
        if 0 < (self.__x1 - self.__vit_hor):
            self.__x1 = self.__x1 - self.__vit_hor
            self.__x2 = self.__x2 - self.__vit_hor
        else:
            pass


        
        
    
   