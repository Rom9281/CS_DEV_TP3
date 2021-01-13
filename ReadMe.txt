%% LANCEMENT

    Le code se lance en chargent le main.py
    Il faut penser a mettre le jeu en pleine ecran
    Si on utilise le bouton rejouer, il faut penser a recliquer sur la fenetre pour que les actions soient faite dans le jeu.

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
            - Ce sont les entites qui sont percutes qui gerent les collsions et qui permetent de dire au GUI si il faut qu'elles soient enleves
    
%%NIVEAU
 - Suite a quelques problemes, il n'y a pas eu d'ajouts de NIVEAU
 - LA difficulte augmente au moment ou il reste que trois aliens d'attaques:
        - Les aliens tirent plus vite
        - Le joueur ne tire pas tout le temps
%%CHEATCODES
    - appuyer sur r permet de gagner ou perdre un nombre de vies choisit aleatoirement. Ne marche que si les on a plus de une vie.
    - Le mode difficile de la fin peut etre enleve en appuyant sur d, mais il enleve une vie
    - Code ultime : Hell mode en appuyant sur h... deconseille