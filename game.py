class Game:
    """
    Manages the overall game state, including starting and ending the game.
    It acts as the central hub for connecting the Screen, Target, and Scoreboard objects.
    """

    def __init__(self, screen, target, scoreboard, game_timer_seconds):
        """
        Initializes the Game manager with all required objects and settings.

        Args:
            screen (Screen): The main turtle screen object.
            target (Target): The target object (the turtle the player clicks).
            scoreboard (Scoreboard): The scoreboard object.
            game_timer_seconds (int): The total duration of the game in seconds.
        """
        self.screen = screen
        self.target = target
        self.scoreboard = scoreboard
        self.game_timer_milliseconds = game_timer_seconds * 1000
        self.game_is_on = True

    def start_game(self):
        """
        Starts the game by beginning the countdown and the target's movement.
        """
        # 1. Start the countdown timer on the scoreboard
        self.scoreboard.update_time()

        # 2. Set a one-time "game over" alarm to end the game after the specified duration
        self.screen.ontimer(self.game_over, self.game_timer_milliseconds)

        # 3. Start the target's movement loop
        self.target.manage_appearance()

    def game_over(self):
        """
        Ends the game by stopping all activity and displaying the final score.
        This method is called by the 'game over' timer.
        """
        # 1. The Game manager tells the scoreboard and target to stop directly.
        self.scoreboard.stop_timer()
        self.target.stop_moving()

        # 2. The Game manager tells the scoreboard to write the final score.
        self.scoreboard.write_final_score()
