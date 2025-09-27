from main import Game, Players
from unittest.mock import mock_open, patch

def test_should_calculate_total():
    player = Players("player")
    player.scores = [1, 2, 3, 4, 5, 6]
    player.calculate_total()
    assert player.total_score == 21

def test_should_reset():
    player = Players("player")
    player.total_score = 21
    player.scores = [1,2,3,4,5,6]
    player.reset()
    assert player.total_score == 0
    assert player.scores == []

def test_highscore_should_update():
    game = Game()
    game.player.highscore = 5
    game.dealer.highscore = 5
    game.player.wins = 10
    game.dealer.wins = 10
    game.player.calculate_highscore()
    game.dealer.calculate_highscore()
    assert game.player.highscore == 10
    assert game.dealer.highscore == 10

def test_read_file_exists():
    game = Game()
    mock_data = "7\n5\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        game.read_file("highscores.txt")
    assert game.player.highscore == 7
    assert game.dealer.highscore == 5

def test_read_file_not_exists():
    game = Game() 
    with patch("builtins.open", side_effect=FileNotFoundError):
        game.read_file("highscores.txt")
    assert game.player.highscore == 0
    assert game.dealer.highscore == 0

def test_highscore_should_not_update():
    game = Game()
    game.player.highscore = 10
    game.dealer.highscore = 10
    game.player.wins = 5
    game.dealer.wins = 5
    game.player.calculate_highscore()
    game.dealer.calculate_highscore()
    assert game.player.highscore == 10
    assert game.dealer.highscore == 10

def test_should_save_file():
    game = Game()
    game.player.highscore = 8
    game.dealer.highscore = 6
    mock = mock_open()
    with patch("builtins.open", mock):
        game.save_file("highscores.txt")
    mock.assert_called_once_with("highscores.txt", "w")
    handle = mock()
    handle.write.assert_any_call("8\n")
    handle.write.assert_any_call("6\n")