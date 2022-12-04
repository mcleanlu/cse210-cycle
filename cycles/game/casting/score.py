from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        position (Point): begin the players at a certain point in the window.
        _player_name (string): Player's name is obtained from a string input
        set_position (method): Place the score position in the window
        set_text (method): Display the player's name in the window
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        position = Point(0, 0)
        self._player_name = ""
        self.set_text(f"{self._player_name}: {self._points}")
        self.set_position(position)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): Increase the value of _points
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        """Get the given points to the user

        Returns:
        ---
            points (int): points collected from player
        """
        return self._points

    def reduce_points(self):
        """Reduces points for the user
        
        Args:
            points (int): Reduce the value of _points
        """
        self._points -= 1
        self.set_text(f"Score: {self._points}")

    def set_player_name(self,name):
        """Collect the name of the player from the user

        Args:
            name (string): Set text to _player_name
        """
        self._player_name = name
        self.set_text(f"Player {self._player_name}: {self._points}")