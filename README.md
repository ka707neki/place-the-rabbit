# 🐇 Place the Rabbit

A tiny terminal game written in Python. You get a 3×3 grid of grass, and you decide where the rabbit goes.

```
Current Field:
🌿 🌿 🌿
🌿 🌿 🌿
🌿 🌿 🌿
```

## ✨ Features

- 3×3 emoji grid rendered directly in the terminal
- Position input as two digits: row then column (e.g. `32` = row 3, column 2)
- Input validation for wrong format and out-of-range positions
- Quit anytime with `q`, `quit`, or `exit`
- Zero dependencies: pure Python standard library

## 🛠 Requirements

- Python 3.6 or newer
- A terminal that can display emoji

## 🚀 Installation

```bash
git clone https://github.com/USERNAME/place-the-rabbit.git
cd place-the-rabbit
```

## ▶️ Usage

```bash
python3 place_the_rabbit.py
```

Enter the position as `RowColumn`, where both values are between 1 and 3:

| Input | Meaning            |
|-------|--------------------|
| `11`  | Top-left corner    |
| `22`  | Center             |
| `33`  | Bottom-right corner|
| `q`   | Quit the game      |

### Example session

```
Welcome to Place the Rabbit!

Current Field:
🌿 🌿 🌿
🌿 🌿 🌿
🌿 🌿 🌿

Where should the rabbit go? (RowCol e.g., 11, 32) or 'q' to quit: 22

Success!
🌿 🌿 🌿
🌿 🐇 🌿
🌿 🌿 🌿
```

## 🧠 How it works

1. The field is a list of 3 lists, each holding 3 🌿 cells.
2. The input is cleaned with `.strip().lower()`, then checked: exactly two digits, each between 1 and 3.
3. The 1-based position is converted to a 0-based index and the 🐇 replaces the 🌿 there.
4. Every round starts with a fresh field.

## 🗺 Ideas for the future

- [ ] Keep the rabbit on the board and let it move between rounds
- [ ] Add a second player or a "find the hidden rabbit" mode
- [ ] Bigger grids (4×4, 5×5)

## 📄 License

Released under the [MIT License](LICENSE).
