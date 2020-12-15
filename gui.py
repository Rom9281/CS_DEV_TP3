import tkinter as tk
from alien import alien

class gui():
    def __init__(self):
        self.__main = ""    #Definition de la fenetre principale
        self.__main_len = "1000"    #longueur de la fenetre
        self.__main_hei = "1000"    #largeur de la fenetre


        self.__score = 0    #Definition du score

        self.__canvas = ""  #Defintion du canvas
        self.__canvas_len = "700"   #Definition de la longueur du canvas
        self.__canvas_hei = "700"   #Definition de la hauteur du canvas

        self.__alien = alien(self.__canvas_len,self.__canvas_hei)
        self.__corps_alien = ""
        self.__corps_aliens = []    #liste a utiliser quand il y aura plusieurs aliens

    

    def AfficherFenetre(self):
        self.__main = tk.Tk()

        self.__main.geometry(self.__main_len+"x"+self.__main_hei)

        
        #Ici le canvas

        self.__canvas = tk.Canvas(self.__main, width = self.__canvas_len, height = self.__canvas_hei, bg = "black")
        self.__canvas.pack()

        self.GenererAlien()     #Genere les aliens
        

        #Ici la zone de score
        score=0
        Score=tk.Label(self.__main , text="Score : "+ str(score) )
        Score.pack(side=tk.RIGHT)

        #ici la zone de vie
        vie=0
        Vie=tk.Label(self.__main , text="Vies : "+ str(vie) )
        Vie.pack(side=tk.RIGHT)

        #ici le bouton quitter

        bouton1 = tk.Button(self.__main , text='Quitter',command=self.__main.quit)
        bouton1.pack()

        #Ici le bouton demarer

        bouton2 = tk.Button(self.__main , text='Play' )
        bouton2.pack()


        #Permet de deplacer les objets
        self.deplacer()     #permet d'actualiser les positions
        self.__main.mainloop()
    
    def deplacer(self):
        self.__alien.ModifierCoord()
        self.__canvas.coords(self.__corps_alien,self.__alien.Getx1(),self.__alien.Gety1(),self.__alien.Getx2(),self.__alien.Gety2())
        self.__main.after(20, self.deplacer)
    
    def GenererAlien(self):
        self.__corps_alien = self.__canvas.create_rectangle(self.__alien.Getx1(),self.__alien.Gety1(),self.__alien.Getx2(),self.__alien.Gety2(), fill = self.__alien.GetColor())

