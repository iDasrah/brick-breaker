import json
from os import path

from consts import *
from generators import *
from pygame import Rect as PyRect
from pygame import display, draw, event, font, image, mixer, time, transform
from pygame.locals import *

from classes.Ball import *
from classes.Puck import *

# Initialisation de pygame.font
font.init()

# Chemins d'accès aux fichiers
heart_path = path.join(ASSETS_FOLDER, 'images/heart.png')
win_sound_path = path.join(ASSETS_FOLDER, 'sounds/win.wav')
lose_sound_path = path.join(ASSETS_FOLDER, 'sounds/lose.wav')

# Chargement de l'image représentant le nombre de vies
heart = image.load(heart_path)
heart = transform.scale(heart, (32, 32))  # Passage de 256x256 à 64*64

# Chargement de la police d'écriture
main_font = font.SysFont('Calibri', 200)

# Chargement des sons du jeu
win_sound = mixer.Sound(win_sound_path)
lose_sound = mixer.Sound(lose_sound_path)


class Game:
    """
    Classe Game, définit une session de jeu.
    """

    def __init__(self, lives, surface, stats, config):
        """
        Constructeur de la classe Game.

        Args:
            lives (int): nombre de vies de la partie
            surface (pygame.Surface): surface du jeu
            stats (string): statistiques de jeu
            config (string): configuration 
        """
        self.lives = lives
        self.surface = surface
        self.config = config
        self.walls = generate_walls(self.surface)
        self.bricks = generate_bricks(self.surface, self.config)
        self.ball = Ball(randint(10, WIDTH - 10),
                         randint(250, HEIGHT - 100), 10, 2, 2, BALL_COLOR, self, self.surface)
        self.puck = Puck(WIDTH // 2 - 50, HEIGHT - 30, 100, 20,
                         PUCK_COLOR, 6, 10, WIDTH - 10, 'LEFT', 'RIGHT', self.surface)
        self.running = True
        self.counter = 3
        self.stats = stats

    def lose_life(self):
        """
        Enlève une vie
        """
        self.lives -= 1

    def show_lives(self):
        """
        Affiche le nombre de vies à l'écran
        """
        for live in range(self.lives):
            self.surface.blit(heart, (WIDTH - heart.get_width() -
                                      20 - live * 26, HEIGHT - heart.get_height() - 10))

    def update_stats(self, action):
        """
        Met à jour le fichier stats.json à la fin de la partie

        Args:
            action (str): action à effectuer (lose/win)
        """
        new_stats = json.dumps(
            {"wins": self.stats['wins'] + 1 if action == 'win' else self.stats['wins'], "loses": self.stats['loses'] + 1 if action == 'lose' else self.stats['wins'], "games": self.stats['games'] + 1}, indent=2)

        stats_file = open(STATS_FILE_PATH, 'w')
        stats_file.write(new_stats)
        stats_file.close()

    def win(self):
        """
        Quand le joueur gagne
        """
        self.puck.set_x(-100)
        self.ball.set_x(-100)
        win_sound.play()
        draw.rect(self.surface, '#ffffff', PyRect(0, 0, WIDTH, HEIGHT))
        text = main_font.render('VICTOIRE !', True, WIN_COLOR)
        self.surface.blit(text, (WIDTH // 2 - text.get_width() //
                          2, HEIGHT // 2 - text.get_height() // 2))
        display.flip()
        time.delay(2000)
        self.running = False
        self.update_stats('win')

    def lose(self):
        """
        Quand le joueur perd
        """
        self.bricks = []
        self.puck.set_x(-100)
        self.ball.set_x(-100)
        lose_sound.play()
        draw.rect(self.surface, '#ffffff', PyRect(0, 0, WIDTH, HEIGHT))
        text = main_font.render('DEFAITE :(', True, LOSE_COLOR)
        self.surface.blit(text, (WIDTH // 2 - text.get_width() //
                          2, HEIGHT // 2 - text.get_height() // 2))
        display.flip()
        time.delay(2000)
        self.running = False
        self.update_stats('lose')

    def run(self):
        """
        Boucle du jeu
        """
        while self.running:
            # Fond blanc
            draw.rect(self.surface, '#ffffff', PyRect(0, 0, WIDTH, HEIGHT))

            if self.counter > 0:
                for _ in range(self.counter):
                    draw.rect(self.surface, '#ffffff',
                              PyRect(0, 0, WIDTH, HEIGHT))
                    text = main_font.render(str(self.counter), True, "#000000")
                    self.surface.blit(text, (WIDTH // 2 - text.get_width() //
                                             2, HEIGHT // 2 - text.get_height() // 2))
                    self.counter -= 1
                    display.flip()
                    time.delay(1000)

            if len(self.bricks) == 0:
                self.win()

            if self.lives == 0:
                self.lose()

            # Affichage des éléments du jeu
            self.puck.draw()
            self.ball.draw()

            for wall in self.walls:
                wall.draw()

            for brick in self.bricks:
                brick.draw()
                brick.check_lives()

                if brick.lives == 0:
                    self.bricks.remove(brick)

            self.show_lives()

            # Tests de collision
            self.ball.is_touching_walls(self.walls)
            self.ball.is_touching_puck(self.puck)
            self.ball.is_touching_bricks(self.bricks)
            self.ball.is_going_out()

            # Mises à jour
            self.puck.update()
            self.ball.update()

            display.flip()

            # Gestion des évènements
            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                elif e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        self.puck.handle_events('KEYDOWN', 'LEFT')
                    elif e.key == K_RIGHT:
                        self.puck.handle_events('KEYDOWN', 'RIGHT')
                elif e.type == KEYUP:
                    if e.key == K_LEFT:
                        self.puck.handle_events('KEYUP', 'LEFT')
                    elif e.key == K_RIGHT:
                        self.puck.handle_events('KEYUP', 'RIGHT')
