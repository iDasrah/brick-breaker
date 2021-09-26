import json

from pygame import Rect as PyRect
from pygame import display, draw, event, font, mouse

from classes.Button import *
from classes.Game import *

font.init()

title_font = font.Font('assets/fonts/BubbleShine.ttf', 100)
title = title_font.render('CASSE BRIQUE', True, '#000000')
main_font = font.SysFont('Calibri', 30)

BUTTONS_WIDTH = 300
BUTTONS_HEIGHT = 50


class MainMenu:
    """
    Classe MainMenu, définit le menu principal.
    """

    def __init__(self, surface, stats):
        """
        Constructeur de la classe MainMenu.

        Args:
            surface (pygame.Surface): surface du jeu
            stats (string): stats du jeu
        """
        self.surface = surface
        self.stats = stats
        self.buttons = [
            Button(WIDTH // 2 - BUTTONS_WIDTH // 2, HEIGHT // 3,
                   BUTTONS_WIDTH, BUTTONS_HEIGHT, main_font, 'JOUER', '#000000', '#28E3CA', self.surface, self.stats)
        ]

    def show_stats(self):
        """
        Affiche les stats à l'écran
        """
        stats_file = open(self.stats)
        stats = json.load(stats_file)

        wins = stats['wins']
        defeats = stats['loses']
        games = stats['games']

        stats = {
            'Victoires': wins,
            'Défaites': defeats,
            'Parties': games
        }
        space_between = 100
        i = 1
        for key, value in stats.items():
            stat_text = main_font.render(f'{key}: {value}', True, '#000000')
            self.surface.blit(
                stat_text, ((stat_text.get_width() + space_between * i), HEIGHT // 2))
            i += 2
        display.flip()

    def run(self):
        """
        Boucle du menu principal
        """
        run = True

        while run:
            # Fond gris
            draw.rect(self.surface, '#BFC4C3', PyRect(0, 0, WIDTH, HEIGHT))
            self.surface.blit(
                title, ((WIDTH // 2 - title.get_width() // 2), 50))

            for button in self.buttons:
                button.draw()

            self.show_stats()

            display.flip()

            for e in event.get():
                if e.type == QUIT:
                    run = False
                elif e.type == MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.is_clicked(mouse.get_pos())
                elif e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        button.create_game()
