# Player points over/under model

from support_files.colors import Colors

# Data structure for player performance and opponent defensive stats
players_data = [
    {
        "player_name": "Jalen Brunson",
        "points_season_avg": 27.5,
        "points_recent_games": [21, 33, 27, 39, 27],
        "points_line": 28.5,

        "opp_position_defense": 15,
        "opp_points_per_game_avg": 110.6,

        "home_game": True,  # Indicates if the player's team is playing at home
        "back_to_back": False,  # Indicates if this game is the second in two consecutive days
    },
    {
        "player_name": "Jayson Tatum",
        "points_season_avg": 27.1,
        "points_recent_games": [25, 20, 41, 26, 35],
        "points_line": 26.5,

        "opp_position_defense": 14,
        "opp_points_per_game_avg": 109.7,

        "home_game": False,  # Indicates if the player's team is playing at home
        "back_to_back": False,  # Indicates if this game is the second in two consecutive days
    },
    {
        "player_name": "Jaylen Brown",
        "points_season_avg": 22.0,
        "points_recent_games": [21, 19, 20, 18, 15],
        "points_line": 19.5,

        "opp_position_defense": 14,
        "opp_points_per_game_avg": 109.7,

        "home_game": False,  # Indicates if the player's team is playing at home
        "back_to_back": False,  # Indicates if this game is the second in two consecutive days
    },
    {
        "player_name": "Anthony Edwards",
        "points_season_avg": 26.3,
        "points_recent_games": [28, 34, 41, 23, 26],
        "points_line": 26.5,


        "opp_position_defense": 26,
        "opp_points_per_game_avg": 115.7,

        "home_game": True,  # Indicates if the player's team is playing at home
        "back_to_back": True,  # Indicates if this game is the second in two consecutive days
    },
    {
        "player_name": "Karl-Anthony Towns",
        "points_season_avg": 22.5,
        "points_recent_games": [22, 23, 13, 24, 19],
        "points_line": 21.5,


        "opp_position_defense": 9,
        "opp_points_per_game_avg": 115.7,

        "home_game": True,  # Indicates if the player's team is playing at home
        "back_to_back": True,  # Indicates if this game is the second in two consecutive days
    },
    {
        "player_name": "Mikal Bridges",
        "points_season_avg": 21.7,
        "points_recent_games": [21, 10, 27, 14, 26],
        "points_line": 21.5,


        "opp_position_defense": 5,
        "opp_points_per_game_avg": 106.8,

        "home_game": False,  # Indicates if the player's team is playing at home
        "back_to_back": False,  # Indicates if this game is the second in two consecutive days
    }
]

# Constants for calculations
DEFENSE_RANKING_MULTIPLIER = 0.1
DEFENSE_POINTS_SCALE_FACTOR = 11
MAX_DEFENSE_RANKING = 30  # Lower number indicates a better defense
MAX_TEAM_AVERAGE_SCORE = 123.8
HOME_GAME_ADJUSTMENT = 2.5  # Points adjustment for playing at home
BACK_TO_BACK_PENALTY = -3  # Points penalty for playing back-to-back games


# Function to predict over/under for a player
# There are 30 teams and a lower 'opp_position_defense' number indicates a better defense
def predict_performance(player_data):
    """
    Predicts whether a player will score over or under their points line based on recent performance,
    opponent's defense, and additional factors like home vs. away games and back-to-back games.

    Parameters:
    - player_data (dict): Contains the player's stats and the opponent's defensive stats,
                          as well as flags for home games and back-to-back games.

    Returns:
    - str: Indicates whether the player is predicted to score over or under their points line, with color coding.
    """
    # Calculate recent average points scored
    recent_avg = sum(player_data["points_recent_games"]) / len(player_data["points_recent_games"])

    # Normalize opponent's defense to a 0-1 scale
    normalized_opp_defense = (MAX_TEAM_AVERAGE_SCORE - player_data["opp_points_per_game_avg"]) / MAX_TEAM_AVERAGE_SCORE

    # Adjust based on opponent defense ranking
    defense_ranking_adjustment = (MAX_DEFENSE_RANKING - player_data["opp_position_defense"]) * DEFENSE_RANKING_MULTIPLIER
    # Scale up the normalized opponent defense for impact
    defense_points_adjustment = normalized_opp_defense * DEFENSE_POINTS_SCALE_FACTOR

    # Total defense adjustment
    defense_adjustment = defense_ranking_adjustment + defense_points_adjustment

    # Adjust for home game advantage or back-to-back game penalty
    if player_data["home_game"]:
        defense_adjustment += HOME_GAME_ADJUSTMENT
    if player_data["back_to_back"]:
        defense_adjustment += BACK_TO_BACK_PENALTY

    # Final prediction with all adjustments
    adjusted_prediction = recent_avg + defense_adjustment

    # Determine over or under prediction with color coding
    if adjusted_prediction > player_data["points_line"]:
        player_prediction = f"{Colors.GREEN}OVER{Colors.ENDC}"
    else:
        player_prediction = f"{Colors.RED}UNDER{Colors.ENDC}"

    return player_prediction


# Iterate over each player and print predictions
for player in players_data:
    prediction = predict_performance(player)
    print(f"{player['player_name']}: is predicted to score {prediction} the points line of {player['points_line']}")
