
#   CPE Lyon - 3ETI

#   Auteurs : Lucas ROTH | Romain GAUD

#   Date : 1/5/2021

#   Matiere : CS DEV

#   TP : 3

#   Objectif : Creer une classe qui gere la "conscience" de l'alien: comment il se deplace, ect...

import tkinter as tk

class alien():
    def __init__(self, canvas_len,canvas_hei,posX1,posY1,posX2,posY2,color,min,max):
        self.__canvas_len = canvas_len  #Recupere la longueur du canvas
        self.__canvas_hei = canvas_hei  #Recupere la hauteur du canvas

        self.__min=min  #Créer le min de la zone où se situe l'alien
        self.__max=max  #Créer le max de la zone où se situe l'alien

        #Corps de l'alien
        self.__corps_alien = ""

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.__x1 = posX1
        self.__y1 = posY1
        self.__x2 = posX2
        self.__y2 = posY2

        #LA couleur
        self.__color_fill = color

        #Deplacement de l'alien
        self.__positif = True
        self.__vit_deplacer_hor = 1 #Vitesse de deplacement horizontal
        self.__vit_deplacer_ver = 10 #Vitesse de deplacement vertical

        self.__etat = True

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

    def GetEtat(self):
        return self.__etat
    
    def Detruire(self):
        self.__etat = False

    def ModifierCoord(self):
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

    #LEs prochaines fonctions vont etablir si il ya collision ou non
    def IsColliding(self,Points):
        """Fonctionne en utilisant des coordones sous forme de tupples"""

        #Permet de verifier les collisions en prenant chaque coin de l'objet projectile et verifiant si il n'est pas dans le carre de l'objet percute

        point_proj = []

        point_proj.append(Points[0])
        point_proj.append(Points[1])

        P3_proj,P4_proj = self.CalcAllPoints(Points)

        point_proj.append(P3_proj)
        point_proj.append(P4_proj)

        #Boucle principale verifiant si un des points du prjectil est dans l'alien (les ifs sont pour les testes)
        for point in point_proj:
            if float(point[0]) > float(self.__x1) and (float(point[0]) < float(self.__x2)):
                    if float(point[1]) < float(self.__y2) and (float(point[1]) > float(self.__y1)):
                        return True
        return False

    def CalcAllPoints(self,Points):

        x3 = Points[1][0]
        y3 = Points[0][1]
        x4 = Points[0][0]
        y4 = Points[1][1]

        return (x3,y3),(x4,y4)