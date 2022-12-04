import constants
from game.casting.End import End
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides with another cycle or the its own segments. Also handles if the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._game_over_message = ""
        # Hit enter to start the game
        input("Press Enter to continue...")

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)

    def _handle_trail_collision(self, cast):
        """"Handles how the cycles interact with the trails

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cycle_one.trail(self._is_game_over)
        cycle_two.trail(self._is_game_over)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of its segments or the other
        cycle.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        cycle1 = cast.get_first_actor("cycle_one")
        cycle2 = cast.get_first_actor("cycle_two")
        head1 = cycle1.get_cycle()
        head2 = cycle2.get_cycle()
        segments1 = cycle1.get_segments()[1:]
        segments2 = cycle2.get_segments()[1:]
        

        # cycle1 wins if cycle2 hits cycle1's trail
        for segment1 in segments1:
            if head2.get_position().equals(segment1.get_position()):
                score2.reduce_points()
                if score2.get_points() < 1:
                    self._game_over_message = f"{cycle1.get_name()} wins!"
                    self._is_game_over = True
            
            # cycle2 wins if cycle1 hits cycle1's trail
            if head1.get_position().equals(segment1.get_position()):
                score1.reduce_points()
                if score1.get_points() < 1:
                    self._game_over_message = f"{cycle2.get_name()} wins!"
                    self._is_game_over = True

        # cycle2 wins if cycle1 hits cycle2's trail
        for segment2 in segments2:
            if head1.get_position().equals(segment2.get_position()):
                score1.reduce_points()
                if score1.get_points() < 1:
                    self._game_over_message = f"{cycle2.get_name()} wins!"
                    self._is_game_over = True

            # cycle1 wins if cycle2 hits cycle2's trail
            if head2.get_position().equals(segment2.get_position()):
                score2.reduce_points()
                if score2.get_points() < 1:
                    self._game_over_message = f"{cycle1.get_name()} wins!"
                    self._is_game_over = True

        # cycle1 wins if cycle1 hits head2
        if head1.get_position().equals(head2.get_position()):
            score1.reduce_points()
            if score1.get_points() < 1:
                self._game_over_message = f"{cycle2.get_name()} wins!"
                self._is_game_over = True

        # cycle1 wins if cycle2 hits head1
        if head2.get_position().equals(head1.get_position()):
            score2.reduce_points()
            if score2.get_points() < 1:
                self._game_over_message = f"{cycle1.get_name()} wins!"
                self._is_game_over = True

        # Tie the game if score1 and score2 are the same
        if score1.get_points() == 0 and score2.get_points() == 0:
            self._game_over_message = f"Tie!"
            self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns both cycles white if the game is over.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        

        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()
            game_over = End()
            game_over.set_position(position)
            game_over.set_text(self._game_over_message)
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)

            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)