'''
jeu de Rock, papper, cissor. 

'''


import random

choix = ["rock", "papper", "siccor"]

def get_choise () : 
    player_choice = input (" choisissez entre (rock, papper, siccor) :" )
    computer_choice = random.choice (choix)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win (player, computer) : 
    print (f"you choise {player} and computer choose {computer}") 
    if player == computer : 
        return print("it's a tie")
    elif player == "rock":
        if computer == "cissor" :
            return print(" rock smash cissor, you WIN !!!")
        else :
            return "papper eat rock, you LOOSE."
    elif player == "cissor":
            if computer == "papper" :
                return print(" cissor cut papper, you WIN !!!")
            else :
                return print(" rock smach cissor, you LOOSE.")
    elif player == "papper":
            if computer == "cissor" :
                return print(" cissor cut paper, you LOOSE.")
            else:
                return print("papper eat rock, you WIN !!!." ) 
    return

choices = get_choise()
result = check_win(choices["player"],choices["computer"])

