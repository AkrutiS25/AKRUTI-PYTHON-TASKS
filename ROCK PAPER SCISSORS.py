import random

def play_game():
    print("Lets Begin Rock , Paper, Scissors!")
    print("GUIDELINES FOR THE GAME \n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

    

    user_selected_choice = int(input("Type 1. Rock, 2. Paper, or 3. Scissors: "))
    
    if (user_selected_choice > 3 or user_selected_choice < 1):
        print("INVALID NUMBER ENTERED . PLEASE CHECK PROPERLY")
    else:
        computer_selected_choice = random.randint(1, 3)
        print("Computer Chose : ", computer_selected_choice)

        if (user_selected_choice == computer_selected_choice):
            print("It's a tie!")
        elif (user_selected_choice == 1 and computer_selected_choice == 3):
            print("YOU WIN as The ROCK BEATS SCISSORS!")
        elif (computer_selected_choice == 1 and user_selected_choice == 3):
            print("You LOSE as The SCISSORS CAN'T BEAT ROCK!")
        elif (user_selected_choice > computer_selected_choice):
            print("YOU WIN")
        else:
            print("YOU LOSE")

while True:
    play_game()
    play_again = input("Do you want to play again? (YES/NO): ")
    if play_again.lower() != "yes":
        break



    
    
