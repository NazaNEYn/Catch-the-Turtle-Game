# Catch the Turtle 🐢

A fun and simple "whack-a-mole" style game built with Python's Turtle graphics library. The goal is to click on the turtle as many times as you can before the time runs out!

---

## Features

* **Interactive Gameplay:** Click on the turtle when it appears to score points.
* **Customizable Settings:** Set the screen size, game duration, and turtle appearance speed.
* **Real-time Timer and Score:** A scoreboard tracks your progress and a countdown timer shows how much time you have left.
* **Game Over Screen:** A final score is displayed when the game ends.

---

## How to Run the Game

**1. Prerequisites**

Make sure you have Python installed on your computer. This game uses the built-in `turtle` and `time` libraries, so you don't need to install any external packages.

**2. File Structure**

Ensure all your `.py` files are in the same directory:
```python
/your_project_folder
|-- main.py
|-- game.py
|-- scoreboard.py
|-- target.py
|-- ascii.py  
```

**3. Execution**
Open your terminal or command prompt, navigate to the project folder, and run the `main.py` file:
```python
python main.py
```

The game window will appear and you'll be prompted to enter your game settings directly in the console.

<hr>

## How It Works
The game's functionality is broken down into several classes for clean and organized code:

* `main.py`: The main entry point of the game. It handles user input, initializes all the other classes, and starts the game loop.

* `Game.py`: The central manager. It starts the game, sets a timer for when the game should end, and tells the other classes what to do (e.g., to stop moving or display the final score) when the time runs out.

* `Scoreboard.py`: Manages all the information displayed to the player, including the current score and the real-time countdown timer.

* `Target.py`: Represents the clickable turtle. It controls the turtle's random movements and appearance, and it detects when the player clicks on it.




