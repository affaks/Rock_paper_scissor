import random
import os, platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# waardes/keuzes in spel 
speler_win = 0
computer_win = 0
choices = ("rock", "paper", "scissors")

# dit kijkt of win aantal naar 3 gaat
while speler_win < 3 and computer_win < 3:
    clear()
    print(f"Score - You: {speler_win} | Computer: {computer_win}")

# user input/keuze
    user_choise =input("rock, paper or scissors? ").lower()
    if user_choise not in choices:
        input("Invalid choise, press Enter to continue!")
        continue

# computer keuze
    computer_choise = random.choice(choices)
    print(f"computer chose is : {computer_choise}")

# vergelijkt de keuzes met elkaar
    if user_choise == computer_choise:
        print("It is a tie!")
    elif (user_choise == "rock" and computer_choise == "scissors") or \
         (user_choise == "paper" and computer_choise == "rock") or \
         (user_choise == "scissors" and computer_choise == "paper"):
             speler_win += 1
             print("you won!")
    else:
        computer_win += 1
        print("You lose computer won!")
    
    input("Press Enter to continue...")
        
clear()
#verteld wie er wint bij 3 punten
if speler_win == 3:
    print("congratulations! you won the game!")
else:
    print("computer won the game! better luck next time!")   
      