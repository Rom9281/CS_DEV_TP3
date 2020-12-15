import tkinter as tk

class gui():
    def __init__(self):
        self.__main = ""
        self.__score = ""
    

    def AfficherFenetre(self):
        self.__main = tk.Tk()
        
        #Ici le canvas

        #Ici la zone de score

        #ici le bouton quitter
        bouton1 = tk.Button(self.__main , text='Quitter',command=self.__main.quit)
        bouton1.pack()

        #Ici le bouton demarer



        self.__main.mainloop()
