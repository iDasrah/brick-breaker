from consts import *

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
            color = BRICK_COLORS[0]
        elif lives == 2:
            color = BRICK_COLORS[1]
        elif lives == 3:
            color = BRICK_COLORS[2]
        else:
            color = BRICK_COLORS[3]
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
                self.color = BRICK_COLORS[0]
            elif self.lives == 2:
                self.color = BRICK_COLORS[1]
            elif self.lives == 3:
                self.color = BRICK_COLORS[2]
            else:
                self.color = BRICK_COLORS[3]

            self.draw()
        else:
            self.set_x(-100)
