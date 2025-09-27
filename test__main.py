from main import Game
from unittest.mock import mock_open, patch

def test_read_file_exists():
    #SETUP
    game = Game()
    mock_data = "7\n5\n"
    #ACT
    with patch("builtins.open", mock_open(read_data=mock_data)):
        game.read_file("highscores.txt")
    #ASSERT
    assert game.player.highscore == 7
    assert game.dealer.highscore == 5


def test_read_file_not_exists():
    #SETUP
    game = Game() 
    #ACT
    with patch("builtins.open", side_effect=FileNotFoundError):
        game.read_file("highscores.txt")
    #ASSERT
    assert game.player.highscore == 0
    assert game.dealer.highscore == 0

def test_highscore_should_update():
    #SETUP
    game = Game()
    game.player.highscore = 5
    game.dealer.highscore = 5
    game.player.wins = 10
    game.dealer.wins = 10
    #ACT
    game.player.calculate_highscore()
    game.dealer.calculate_highscore()
    #ASSERT
    assert game.player.highscore == 10
    assert game.dealer.highscore == 10

def test_highscore_should_not_update():
    #SETUP
    game = Game()
    game.player.highscore = 10
    game.dealer.highscore = 10
    game.player.wins = 5
    game.dealer.wins = 5
    #ACT
    game.player.calculate_highscore()
    game.dealer.calculate_highscore()
    #ASSERT
    assert game.player.highscore == 10
    assert game.dealer.highscore == 10

