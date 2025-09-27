
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
                print(f"Your previous highscore i {self.player.highscore} and my previous highscore is {self.dealer.highscore}")
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

    def play_a_round(self):
        
        #Players turn
        while self.player.total_score < 21:
            try:
                roll_or_stop = input("Would you like to roll or stop? Write 'Roll' or 'Stop':\n")
                if roll_or_stop.lower() not in ["roll", "stop"]:
                    raise ValueError()
            except ValueError:
                print("No. That is not a valid value. If you wont play right I'm telling mummy")
            if roll_or_stop.lower() == "roll":
                self.player.roll()
                self.player.calculate_total()
                if self.player.total_score > 21:
                    print(f"Mwuahaha! You've lost, I win!")
                    self.dealer.wins += 1
                    self.player.reset()
                    self.dealer.reset()
                    return
                if self.player.total_score == 21:
                    print("oh... well congratualtions... you win. Whatever")
                    self.player.wins += 1
                    self.player.reset()
                    self.dealer.reset()
                    return
            elif roll_or_stop.lower() == "stop":
                print(f"Okay then, your final score is {self.player.total_score}. Now it's my turn!")
                break

        #Dealers turn
        while self.dealer.total_score < 17:
            self.dealer.roll()
            self.dealer.calculate_total()     
            if self.dealer.total_score > 21:
                print(f"Aw shucks... I guess you... win... Whatever")
                self.player.wins += 1
                self.player.reset()
                self.dealer.reset()
                return
            elif self.dealer.total_score == 21:
                print(f"WOHOO!! I win! In your face!!!")
                self.dealer.wins += 1
                self.player.reset()
                self.dealer.reset()
                return
        
        # Comparing scores
        if self.dealer.total_score == self.player.total_score:
            print("Hmm I guess we're even... that's no fun.")    
        elif self.dealer.total_score > self.player.total_score:
            self.dealer.wins += 1
            print(f"BOOM, I win. I'm the BEST!!")
        else:
            self.player.wins += 1
            print(f"Uuuuhm, I guess I have to stop here and admit you win. But it's just a game so whatever... Don't let it get to you're head")
        
        #Resetting scores
        self.player.reset()
        self.dealer.reset()

game = Game()
play_game = True
while play_game:
    game.play_a_round()
    while True:
        try:
            answer = input("Wanna play another round? Write 'Yes' or 'No':\n")
            if answer.lower() not in ["yes", "no"]:
                raise ValueError()
            break 
        except ValueError:
            print(f"Uuuuuuhm????? Not a valid input! Write 'yes' or 'no'")     
    if answer.lower() == "yes":
        print(f"NICE!! So you've won {game.player.wins} times and I've won {game.dealer.wins}")
    elif answer.lower() == "no":
        print(f"Okay, then we'll leave it at...\nplayer: {game.player.wins}\ndealer: {game.dealer.wins}. Coward")
        game.player.calculate_highscore()
        game.dealer.calculate_highscore()
        game.save_file("highscores.txt")
        play_game = False
        break


