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
        self.__y1 = self.__canvas_hei - 51
        self.__x2 = 500
        self.__y2 = self.__canvas_hei - 1

        self.__len = self.__x2 - self.__x1
        self.__hei = self.__y2 - self.__y1
        
        self.__color_fill = "blue"

        #Vitesse de delacement du vaisseau
        self.__vit_hor = 30 #Vitesse de deplacement horitontal
      

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
        x,y = self.__x1 +((self.__x2 - self.__x1)/2), self.__y1 +((self.__y2- self.__y1)/2)
        return x,y

    def MoveRight(self,event):
        if self.__canvas_len > (self.__x2 + self.__vit_hor):
            self.__x2 = self.__x2 + self.__vit_hor
            self.__x1 = self.__x1 + self.__vit_hor
        else:
            self.__x2 = self.__canvas_len - 1
            self.__x1 = (self.__canvas_len - 1) - self.__len
            pass

    def MoveLeft(self,event):
        if 0 < (self.__x1 - self.__vit_hor):
            self.__x1 = self.__x1 - self.__vit_hor
            self.__x2 = self.__x2 - self.__vit_hor
        else:
            self.__x1 = 0
            self.__x2 = self.__len
            pass
    
    def IsColliding(self,Points):
        """Fonctionne en utilisant des coordones sous forme de tupples"""

        #Permet de verifier les collisions en prenant chaque coin de l'objet projectile et verifiant si il n'est pas dans le carre de l'objet percute


        point_proj = []

        point_proj.append(Points[0])
        point_proj.append(Points[1])

        P3_proj,P4_proj = self.CalcAllPoints(Points)                #Permet d'obtenir les points restants

        point_proj.append(P3_proj)
        point_proj.append(P4_proj)

        #Boucle principale verifiant si un des points du prjectil est dans l'alien (les ifs sont pour les testes)
        for point in point_proj:
            if float(point[0]) > float(self.__x1) and (float(point[0]) < float(self.__x2)):
                if float(point[1]) < float(self.__y2) and (float(point[1]) > float(self.__y1)):
                    return True
        return False

    def CalcAllPoints(self,Points):
        """ Permet de calculer les points restants a partir des points donnes"""
        
        x3 = Points[1][0]
        y3 = Points[0][1]
        x4 = Points[0][0]
        y4 = Points[1][1]

        return (x3,y3),(x4,y4)


        
        
    
   