"""
main.py

This script runs the "Catch the Turtle" game.
It initializes the game components (Screen, Scoreboard, Target, and Game manager),
collects user input for game settings, and starts the main game loop.
"""

from turtle import Screen
from target import Target
from scoreboard import Scoreboard
from game import Game
from ascii import ascii_turtle


# --- START-UP AND USER INPUT ---
# Prints a decorative ASCII art message to the console for a stylized start-up.
print("----------------------------------------------------")
print("----------------------------------------------------")
print(ascii_turtle)
print("----------------------------------------------------")
print("----------------------------------------------------")

# Prompts the user to enter game settings and stores their input in variables.
# The input is converted to integers as required for the turtle screen setup.
screen_width = int(input("Enter desired screen width (e.g., 800): \n"))
screen_height = int(input("Enter desired screen height (e.g., 600): \n"))
user_timer = int(input("Enter time between appearances (in milliseconds): \n"))
game_timer_seconds = int(input("Set an overall time for the game (in seconds): \n"))

# --- SCREEN SETUP ---
# Creates the main game screen and configures its properties.
screen = Screen()
screen.colormode(255)
screen.title("Catch the Turtle")
screen.setup(screen_width, screen_height)


# --- OBJECT INITIALIZATION ---
# Creates the Scoreboard object, passing screen height and total game time.
# The game time is converted to milliseconds as required by the Scoreboard class.
game_scoreboard = Scoreboard(screen_height, game_timer_seconds * 1000)

# Creates the Target object, passing all required properties including its appearance timer and a reference to the scoreboard.
game_target = Target(
    "turtle", "deepskyblue4", screen_width, screen_height, user_timer, game_scoreboard
)

# Creates the central Game manager object.
# It receives all other objects (Screen, Target, Scoreboard) to control the game flow.
game_manager = Game(screen, game_target, game_scoreboard, game_timer_seconds)


# --- GAME START ---
# Initiates the game's main loop by calling the 'start_game' method on the game manager.
# This method is responsible for starting the timer and the target's movement.
game_manager.start_game()

# --- MAIN LOOP ---
# The screen listens for events like mouse clicks.
screen.listen()

# Starts the turtle graphics main loop, which keeps the window open.
screen.mainloop()
