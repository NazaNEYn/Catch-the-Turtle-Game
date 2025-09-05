# Catch the Turtle 🐢

An interactive, "whack-a-mole" style arcade game built entirely using Python's built-in turtle library. This project is designed to be a clear and educational example of object-oriented programming (OOP) principles, state management, and event-driven programming in a simple game environment.


### You can check out the video demo in my [tweet](https://x.com/nazanin_ashrafi/status/1960447274686820423) or you can click on the pic below and watch the demo on youtube.

[![A video thumbnail for a video titled '2024 F1 British Grand Prix: Race Highlights'](https://github.com/user-attachments/assets/58d0e6e6-1cce-4680-bdaa-2c92b2e1f350)](https://www.youtube.com/watch?v=0xpLjfTc8iU)



<hr>



## Features

* **Dynamic Gameplay:** A turtle randomly appears at different locations, and your goal is to click it to score points.

* **Customizable Settings:** At startup, you can set the screen dimensions, the overall game duration, and the speed at which the turtle moves.

* **Real-time Scoreboard:** A dedicated class manages and displays the player's score and a live countdown timer.

* **Responsive Game State:** The turtle's movement and the timer stop automatically when the game ends.

* **Object-Oriented Design:** The code is cleanly separated into different classes, each with a specific responsibility, making it easy to read and extend.


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

## Project Structure & Design
The project is built using an object-oriented approach, where each part of the game is its own class. This separation of concerns makes the code modular and easy to manage.

* `main.py`
The **main entry point** of the program. It handles all initial setup, including getting user input, creating the screen, and instantiating the core objects of the game (`Game`, `Scoreboard`, and `Target`). It then starts the entire process by calling the `game_manager.start_game()` method.

* `game.py`
The **central game manager**. This class acts as a coordinator, connecting the other objects and managing the overall game state. It is responsible for starting the game loops for the timer and target, and more importantly, it sets a one-time "game over" timer. When this timer triggers, the `game_over()` method is called, which then commands the `Scoreboard` and `Target` to stop their loops.

* `scoreboard.py`
This class's sole responsibility is to **manage the display of the score and the timer**. It uses two separate `Turtle` objects to write the score and time on the screen. The countdown is handled by a self-scheduling loop using `ontimer()`.

* `target.py`
This class represents the **interactive game object**. It controls the turtle's random movements and appearance. It also contains the logic to detect a mouse click, update the score by communicating with the `Scoreboard`, and stop its own movement loop when commanded by the `Game` manager.


## Customization

The game is easy to customize. Simply open the relevant `.py` file and change the values to alter the game's appearance and behavior.

* **Change Colors & Shapes:** In `target.py`, you can change the `shape` and `color` variables in the `__init__` method.
* **Adjust Fonts:** In `scoreboard.py`, you can modify the `font` parameter in the `write()` methods to change the text style.
* **Modify Game Logic:**
    * Change the game's duration in `main.py` by altering the `game_timer_seconds` input.
    * Adjust the turtle's appearance speed by changing the `user_timer` input.
    * Change the hit radius for a click in `target.py` by modifying the `distance_from_target < 20` check.


