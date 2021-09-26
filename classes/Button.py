from pygame import Color
from pygame import Rect as PyRect
from pygame import draw

from classes.Game import *
from classes.Rect import *


class Button(Rect):
    """
    Classe Button, définit un bouton.
    Hérite de la classe Rect.
    """

    def __init__(self, x, y, width, height, font, text, text_color, button_color, surface, stats):
        """
        Constructeur de la classe Button.

        Args:
            x (int): position en x
            y (int): position en y
            width (int): longueur
            height (int): hauteur
            font (pygame.Font): police d'écriture
            text (string): texte dans le bouton
            text_color (tuple/string): couleur du texte
            button_color (tuple/string): couleur du bouton
            surface (pygame.Surface): surface du jeu
            stats (string): statistiques de jeu
        """
        super().__init__(x, y, width, height)
        self.font = font
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.button_text = font.render(self.text, True, self.text_color)
        self.surface = surface
        self.stats = stats

    def draw(self):
        """
        Affiche le bouton et son texte.
        """
        draw.rect(self.surface, Color(self.button_color), PyRect(
            self.x, self.y, self.width, self.height))
        self.surface.blit(self.button_text, ((self.x + self.width // 2 -
                                              self.button_text.get_width() // 2), (self.y + self.height // 2 - self.button_text.get_height() // 2)))

    def is_clicked(self, mouse_pos):
        """
        Vérifie si le bouton est cliqué.

        Args:
            mouse_pos (tuple): positon en (x; y) du pointeur de la souris.
        """
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
            self.create_game()

    def create_game(self):
        """
        Créée une session Zde jeu.
        """
        game = Game(5, self.surface, self.stats)
        game.run()
