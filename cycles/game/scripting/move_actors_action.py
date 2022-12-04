from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """
    MoveActorsAction gets all the actors from the cast. It then loops through every actor in actors and calls the move_next() method on each one.
    """

    def execute(self, cast, script):
        """
        Execute MoveActorsAction with cast and script.

        Args:
           cast: all actors
           script: all actions
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()