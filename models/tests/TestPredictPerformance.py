# Tests for the predict_performance algorithm

import unittest
from models.scripts.points_prediction_model_1 import predict_performance, Colors


class TestPredictPerformance(unittest.TestCase):

    def test_over_prediction(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 25.5,
            "points_recent_games": [26, 27, 28, 29, 30],
            "points_line": 25,
            "opp_position_defense": 15,
            "opp_points_per_game_avg": 110
        }
        self.assertEqual(predict_performance(player_data), f"{Colors.GREEN}OVER{Colors.ENDC}")

    def test_under_prediction(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 25.5,
            "points_recent_games": [20, 21, 22, 23, 24],
            "points_line": 25,
            "opp_position_defense": 15,
            "opp_points_per_game_avg": 110
        }
        self.assertEqual(predict_performance(player_data), f"{Colors.RED}UNDER{Colors.ENDC}")

    # High Scoring Player Against Weak Defense
    def test_high_score_weak_defense(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 28.2,
            "points_recent_games": [30, 31, 29, 32, 28],
            "points_line": 27.5,
            "opp_position_defense": 27,
            "opp_points_per_game_avg": 120
        }
        self.assertEqual(predict_performance(player_data), f"{Colors.GREEN}OVER{Colors.ENDC}")

    # Consistent Player Against Average Defense
    def test_consistent_player_average_defense(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 25.3,
            "points_recent_games": [25, 25, 25, 25, 25],
            "points_line": 24.5,
            "opp_position_defense": 15,
            "opp_points_per_game_avg": 115
        }
        self.assertEqual(predict_performance(player_data), f"{Colors.GREEN}OVER{Colors.ENDC}")

    # Slumping Player Against Strong Defense
    def test_slumping_player_strong_defense(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 22.6,
            "points_recent_games": [15, 16, 14, 17, 15],
            "points_line": 21.5,
            "opp_position_defense": 4,
            "opp_points_per_game_avg": 110
        }
        self.assertEqual(predict_performance(player_data), f"{Colors.RED}UNDER{Colors.ENDC}")

    # Elite Scorer Against Elite Defense
    def test_elite_player_elite_defense(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 32.7,
            "points_recent_games": [34, 33, 35, 34, 36],
            "points_line": 31.5,
            "opp_position_defense": 1,
            "opp_points_per_game_avg": 106
        }
        self.assertEqual(predict_performance(player_data), f"{Colors.GREEN}OVER{Colors.ENDC}")

    def test_case_equal_prediction(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 25,
            "points_recent_games": [25, 25, 25, 25, 25],
            "points_line": 25,
            "opp_position_defense": 15,
            "opp_points_per_game_avg": 110
        }
        # If the prediction is equal to the points line, it's considered UNDER
        self.assertEqual(predict_performance(player_data), f"{Colors.RED}UNDER{Colors.ENDC}")

    def test_empty_recent_games(self):
        player_data = {
            "player_name": "Test Player",
            "points_season_avg": 25,
            "points_recent_games": [],
            "points_line": 25,
            "opp_position_defense": 15,
            "opp_points_per_game_avg": 110
        }
        with self.assertRaises(ZeroDivisionError):
            predict_performance(player_data)


if __name__ == '__main__':
    unittest.main()
