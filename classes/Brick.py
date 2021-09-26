from pygame import Rect as PyRect
from pygame import draw

from classes.Wall import *


class Brick(Wall):
    """
    Classe Brick, définit une brique.
    Hérite de la classe Wall.
    """

    def __init__(self, x, y, width, height, lives, surface, color=None):
        """
        Constructeur de la classe Brick

        Args:
            x (int): position en x
            y (int): position en y
            width (int): longueur
            heigth (int): hauteur
            lives (int): vies de la brique
            color (tuple/string, optional): couleur
        """
        if lives == 1:
            color = '#41F063'
        elif lives == 2:
            color = '#416BF0'
        elif lives == 3:
            color = '#F0BA41'
        else:
            color = '#FA0801'
        super().__init__(x, y, width, height, color, surface)
        self.lives = lives

    def lose_life(self):
        """
        Fait perdre une vie à la brique
        """
        self.lives -= 1

    def get_lives(self):
        """
        Retourne le nombre de vies de la brique

        Returns:
            int: nombre de vies de la brique
        """
        return self.lives

    def draw(self):
        """
        Dessine la brique si et seulement si elle a plus de 1 vie.
        """
        if self.lives > 0:
            super().draw()

    def check_lives(self):
        """
        Vérifie le nombre de vies restantes de la brique.
        """
        if self.lives > 0:
            if self.lives == 1:
                self.color = '#41F063'
            elif self.lives == 2:
                self.color = '#416BF0'
            elif self.lives == 3:
                self.color = '#F0BA41'
            else:
                self.color = '#FA0801'

            self.draw()
        else:
            self.set_x(-100)
