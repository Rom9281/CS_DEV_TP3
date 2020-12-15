import tkinter as tk

class vaisseau():
    def __init__(self, canvas_len, canvas_hei):
        self.__canvas_len = canvas_len  #Recupere la longueur du canvas
        self.__canvas_hei = canvas_hei  #Recupere la hauteur du canvas

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.__x1 = 330
        self.__y1 = 650
        self.__x2 = 370
        self.__y2 = 680
        self.__color_fill = "blue"
      



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
        
        
    
   