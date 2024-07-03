# Simple Snake Game

This is a simple snake game built using Python's `turtle` module. The player controls the snake using the arrow keys, guiding it to eat the food that appears on the screen. Each time the snake eats the food, it grows longer, and the player's score increases. The game ends if the snake collides with the wall or with itself.

## Features

- Control the snake using the arrow keys.
- Snake grows longer each time it eats the food.
- Score increases each time the snake eats the food.
- Game ends if the snake collides with the wall or with itself.
- Display a game over message when the game ends.

## Requirements

- Python 3.x
- `turtle` module (comes pre-installed with Python)

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/gitkuangy/snake-game.git
    cd snake-game
    ```

2. Necessary files for the game:
    - 'main.py' for running the game
    - `snake.py` for the Snake class
    - `food.py` for the Food class
    - `scoreboard.py` for the Scoreboard class

3. Run the program:
    ```sh
    python main.py
    ```

4. Use the arrow keys to control the snake and try to eat the food while avoiding collisions with the wall and the snake's own body.

## Example

```plaintext
Use the arrow keys to control the snake:
- Up arrow to move up
- Down arrow to move down
- Left arrow to move left
- Right arrow to move right
