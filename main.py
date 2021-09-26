import os
from json import dumps

import pygame

from classes.MainMenu import *

stats_file_path = 'stats.json'

if os.path.isfile(stats_file_path) == False:
    stats_file = open(stats_file_path, 'w')
    default_content = dumps({"wins": 0, "loses": 0, "games": 0}, indent=2)
    stats_file.write(default_content)
    stats_file.close()

pygame.init()


# Parametrages de la fenêtre
size = WIDTH, HEIGHT = 1000, 600
win = pygame.display.set_mode(size)
pygame.display.set_caption('Casse Brique')

# Affichage du menu principal
main_menu = MainMenu(win, stats_file_path)
main_menu.run()