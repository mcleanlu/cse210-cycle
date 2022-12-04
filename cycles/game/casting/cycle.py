import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Cycle(Actor):
    """Cycle() moves positions in segments while building a finite trail and accepts inputs to change directions

    Attributes:
    ---
        _cycle (self): player's head and current position
        _segments (list): list of actors in a cycle
        _cycle_position_velocity (method): initiate and create a cycle for the game
    """
    def __init__(self, position):
        """Initiate a cycle with list for segment
        """
        super().__init__()

        self._segments = []
        self._color = Color(255, 255, 255)
        self._cycle_position_velocity(position)
        self._name = ""

    def _cycle_position_velocity(self, position):
        """set position and velocity direction of cycle
        """
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "O" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)

    def set_name(self, name):
        """set name for player

        Args:
        ---
            _name (String): name
        """
        self._name = name
    
    def set_cycle_color(self, color):
        """color of cycle

        Args:
        ---
            color (Color): set color for cycle and actor
        """

        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)

    def get_segments(self):
        """get the segment of a cycle

        Returns:
        ---
            _segment (list): list of actors in a cycle"""
        return self._segments

    def get_name(self):
        """gets text to placed as player's name.

        Returns:
        ---
            _name (String): Text to be returned"""
        return self._name

    def move_next(self):
        """Move actor (head current position) to next position determined by direction and velocitiy. Within a range 1, 0 iterate through by -1 with determined velocity
        
        Args:
        _velocity

        """

        for segment in self._segments:
            segment.move_next()
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        """gets actor from _segments

        Returns:
        ---
            _segments (Actor): return the actor from _segments."""
        return self._segments[0]

    def turn_cycle(self, velocity):
        """Change direction of cycle via _velocity

        Args:
        ---
            Point: A given velocity to change direction.
        """

        self._segments[0].set_velocity(velocity)

    def trail(self, game_over):
        """Builds the trail a cycle.
        """
        trail = self._segments[-1]
        velocity = trail.get_velocity()
        offset = velocity.reverse()
        position = trail.get_position().add(offset)

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        if not game_over:
            segment.set_color(self._color)
        else:
            segment.set_color(constants.WHITE)
        self._segments.append(segment)