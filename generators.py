from random import randint

from classes.Brick import *
from classes.Wall import *

WIDTH = 1000
HEIGHT = 600


WALLS_COLOR = '#484B4C'
WALLS_SIZES = [
    [0, 0, 10, HEIGHT],
    [WIDTH - 10, 0, 10, HEIGHT],
    [0, 0, WIDTH, 10],
]


def generate_bricks(surface, config):
    ROWS = config['rows']
    LINES = config['lines']

    BRICKS_WIDTH = (WIDTH - 20) // LINES
    BRICKS_HEIGHT = 30

    bricks = []
    y = -BRICKS_HEIGHT + 10
    for row in range(ROWS):
        y += BRICKS_HEIGHT
        x = 10
        for line in range(LINES):
            lives = randint(1, 4)

            bricks.append(Brick(x, y, BRICKS_WIDTH,
                          BRICKS_HEIGHT, lives, surface))
            x += BRICKS_WIDTH
    return bricks


def generate_walls(surface):
    walls = []
    for i in range(len(WALLS_SIZES)):
        walls.append(Wall(WALLS_SIZES[i][0], WALLS_SIZES[i][1],
                     WALLS_SIZES[i][2], WALLS_SIZES[i][3], WALLS_COLOR, surface))
    return walls
