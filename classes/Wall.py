from pygame import Color
from pygame import Rect as PyRect
from pygame import draw

from classes.Rect import *


class Wall(Rect):
    """
    Classe Wall, définit un mur.
    Hérite de la classe Rect.
    """

    def __init__(self, x, y, width, heigth, color, surface):
        """
        Constructeur de la classe Wall

        Args:
            x (int): position en x
            y (int): position en y
            width (int): longueur
            heigth (int): hauteur
            color (tuple/string): couleur
            surface (pygame.Surface): surface du jeu
        """
        super().__init__(x, y, width, heigth)
        self.color = color
        self.surface = surface

    def draw(self):
        """
        Dessine un mur
        """
        draw.rect(self.surface, Color(self.color), PyRect(
            self.x, self.y, self.width, self.height))
        draw.rect(self.surface, Color("#111000"), PyRect(
            self.x, self.y, self.width, self.height), 1)
