import tkinter as tk

class gui():
    def __init__(self):
        self.__main = ""    #Definition de la fenetre principale
        self.__score = 0    #Definition du score

        self.__canvas = ""  #Defintion du canvas

    

    def AfficherFenetre(self):
        self.__main = tk.Tk()
        self.__main.geometry("1000x1000")
        
        #Ici le canvas

        self.__canvas = tk.Canvas(self.__main, width = "700", height = "700", bg = "black")
        self.__canvas.pack()


        #Ici la zone de score

        #ici le bouton quitter

        #Ici le bouton demarer

        self.__main.mainloop()
