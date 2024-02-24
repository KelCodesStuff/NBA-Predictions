# Player points over/under model

from support_files.colors import Colors

# List of dictionaries containing player stats and opponent stats
players_data = [
    {
        "player_name": "Jalen Brunson",
        "points_season_avg": 27.5,
        "points_recent_games": [21, 33, 27, 39, 27],
        "points_line": 28.5,
        "opp_position_defense": 15,
        "opp_points_per_game_avg": 110.6,
    },
    {
        "player_name": "Jayson Tatum",
        "points_season_avg": 27.1,
        "points_recent_games": [25, 20, 41, 26, 35],
        "points_line": 26.5,
        "opp_position_defense": 14,
        "opp_points_per_game_avg": 109.7,
    },
    {
        "player_name": "Jaylen Brown",
        "points_season_avg": 22.0,
        "points_recent_games": [21, 19, 20, 18, 15],
        "points_line": 19.5,
        "opp_position_defense": 14,
        "opp_points_per_game_avg": 109.7,
    },
    {
        "player_name": "Anthony Edwards",
        "points_season_avg": 26.3,
        "points_recent_games": [28, 34, 41, 23, 26],
        "points_line": 26.5,
        "opp_position_defense": 26,
        "opp_points_per_game_avg": 115.7,
    },
    {
        "player_name": "Karl-Anthony Towns",
        "points_season_avg": 22.5,
        "points_recent_games": [22, 23, 13, 24, 19],
        "points_line": 21.5,
        "opp_position_defense": 9,
        "opp_points_per_game_avg": 115.7,
    },
    {
        "player_name": "Mikal Bridges",
        "points_season_avg": 21.7,
        "points_recent_games": [21, 10, 27, 14, 26],
        "points_line": 21.5,
        "opp_position_defense": 5,
        "opp_points_per_game_avg": 106.8,
    }
]

# Constants for calculations
DEFENSE_RANKING_MULTIPLIER = 0.1
DEFENSE_POINTS_SCALE_FACTOR = 11
MAX_DEFENSE_RANKING = 30  # the lower the number the better the defense
MAX_TEAM_AVERAGE_SCORE = 123.8


# Function to predict over/under for a player
# There are 30 teams and a lower 'opp_position_defense' number indicates a better defense
def predict_performance(player_data):
    """
    Predicts whether a player will score over or under their points line based on their recent performance and the opponent's defense.

    Parameters:
    - player_data (dict): A dictionary containing the player's stats and the opponent's defensive stats.

    Returns:
    - str: A string indicating whether the player is predicted to score over or under their points line.
    """
    recent_avg = sum(player_data["points_recent_games"]) / len(player_data["points_recent_games"])

    # Normalize the opponent's points per game to a scale of 0-1
    normalized_opp_defense = (MAX_TEAM_AVERAGE_SCORE - player_data["opp_points_per_game_avg"]) / MAX_TEAM_AVERAGE_SCORE

    # Combine normalized opponent defense with position defense for adjustment
    defense_ranking_adjustment = (MAX_DEFENSE_RANKING - player_data["opp_position_defense"]) * DEFENSE_RANKING_MULTIPLIER
    defense_points_adjustment = normalized_opp_defense * DEFENSE_POINTS_SCALE_FACTOR  # Scale up to make impactful

    defense_adjustment = defense_ranking_adjustment + defense_points_adjustment  # Adjust prediction based on both metrics

    adjusted_prediction = recent_avg + defense_adjustment  # Adjust prediction

    if adjusted_prediction > player_data["points_line"]:
        player_prediction = f"{Colors.GREEN}OVER{Colors.ENDC}"
    else:
        player_prediction = f"{Colors.RED}UNDER{Colors.ENDC}"

    return player_prediction


# Iterate over each player and print predictions
for player in players_data:
    prediction = predict_performance(player)
    print(f"{player['player_name']}: is predicted to score {prediction} the points line of {player['points_line']}")
