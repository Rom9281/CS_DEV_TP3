%% LANCEMENT

    Le code se lance en chargent le main.py

%%STRUCTURE

    %le gui

        Le code se compose de plusieurs objects ayant des fonction differentes. L'objet GUI est l'interface principale.
        Il permet de Gerer l'interface graphique, et permet de gerer les differentes interactions entre les object.
        C'est un peu l'equivalent d'un dieu.


    %Autres Objets
    
        Le code repose sur la base suivante:
            - Chaque entite du jeu est compose d'un corps, qui est un objet canvas et d'un esprit, qui est un objet cree par notre equipe
            - L'esprit dicte au corps de bouger : c'est donc lui qui effectue les calculs de coordonnes.
            - Chaque entite (sauf le vaisseau qui est unique en son genre) est stoque dans un dictionaire et possede une identite numerique qui permet de le repertorier