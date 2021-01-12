#   CPE Lyon - 3ETI

#   Auteurs : Lucas ROTH | Romain GAUD

#   Date : 1/5/2021

#   Matiere : CS DEV

#   TP : 3

#   Objectif : Creer une classe qui permet de mettre des blocks de defense

class block():
    def __init__(self,posX1,posY1,posX2,posY2,invincible,color):
        self.__X1 = posX1
        self.__Y1 = posY1
        self.__X2 = posX2
        self.__Y2 = posY2

        self.__color_fill = color

        self.__invincible = invincible

    def Getx1(self):
        return self.__X1
    
    def Getx2(self):
        return self.__X2

    def Gety1(self):
        return self.__Y1
    
    def Gety2(self):
        return self.__Y2

    def GetColor(self):
        return self.__color_fill

    def IsInvincible(self):
        return self.__invincible