# NBA-Predictions

This project provides a predictive model for determining whether NBA players will score over or under their points line in upcoming games. It utilizes player statistics, opponent defense rankings, and opponent points per game averages to make predictions.

## Features

- **Recent Performance Analysis**: Calculates a player's recent performance by averaging the points scored in their most recent games.
- **Defense Adjustment**: Adjusts predictions based on the opponent's defense ranking and average points allowed per game, with consideration for the impact of defense on player performance.
- **Predictive Outcome**: Offers a simple "OVER" or "UNDER" prediction for each player's performance relative to the set points line.

## How It Works

1. **Player Data Input**: The script processes a list of dictionaries, each representing a player. Each dictionary contains the player's name, season average points, recent game points, points line for the upcoming game, opponent's defensive ranking, and opponent's average points per game.

2. **Prediction Calculation**:
    - Calculates a player's recent performance average.
    - Normalizes the opponent's defense based on a scale of maximum team average score.
    - Adjusts predictions based on a combined metric of opponent's defensive ranking and normalized defensive performance.

3. **Output**: For each player, the script outputs a prediction of whether they will score "OVER" or "UNDER" their points line, colored in green for "OVER" and red for "UNDER" for easy visualization.

## Installation

No external libraries are required to run this script beyond Python's standard library. Ensure Python is installed on your system.

1. Clone the repository or download the script directly.
2. Ensure the `colors.py` module is in the `support_files` directory as it is required for the script to run properly.

## Usage

To use the script:

1. Modify the `players_data` list in the script to include the players and their respective data you wish to predict for.
2. Run the script in your terminal or command prompt:

```bash
python player_points_prediction.py