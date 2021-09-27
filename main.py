import os
from json import dumps

import pygame

from classes.MainMenu import *
from consts import *

if os.path.isfile(STATS_FILE_PATH) == False:
    stats_file = open(STATS_FILE_PATH, 'w')
    default_content = dumps(
        {"wins": 0, "loses": 0, "games": 0}, indent=2)
    stats_file.write(default_content)
    stats_file.close()
if os.path.isfile(CONFIG_FILE_PATH) == False:
    config_file = open(CONFIG_FILE_PATH, 'w')
    default_content = dumps({"rows": 8, "lines": 10, "lives": 5}, indent=2)
    config_file.write(default_content)
    config_file.close()

stats = json.load(open(STATS_FILE_PATH))
config = json.load(open(CONFIG_FILE_PATH))

pygame.init()


# Parametrages de la fenêtre
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Casse Brique')

# Affichage du menu principal
main_menu = MainMenu(win, stats, config)
main_menu.run()
