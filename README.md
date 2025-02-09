# Country-Capital Guessing Game

This Python game tests your knowledge of countries and their capitals. You are given either a country or a capital and must correctly identify its corresponding capital or country. The game tracks your mistakes and increases the probability of showing commonly mistaken pairs. Mistakes are saved across sessions, but you can reset them if desired.

## Features
- Randomly generates country-capital questions.
- Tracks errors and increases the chance of repeated mistakes appearing.
- Uses fuzzy matching to allow for minor spelling mistakes.
- Saves progress between sessions.
- Allows quitting at any time while retaining progress.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.7). Then, install the required dependencies:

```sh
pip install numpy fuzzywuzzy python-Levenshtein
```

### Dataset
This project uses `pays-json-master` for the list of country-capital pairs.

## Usage
1. Ensure `liste-197-etats-2020.csv` is available in the correct directory.
2. Run the script:

```sh
python geography_game.py
```

3. Answer the prompted questions. Type `quit` to exit and save your progress.

## Configuration
- The game state (error tracking) is saved in `geography_game_state.json`.
- Modify `similarity_threshold` in `check_correct_answer` to adjust answer tolerance.

## Example
### Question:
```
What is the capital of France?
```
### Answer:
```
Paris
```
(If a typo is made, it will still be considered correct within the similarity threshold.)

## License
This project is licensed under the MIT License.

## Author
[Your Name]

