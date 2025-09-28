from main import Game, Players
from unittest.mock import mock_open, patch, call

def test_should_calculate_total():
    player = Players("player")
    player.scores = [1, 2, 3, 4, 5, 6]
    player.calculate_total()
    assert player.total_score == 21
    
    #Testar om metoden calculate_total räknar ut summan av alla värden i listan scores
        #SETUP:
            # Skapar upp en instans för klassen Player
            # Tilldelar scores till listan scores till ett antal kända värden som tillsammans adderas till 21
        #ACT:
            # Anropar metoden calculate_total
        #ASSERT:
            # Säkerställer att total_score nu faktist är 21

def test_should_reset():
    player = Players("player")
    player.total_score = 21
    player.scores = [1,2,3,4,5,6]
    player.reset()
    assert player.total_score == 0
    assert player.scores == []
   
    #Testa om metoden reset skriver över total_score med 0 och scores med en tom lista
        #SETUP:
            # Skapar en instans av klassen Players
            # Tilldelar ett värde för total_score
            # Tilldelar en lista med element för scores
        #ACT:
            #Anropas metoden reset
        #ASSERT:
            # Säkerställer att total_score nu har fått värde 0
            # Säkerställer att listan score nu är tom

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

    #Testar om metoden calculate_highscore uppdaterar highscore om wins är större än tidigare highscore
    #SETUP:
        #startar upp en instans av klassen Game
        #Ger ett värde till playerns highscore
        #Ger ett värde till dealerns highscore
        #Sätter playerns wins till ett högre värde än highscore
        #Sätter dealerns wins till ett högre värde än highscore
    #ACT:
        #anropar calculate_highscore för playerns räkning
        #anropar calculate_highscore för dealerns räkning
    #ASSERT:
        #Säkerställer att playerns highscore har uppdaterats till det högre värdet
        #Säkerställer att dealerns highscore har uppdaterats till det högre värdet

def test_read_file_exists():
    game = Game()
    mock_data = "7\n5\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        game.read_file("highscores.txt")
    assert game.player.highscore == 7
    assert game.dealer.highscore == 5

    #Testar om metoden read_file läser in och assignar highscores korrekt om en highscores.txt redan existerar
    #SETUP:
        #Startar upp instans av klassen Game
        #Skapar en sträng som låtsas vara två rader med varsin siffra, precis som hur det hade varit i highscores.txt
    #ACT:
        #Ersätter pythons inbyggda open, som letar efter en highscores.txt, med ett kommando att läsa av mock_data istället
        #Anropa read_file
    #ASSERT:
        #Säkerställer att playerns highscore blir 7 (från första raden)
        #Säkerställer att dealerns highscore blir 5 (från andra raden)

def test_read_file_not_exists():
    game = Game()
    with patch("builtins.open", side_effect=FileNotFoundError):
        game.read_file("highscores.txt")
    assert game.player.highscore == 0
    assert game.dealer.highscore == 0

    #Testar om metoden read_file assignar highscore till 0 om en highscores.txt inte existerar
        #SETUP
            #Startar en instans av klassen Game
        #ACT
            #"Mockar open() så att den kastar FileNotFoundError"
            #Anropar read_file
        #ASSERT
            #Säkerställer att playerns highscore sätts till 0
            #Säkerställer att dealerns highscore sätts till 0

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

    #Testa om metoden calculate_highscore låter bli att uppdatera highscore om det är större än wins
        #SETUP
            #Startar en instans av klassen Game
            #tilldelar ett värde till playerns highscore
            #Tilldelar ett värde till dealerns highscore
            #tilldelar ett värde till playerns wins som inte är större än highscore
            #tilldelar ett värde till dealerns wins som inte är större än highscore
        #ACT
            #anropar metoden calculate_highscore för playerns räkning
            #Anropar metoden calculate_highscore för dealerns räkning
        #ASSERT
            #Säkerställer att playerns highscore fortfarande är 10
            #Säkerställer att dealerns highscore fortfarande är 10
            
def test_should_save_file():
    game = Game()
    game.player.highscore = 8
    game.dealer.highscore = 6
    mock = mock_open()
    with patch("builtins.open", mock):
        game.save_file("highscores.txt")
    mock.assert_called_once_with("highscores.txt", "w")
    handle = mock()
    handle.write.assert_has_calls([call("8\n"), call("6\n")])

    #Testar om metoden save_file skriver in highscores i highscores.txt på korrekt sätt
        #SETUP:
            #Startar upp en instans av klassen Game
            #Ger ett värde till playerns highscore
            #Ger ett värde till dealerns highscore
            #skapar upp ett mock-objekt som låtsas vara open()
        #ACT:
            #Ersätter pythons inbyggda open funktion med mock-objektet
            #Kör save_file metoden
        #ASSERT:
            #Kollar att open kördes bara 1 gång och med en parameter för filens namn, dvs "highscores.txt", och en parameter "w" för skrivläge.
            #Hämtar ett mockat fil-handtag, motsvararande det som skulle ha getts av with open(...) as file:, så att det kan låtsas vara file-objektet inuti save_file
            #Kollar att file.write anropas och skapar två rader med players_highscore på första raden och dealer_highscore på andra raden