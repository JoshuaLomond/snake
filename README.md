# Snake Game

A classic Snake game implemented in Python using the Pygame library.

## Features

- **Classic Gameplay**: Navigate the snake to eat food and grow in length.
- **Scoring System**: Earn points for every piece of food eaten.
- **High Score**: Your highest score is saved and persists across game sessions.
- **Smooth Controls**: Responsive arrow key controls for precise movement.
- **Polished UI**: Clean Start and Game Over screens.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/JoshuaLomond/snake.git
   cd snake
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the game using the following command:

```bash
python main.py
```

## Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Any Key**: Start the game / Restart after Game Over

## Game Rules

- Eat the red food squares to grow and earn points.
- Avoid hitting the walls or your own tail.
- The game ends if you collide with a wall or yourself.
- Try to beat your high score!

## Future Improvements

- Add sound effects and music
- Add a pause menu
- Add a settings menu
- Add a main menu

## License

This project is open source and available under the [MIT License](LICENSE).
