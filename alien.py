import tkinter as tk

class alien():
    def __init__(self):
        self.__x = 100
        self.__y = 100

        self.__length = 200
        self.__height = 200

        self.__color_fill = "pink"


    
    def AfficherAlien(self,main):
        main.create_rectangle(self.__x,self.__y,self.__length,self.__height, fill =self.__color_fill)