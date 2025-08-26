from turtle import Turtle
import time


class Scoreboard:
    """
    Manages the game's score and timer display on the screen.
    It tracks the score, handles the countdown, and shows the final score.
    """

    def __init__(self, screen_height, game_time_milliseconds):
        """
        Initializes the scoreboard by setting up the score and time turtles.

        Args:
            screen_height (int): The height of the game screen, used for positioning the score.
            game_time_milliseconds (int): The total duration of the game in milliseconds.
        """
        # --- Score and Time Variables ---
        self.score = 0
        self.game_time_milliseconds = game_time_milliseconds
        self.game_time_seconds = self.game_time_milliseconds / 1000
        self.timer_is_on = True  # This flag controls the timer loop

        # --- Score Turtle Setup ---
        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        score_x_cor = 0
        score_y_cor = (screen_height / 2) - 40
        self.score_turtle.goto(score_x_cor, score_y_cor)
        self.display_score()

        # --- Time Turtle Setup ---
        self.time_turtle = Turtle()
        self.time_turtle.penup()
        self.time_turtle.hideturtle()
        time_x_cor = 0
        time_y_cor = (screen_height / 2) - 80
        self.time_turtle.goto(time_x_cor, time_y_cor)

        self.start_time = time.time()  # Records the time when the game starts

        # Starts the timer loop when the scoreboard object is created
        self.update_time()

    def update_score(self):
        """Increases the score by one and updates the display."""
        self.score += 1
        self.display_score()

    def display_score(self):
        """Clears the previous score and writes the current score on the screen."""
        self.score_turtle.clear()
        self.score_turtle.write(
            f"Score: {self.score}", align="center", font=("lato", 20, "normal")
        )

    def update_time(self):
        """
        Manages the countdown timer.
        It runs repeatedly to update the remaining time on the screen.
        """
        # Checks if the game is still active using the timer_is_on flag
        if self.timer_is_on:
            remaining_time = round(
                self.game_time_seconds - (time.time() - self.start_time)
            )
            self.time_turtle.clear()
            self.time_turtle.write(
                f"Time: {remaining_time}", align="center", font=("lato", 20, "normal")
            )
            # Schedules this method to run again in 1 second
            self.time_turtle.getscreen().ontimer(self.update_time, 1000)

    def stop_timer(self):
        """Stops the timer by changing the control flag to False."""
        self.timer_is_on = False

    def write_final_score(self):
        """Displays the final score in the center of the screen at the end of the game."""
        self.score_turtle.goto(0, 0)
        self.score_turtle.write(
            f"Final Score: {self.score}", align="center", font=("lato", 30, "bold")
        )
