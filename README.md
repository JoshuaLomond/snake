# 🐍 Snake Game (Python + Pygame)

A simple, classic **Snake** game implemented in Python using [Pygame](https://www.pygame.org/).  
The player controls a snake that grows longer each time it eats food. The objective is to achieve the highest score possible before colliding with yourself (or optionally, with walls).

---

## 🎮 Features

- **Classic Snake Gameplay** – grid-based movement, growing with each food.
- **Scoring System** – score increases by 1 point per food eaten, displayed on-screen.
- **Persistent High Score** – your best score is saved between sessions and shown on the Game Over screen.
- **Dynamic Speed** – snake speed increases slightly every 5 food items.
- **Pause / Resume** – toggle pause anytime with the `P` key.
- **Restart Option** – restart instantly after game over with the `R` key.
- **Quit Anytime** – exit with `Q` or `ESC`.
- **Clean UI** – grid, colored snake (blue head, green body), red food, and HUD.

---

## 🖥️ Requirements

- Python **3.7+**
- Pygame library

Install Pygame via pip:

```bash
pip install pygame
```

## ▶️ How to Run

1. Clone or download this repository.

2. Save the game file (e.g., snake_game.py) into your project folder.

3. Run the script:

```bash
python snake_game.py
```

## 🎹 Controls

| Key          | Action         |
| ------------ | -------------- |
| ⬆ / `W`      | Move up        |
| ⬇ / `S`      | Move down      |
| ⬅ / `A`      | Move left      |
| ➡ / `D`      | Move right     |
| `P`          | Pause / Resume |
| `R`          | Restart game   |
| `Q` or `ESC` | Quit game      |

## 📜 Rules

- Eating food increases your score by 1 and lengthens the snake.

- Every 5 points, the snake’s speed increases slightly.

- Colliding with the wall or yourself ends the game.

- After game over, your highest score is automatically saved in `highscore.txt` (stored in the same folder as the game).

## 🔧 Customization

- You can adjust the game difficulty and visuals easily:

- Window size – change `WINDOW_WIDTH` / `WINDOW_HEIGHT`

- Grid size – change `CELL_SIZE`

- Base speed – change `FPS`

- Snake starting length – change `SNAKE_INITIAL_LENGTH`

- Colors – edit the RGB tuples in the config section

## 🚀 Future Improvements

- Add obstacles / levels

- Toggle wrap-around vs wall-death mode from the menu

- Add sound effects

## 📄 License

This project is released under the MIT License – feel free to modify and share!
