from classes.Wall import *


class Puck(Wall):
    """
    Classe Puck, définit un palet.
    Hérite de Wall.
    """

    def __init__(self, x, y, width, heigth, color, speed, limit1, limit2, key1, key2, surface):
        """
        Constructeur de la classe Puck

        Args:
            x (int): position en x
            y (int): position en y
            width (int): longueur
            heigth (int): hauteur
            color (tuple/string): couleur
            speed (int): vitesse du palet
            limit1 (int): limite inférieure du déplacement
            limit2 (int): limite supérieure du déplacement
            key1 (string): touche direction (gauche)
            key2 (string): touche direction (droite)
            surface (pygame.Surface): surface du jeu
        """
        super().__init__(x, y, width, heigth, color, surface)

        self.speed = speed
        self.limit1 = limit1
        self.limit2 = limit2
        self.keys = {
            "key1": key1,
            "key2": key2,
            "states": {
                "key1": False,
                "key2": False
            }
        }

    def update(self):
        """
        Met à jour la position du palet quand déplacé
        """
        if self.keys['states']['key1'] == True:
            self.x -= self.speed
        if self.keys['states']['key2'] == True:
            self.x += self.speed
        if self.x <= self.limit1:
            self.x = self.limit1 + 1
        if self.x + self.width >= self.limit2:
            self.x = self.limit2 - self.width

    def handle_events(self, event, key=None):
        """
        Gère les évènements

        Args:
            event (string): nom de l'évènement
            key (string, optional): touche
        """
        if event == 'KEYDOWN':
            if key == 'LEFT':
                self.keys['states']['key1'] = True
            elif key == 'RIGHT':
                self.keys['states']['key2'] = True
        elif event == 'KEYUP':
            if key == 'LEFT':
                self.keys['states']['key1'] = False
            elif key == 'RIGHT':
                self.keys['states']['key2'] = False
