
import random

class Players:
    def __init__(self, name):
        self.scores = []
        self.total_score = 0
        self.wins = 0
        self.highscore = 0
        self.name = name

    def roll(self):
        score = random.randint(1,6)
        self.scores.append(score)
        print(f"The dice rolled: {score}")

    def calculate_total(self):
        self.total_score = sum(self.scores)
        print(f"Total score: {self.total_score}")

    def calculate_highscore(self):
        if self.wins > self.highscore:
            self.highscore = self.wins
            print(f"New {self.name} highscore: {self.highscore}")

    def reset(self):
        self.total_score = 0
        self.scores = []

class Game:
    def __init__(self):
        self.player = Players("player")
        self.dealer = Players("dealer")
        self.read_file("highscores.txt")
    
    def read_file(self, name):
        print("Loading previous highscores")
        try:
            with open(name) as file:
                lines = list(map(lambda row: row.strip(), file))
                self.player.highscore = int(lines[0])
                self.dealer.highscore = int(lines[1])
                print(f"Your previous highscore is {self.player.highscore} and my previous highscore is {self.dealer.highscore}")
        except FileNotFoundError:
            self.player.highscore = 0
            self.dealer.highscore = 0
            print(f"No previous highscore recorded, starting with clean slate\nPlayer: {self.player.wins}\nDealer: {self.dealer.wins}")
            return []
    
    def save_file(self, name):
        print("Updating highscores file...")
        try:
            with open(name, "w") as file:
                file.write(f"{self.player.highscore}\n")
                file.write(f"{self.dealer.highscore}\n")

        except OSError:
            print("File could not be updated for some reason")
        else:
            print("Highscores file has been updated")

    def ask_input(self, prompt, valid_options):
        while True:
            try:
                answer = input(prompt).lower()
                if answer not in valid_options:
                    raise ValueError
                return answer
            except ValueError:
                print("That is not a valid value. If you wont play right I'm telling mummy!")

    def players_turn(self):
        while self.player.total_score < 21:
            roll_or_stop = self.ask_input("Would you like to roll or stop? Write 'Roll' or 'Stop':\n", ["roll", "stop"])
            if roll_or_stop == "roll":
                self.player.roll()
                self.player.calculate_total()
                if self.player.total_score > 21:
                    return "bust"
                if self.player.total_score == 21:
                    return "win"
            else:
                print(f"Okay then, your final score is {self.player.total_score}. Now it's my turn!")
                break
        return "stop"

    def dealers_turn(self):
        while self.dealer.total_score < 17:
            self.dealer.roll()
            self.dealer.calculate_total()     
            if self.dealer.total_score > 21:
                return "bust"
            elif self.dealer.total_score == 21:
                return "win"
        return "stop"
        
    def comparing_scores(self, players_result, dealers_result):
        #Player scores over 21
        if players_result == "bust":
            self.dealer.wins += 1
            print("Mwuahaha! You've lost, I win!")
            self.player.reset()
            self.dealer.reset()
            return
        # Dealer scores over 21
        elif dealers_result == "bust":
            self.player.wins += 1
            print(f"Aw shucks... I guess you... win... Whatever")
            self.player.reset()
            self.dealer.reset()
            return
        #Player scores 21
        elif players_result == "win":
            self.player.wins += 1
            print("oh... well congratualtions... you win. Whatever")
            self.player.reset()
            self.dealer.reset()
            return
        #Dealer scores 21
        elif dealers_result == "win":
            self.dealer.wins +=1
            print(f"WOHOO!! I win! In your face!!!")
            self.player.reset()
            self.dealer.reset()
            return
        #Tie
        elif self.dealer.total_score == self.player.total_score:
            print("Hmm it's a tie... that's no fun.") 
        #Dealer scores higher than player
        elif self.dealer.total_score > self.player.total_score:
            self.dealer.wins += 1
            print(f"BOOM, I win. I'm the BEST!!")
        #Player scores higher than dealer
        else:
            self.player.wins += 1
            print(f"Uuuuhm, I guess I have to stop here and admit you win. But it's just a game so whatever... Don't let it get to you're head")   
        #Resetting scores
        self.player.reset()
        self.dealer.reset()

if __name__ == "__main__":
    game = Game()
    play_game = True
    while play_game:
        players_result = game.players_turn()
        if players_result in ["bust", "win"]:
            dealers_result = "stop"
        else:
            dealers_result = game.dealers_turn()
        game.comparing_scores(players_result, dealers_result)
        while True:
            play_again = game.ask_input("Wanna play another round? Write 'Yes' or 'No':\n", ["yes", "no"])
            if play_again == "yes":
                print(f"NICE!! So you've won {game.player.wins} times and I've won {game.dealer.wins} times")
                break
            elif play_again == "no":
                print(f"Okay, then we'll leave it at...\nplayer: {game.player.wins}\ndealer: {game.dealer.wins}")
                game.player.calculate_highscore()
                game.dealer.calculate_highscore()
                game.save_file("highscores.txt")
                play_game = False
                break