class Rect:
    """
    Classe Rect, définit un rectangle.
    """

    def __init__(self, x, y, width, height):
        """
        Constructeur de la classe Rect

        Args:
            x (int): position en x
            y (int): position en y
            width (int): longueur
            height (int): hauteur
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        """
        Retourne la valeur de x

        Returns:
            int: x (abscisse)
        """
        return self.x

    def get_y(self):
        """
        Retourne la valeur de y

        Returns:
            int: y (ordonnée)
        """
        return self.y

    def get_width(self):
        """
        Retourne la longueur du rectangle

        Returns:
            int: longueur du rectangle
        """
        return self.width

    def get_height(self):
        """
        Retourne la hauteur du rectangle

        Returns:
            int: hauteur du rectangle
        """
        return self.height

    def set_x(self, x):
        """
        Change la valeur de x

        Args:
            x (int): nouveau x
        """
        self.x = x

    def set_y(self, y):
        """
        Change la valeur de y

        Args:
            y (int): nouveau y
        """
        self.y = y

    def move_x(self, dx):
        """
        Déplace le rectangle en x

        Args:
            dx (int): longueur du déplacement en x
        """
        self.x += dx

    def move_y(self, dy):
        """
        Déplace le rectangle en y

        Args:
            dy (int): longueur du déplacement en y
        """
        self.y += dy

    def is_colliding(self, rect, dx=0, dy=0):
        """
        Vérifie si oui ou non deux rectangles sont en collision.

        Args:
            rect (Rect): rectangle comparé
            dx (int, optional): déplacement éventuel en x. Defaults to 0.
            dy (int, optional): déplacement éventuel en y. Defaults to 0.

        Returns:
            bool: True si self et rect sont en collisions, sinon False.
        """
        if self.x + self.width + dx < rect.x or rect.x + rect.width < self.x + dx or self.y + self.height + dy < rect.y or rect.y + rect.height < self.y + dy:
            return False
        else:
            return True
