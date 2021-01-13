#   CPE Lyon - 3ETI

#   Auteurs : Lucas ROTH | Romain GAUD

#   Date : 1/5/2021

#   Matiere : CS DEV

#   TP : 3

#   Objectif : Creer la classe qui gere les coordonnes du projectile

class projectile():
    def __init__(self,canvas_len, canvas_hei, objet_x, objet_y, tir_ami,color):
        self.__canvas_len = canvas_len                          #Recupere la longueur du canvas
        self.__canvas_hei = canvas_hei                          #Recupere la hauteur du canvas

        self.__tir_ami = tir_ami                                #True = Tir ami

        self.__etat = True

        self.__largeur = 3                                      #Definit la largeur du projectile
        self.__longueur = 9                                     #Definit la longeur du projectile
        self.__color = color                                   #Definit la couleur du projectile

        self.__deplacer_vit = 4                                 #Vitesse de deplacment du missile

        if self.__tir_ami:
            #Si c'est un tir ami, le projectile devra partir du bas du vaisseau et monter
            self.__x1 = objet_x - self.__largeur/2
            self.__y1 = objet_y - self.__longueur
            self.__x2 = objet_x + self.__largeur/2
            self.__y2 = objet_y
        else:
            #Si c'est un tir enemeis, le projectile devra partir du bas du vaisseau et monter
            self.__x1 = objet_x - self.__largeur/2
            self.__y1 = objet_y
            self.__x2 = objet_x + self.__largeur/2
            self.__y2 = objet_y + self.__longueur

    def Getx1(self):
        return self.__x1

    def Getx2(self):
        return self.__x2

    def Gety1(self):
        return self.__y1
    
    def Gety2(self):
        return self.__y2

    def GetPoints(self):
        return [(self.__x1,self.__y1),(self.__x2,self.__y2)]

    def GetColor(self):
        return self.__color
    
    def GetEtat(self):
        return self.__etat
    
    def GetEkip(self):
        return self.__tir_ami
    
    def Detruire(self):
        self.__etat = False
    
    def ModifierCoord(self):
        """Permet de modifier les coordonnes du projectile"""

        if self.__tir_ami:
            if 0 < (self.__y1 - self.__deplacer_vit):
                self.DeplacerHaut()
            else:
                self.__etat = False
        else:
            if int(self.__canvas_hei) > (self.__y2 + self.__deplacer_vit):
                self.DeplacerBas()
            else:
                self.__etat = False

    def DeplacerHaut(self):
        self.__y1 += - self.__deplacer_vit
        self.__y2 += - self.__deplacer_vit
    
    def DeplacerBas(self):
        self.__y1 += + self.__deplacer_vit
        self.__y2 += + self.__deplacer_vit
    
    def CalculerCentre(self):
        return (self.__x1 + (self.__x2 - self.__x1)/2) , (self.__y1 + (self.__y2 - self.__y1)/2)

    
