from turtle import Turtle
import random


class Target:
    """
    Represents the interactive turtle that the player clicks on.
    It handles its own movement, appearance, and click events.
    """

    def __init__(self, shape, color, screen_width, screen_height, timer, scoreboard):
        """
        Initializes the target turtle with its properties and screen boundaries.

        Args:
            shape (str): The shape of the turtle.
            color (str): The color of the turtle.
            screen_width (int): The width of the game screen.
            screen_height (int): The height of the game screen.
            timer (int): The time in milliseconds between each appearance.
            scoreboard (Scoreboard): A reference to the scoreboard object to update the score.
        """
        self.turtle = Turtle()
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.timer = timer
        self.scoreboard = scoreboard
        self.is_moving = True  # This flag controls the movement loop

        self.turtle.penup()
        self.turtle.hideturtle()

        # Binds the mouse click event to the was_clicked method
        self.turtle.onclick(self.was_clicked)

    def random_appearances(self):
        """Moves the turtle to a new random location on the screen."""
        x_limit = int(self.screen_width / 2.1)
        y_limit = int(self.screen_height / 2.1)

        random_x = random.randint(-x_limit, x_limit)
        random_y = random.randint(-y_limit, y_limit)
        print(f"Target's coordinates: {random_x, random_y}")

        self.turtle.goto(random_x, random_y)

        # Refreshes the screen to show the new turtle position
        self.turtle.getscreen().update()

    def hide_turtle(self):
        """Hides the turtle from the screen."""
        self.turtle.hideturtle()

    def show_turtle(self):
        """Displays the turtle on the screen."""
        self.turtle.showturtle()

    def manage_appearance(self):
        """
        Manages the turtle's repeated appearance and movement.
        It runs repeatedly to move the turtle to a new random spot.
        """
        # Checks if the game is still active using the is_moving flag
        if self.is_moving:
            self.turtle.hideturtle()
            self.random_appearances()
            self.turtle.showturtle()
            # Schedules this method to run again after the specified timer
            self.turtle.getscreen().ontimer(self.manage_appearance, self.timer)
        else:
            # Hides the turtle when the game is over
            self.turtle.hideturtle()

    def stop_moving(self):
        """Stops the movement loop by changing the control flag to False."""
        self.is_moving = False

    def was_clicked(self, x, y):
        """
        Handles the event when the turtle is clicked.
        It checks if the click was close enough to be a "hit" and updates the score.
        """
        distance_from_target = self.turtle.distance(x, y)

        if distance_from_target < 20:
            # Writes "Hit!" on the screen briefly
            self.turtle.write("Hit!", align="center", font=("lato", 12, "normal"))
            print(f"Click's coordinates: {distance_from_target}")
            self.scoreboard.update_score()
            # Schedules the text to be cleared after 600 milliseconds
            self.turtle.getscreen().ontimer(self.clear_hit_text, 600)

    def clear_hit_text(self):
        """Clears the "Hit!" text from the screen."""
        self.turtle.clear()
