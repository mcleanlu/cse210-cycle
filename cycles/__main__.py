import constants

from game.casting.cast import Cast
from game.casting.cycle import Cycle
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # create two cycles for two players
    cycle1 = Cycle(Point(int(constants.MAX_X - 600), int(constants.MAX_Y / 2)))
    cycle2 = Cycle(Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
    cycle1.set_cycle_color(constants.GREEN)
    cycle2.set_cycle_color(constants.RED)
    cycle_one_name = input("\n\nPlease enter player 1 name: " + "\n\n")
    cycle_two_name = input("\n\nPlease enter player 2 name: " + "\n\n")
    cycle1.set_name(cycle_one_name)
    cycle2.set_name(cycle_two_name)

    # create the cast
    cast = Cast()
    score1 = Score()
    score2 = Score()
    score1.set_position(Point(constants.MAX_X - 850, 0))
    score2.set_position(Point(constants.MAX_X - 200, 0))
    score1.add_points(3)
    score2.add_points(3)
    score1.set_player_name(cycle_one_name)
    score2.set_player_name(cycle_two_name)
    cast.add_actor("cycle_one", cycle1)
    cast.add_actor("cycle_two", cycle2)
    cast.add_actor("score1", score1)
    cast.add_actor("score2", score2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()