from os import path
from random import randint

from pygame import Color, draw, mixer

from classes.Rect import *

mixer.init()

# Initialisation des sons
hit_sfx = mixer.Sound('assets/sounds/hit.wav')
out_sfx = mixer.Sound('assets/sounds/out.wav')


class Ball(Rect):
    """
    Classe Ball, définit une balle.
    Hérite de la classe Rect.
    """

    def __init__(self, x, y, radius, speed_x, speed_y, color, game, surface):
        """
        Constructeur de la classe Ball

        Args:
            x (int): position en x
            y (int): position en y
            radius (int): rayon de la balle
            speed_x (int): déplacement à la verticale
            speed_y (int): déplacement à l'horizontale
            color (tuple/string): couleur
            game (Game): jeu en cours
            surface (pygame.Surface): surface du jeu
        """
        super().__init__(x, y, width=radius, height=radius)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.game = game
        self.surface = surface

    def update(self):
        """
        Met à jour la positon de la balle
        """
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        """
        Dessine la balle
        """
        draw.circle(self.surface, Color(self.color),
                    (self.x, self.y), self.radius)

    def is_touching_walls(self, walls):
        """
        Vérifie si la balle entre en collison avec les murs

        Args:
            walls (list): liste de murs
        """
        for wall in walls:
            if self.is_colliding(wall, self.speed_x):
                self.speed_x = -self.speed_x
            if self.is_colliding(wall, 0, self.speed_y):
                self.speed_y = -self.speed_y

    def is_touching_bricks(self, bricks):
        """
        Vérifie si la balle entre en collison avec les briques

        Args:
            bricks (list): liste de briques
        """
        for brick in bricks:
            if self.is_colliding(brick, self.speed_x):
                hit_sfx.play()
                self.speed_x = -self.speed_x
                brick.lose_life()
            if self.is_colliding(brick, 0, self.speed_y):
                hit_sfx.play()
                self.speed_y = -self.speed_y
                brick.lose_life()

    def is_touching_puck(self, puck):
        """
        Vérifie si la balle touche le palet

        Args:
            puck (Puck): palet
        """
        if self.is_colliding(puck, self.speed_x):
            self.speed_x = -self.speed_x
        if self.is_colliding(puck, 0, self.speed_y):
            self.speed_y = -self.speed_y

    def is_going_out(self):
        """
        Vérifie si la balle sort du jeu
        """
        if self.y > 600:
            self.y = randint(250, 600 - 100)
            self.speed_y = -self.speed_y
            self.game.lose_life()
            out_sfx.play()
