import tkinter as tk

class alien():
    def __init__(self, canvas_len, canvas_hei):
        self.__canvas_len = canvas_len  #Recupere la longueur du canvas
        self.__canvas_hei = canvas_hei  #Recupere la hauteur du canvas

        #Caracteristiques de l'alien

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.__x1 = 0
        self.__y1 = 100
        self.__x2 = 200
        self.__y2 = 200
        self.__color_fill = "pink"

        #Deplacement de l'alien
        self.__sens = "+"


    
    def AfficherAlien(self,main):
        main.create_rectangle(self.__x1,self.__y1,self.__x2,self.__y2, fill =self.__color_fill)
    
    def ModifierCoord(self):
        return False