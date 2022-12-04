import constants
from game.casting.actor import Actor


class End(Actor):
    """
    End the game with a message

    Attributes:
    ---
        _color (constant): Message color
    """
    def __init__(self):
        "Generate ending message with constant color."
        super().__init__()
        self._color = constants.GREEN

    def get_color(self):
        """Gets the color.

        Returns:
        ---
            Color: message color.
        """
        return super().get_color()

    def set_color(self, color):
        """Sets the color.

        Args:
        ---
            color (Color): message color.
        """
        return super().set_color(color)