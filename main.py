
import random

def play_a_round():
    player_scores = []
    dealer_scores = []
    player_score_sum = 0
    dealer_score_sum = 0
    
    while player_score_sum < 21:
        try:
            roll_or_stop = input("Would you like to roll or stop? Write 'Roll' or 'Stop':\n")
            if roll_or_stop.lower() not in ["roll", "stop"]:
                raise ValueError()
        except ValueError:
            print("No. That is not a valid value. If you wont play right I'm telling mummy")
        if roll_or_stop.lower() == "roll":
            score = random.randint(1,6)
            player_scores.append(score)
            player_score_sum = sum(player_scores)
            print(f"You rolled {score}, your total score is now {player_score_sum}")
            if player_score_sum > 21:
                print(f"Mwuahaha! You've lost, I win!")
                return
            if player_score_sum == 21:
                print("oh... well congratualtions... you win. Whatever")
                return
        elif roll_or_stop.lower() == "stop":
            player_score_sum = sum(player_scores)
            print(f"Okay then, your final score is {player_score_sum}. Now... It's my turn!")
            break

    
    while dealer_score_sum < 17:
        score = random.randint(1,6)
        dealer_scores.append(score)
        dealer_score_sum = sum(dealer_scores)        
        if dealer_score_sum > 21:
            print(f"Aw shucks... I rolled {score}, making my score {dealer_score_sum}. I guess you... win... Whatever")
            return
        elif dealer_score_sum == 21:
            print(f"WOHOO I rolled {score}!! My total is {dealer_score_sum} and I win! In your face!!!")
            return
        else:
            print(f"I've rolled {score}! My total score is now {dealer_score_sum}")
    if dealer_score_sum == player_score_sum:
        print("Hmm I guess we're even... that's no fun.")    
    elif dealer_score_sum > player_score_sum:
        print("BOOM, I win. I'm the BEST!!")
    else:
        print(" Uuuuhm, I guess I have to stop here and admit you win. But you know, it's just a game so whatever... Don't let it get to you're head")
    

while True:
    play_a_round()
    while True:
        try:
            play_again = input("Wanna play again? Write 'Yes' or 'No':\n")
            if play_again.lower() not in ["yes", "no"]:
                raise ValueError()
            break 
        except ValueError:
            print(f"Uuuuuuhm????? Not a valid input!")     
    if play_again.lower() == "no":
        print("Okay, come back and play any time... Coward")
        break
    elif play_again.lower() == "yes":
        print("NICE!!")


