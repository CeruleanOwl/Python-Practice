'''Global Variables'''
rockC = False
scissorsC = False
paperC = False
rockU = False
scissorsU = False
paperU = False

#computer logic
def computer_choice():
    #import random module
    import random
    #request global variables
    global rockC
    global paperC
    global scissorsC

    #Random int generator between 1-3
    computer = random.randint(1,3)

    #Conditions for which random number is selected
    if computer == 1:
        rockC = True
        print('Computer chose rock.')
    elif computer == 2:
        paperC = True
        print('Computer chose paper.')
    elif computer == 3:
        scissorsC = True
        print('Computer chose scissors.')

#player logic
def player_choice():
    #request global variables
    global rockU
    global paperU
    global scissorsU

    #default choice to zero and requesting parameters to True
    choice = 0
    requesting = True

    #Logic for user selecting choice and protecting from bad user selections
    while requesting:
        try:
            while choice not in range(1,4):
                choice = int(input('Please select Rock(1), Paper(2), or Scissors(3).\n'))
        except ValueError:
            print('That wasn\'t a selection. Try again.')
        if choice in range(1,4):
            requesting = False
    
    #Conditions based on user selection
    if choice == 1:
        rockU = True
        print('You chose rock.')
    elif choice == 2:
        paperU = True
        print('You chose paper.')
    elif choice == 3:
        scissorsU = True
        print('You chose scissors.')

#Decides who wins
def win_condition():
    #request global variables
    global rockC
    global rockU
    global paperC
    global paperU
    global scissorsC
    global scissorsU

    #Rock user condition against computer conditions.
    if (rockU == True) and (rockC == True):
        print('It was a draw.')
    elif (rockU == True) and (paperC == True):
        print('You Lose!')
    elif (rockU == True) and (scissorsC == True):
        print('You Win!')
    elif (paperU == True) and (paperC == True):
        print('It was a draw.')
    elif (paperU == True) and (rockC == True):
        print('You win!')
    elif (paperU == True) and (scissorsC == True):
        print('You lose!')
    elif (scissorsU == True) and (scissorsC == True):
        print('It was a draw.')
    elif (scissorsU == True) and (paperC == True):
        print('You win!')
    elif (scissorsU == True) and (rockC == True):
        print('You lose!')

#game logic
def play_game():
    player_choice()

    computer_choice()

    win_condition()

play_game()

