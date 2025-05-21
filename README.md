# India States Game 🗺️🇮🇳

Welcome to the **India States Game** — a fun, interactive quiz built with Python's Turtle and Pandas libraries!

### What is this?

It's a simple educational game that challenges you to name all the states of India. Guess a state, and if correct, its name appears on the map. Try to get all the states right!

### How it works

- The game shows a blank map of India.
- You type the name of a state.
- If you’re correct, the state’s name appears on the map at the correct location.
- If you want to quit, just type **Exit** — the game will generate a list of states you missed.

### Features

- Uses Turtle for graphical display.
- Uses Pandas to manage state data.
- Interactive input with feedback.
- Saves missed states to a CSV for later learning.

---

## Files

- `main.py` — the main game script.
- `india_states.csv` — contains states and their coordinates.
- `blank_india_img.gif` — blank India map image used as background.
- `get_coordinates.py` — helper script to get coordinates by clicking on the map.

---

## How to run

1. Make sure you have Python installed (preferably 3.7+).
2. Install Pandas if you haven't: `pip install pandas`
3. Run the main game:  
   ```bash
   python main.py
