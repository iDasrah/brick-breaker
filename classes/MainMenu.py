from os import path

from consts import *
from pygame import Rect as PyRect
from pygame import display, draw, event, font, mouse

from classes.Button import *
from classes.Game import *

font.init()

title_path = path.join(ASSETS_FOLDER, 'fonts/BubbleShine.ttf')

title_font = font.Font(title_path, 100)
title = title_font.render('CASSE BRIQUE', True, '#000000')
main_font = font.SysFont('Calibri', 30)


class MainMenu:
    """
    Classe MainMenu, définit le menu principal.
    """

    def __init__(self, surface, stats, config):
        """
        Constructeur de la classe MainMenu.

        Args:
            surface (pygame.Surface): surface du jeu
            stats (string): stats du jeu
        """
        self.surface = surface
        self.stats = stats
        self.config = config
        self.buttons = [
            Button(WIDTH // 2 - BUTTONS_WIDTH // 2, HEIGHT // 3,
                   BUTTONS_WIDTH, BUTTONS_HEIGHT, main_font, 'JOUER', '#000000', PLAY_BUTTON_COLOR, self.surface, self.stats, self.config)
        ]

    def show_stats(self):
        """
        Affiche les stats à l'écran
        """

        wins = self.stats['wins']
        defeats = self.stats['loses']
        games = self.stats['games']

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
