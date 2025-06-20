import random
from colorama import *
# the die roler game
""""""
def Dieroler():
    mony = (50)
    print(Style.BRIGHT + Fore.GREEN  +"wellcome to the die roler game")
    
    while True:
        chose_computer1 = random.randint(1, 6)
        chose_computer2 = random.randint(1, 6)
        com_sum = chose_computer1 + chose_computer2
        Do_play = input(Fore.YELLOW + "Do you want to play the die roler game? (Y/N): ").lower()
    
        if Do_play == "y":
            
            try:
                print("the instructions are simple")
                print(Fore.LIGHTGREEN_EX + "there are lower 1-4,miidle 5-8 and hight 9-12 numbers")
                print(Fore.LIGHTGREEN_EX + "if you chose lower if the sum of computer is 1-4 you win \n if you chose middle if the sum of computer is 5-8 you win \n if you chose hight if the sum of computer is 9-12 you win")
                player_input = int(input(Fore.CYAN + "Enter a number between 1 and 12: "))
                
                if 0< player_input <=12:
                    
                    if player_input == com_sum:
                        print(Fore.YELLOW + "It's a tie! The computer rolled:", com_sum)
                        mony += 20
                        print(Fore.YELLOW + "You add 20$ to your balance \n", "Your current balance is: $", mony)
                        
                    elif ((player_input <= 4 and com_sum <= 4)  or
                        (4<player_input<9 and 4 < com_sum < 9)  or
                        (9<=player_input <=12 and 9<=com_sum <= 12) ): 
                        print(Fore.GREEN + "You win! The computer rolled:", com_sum, "and you add 10$ to your account")
                        mony += 10
                        print(Fore.YELLOW + "Your current balance is: $", mony)
                        print(Fore.YELLOW + "You add 20$ to your balance \n", "Your current balance is: $", mony)
                        
                    else:
                        print(Fore.RED + "You lose! The computer rolled:", com_sum, "and you lose 10$")
                        mony -= 10
                        print(Fore.YELLOW + "Your current balance is: $", mony)
                        
                    if mony == 0:
                        print(Fore.RED + "You have no money left. Game over!")
                        break
                        
            except ValueError:
                print(Fore.RED + "Please enter a valid number between 1 and 6 only numbers")
                continue
            
        elif Do_play == "n":
            print(Fore.YELLOW + "Thank you for playing! Your final balance is: $", mony)
            print(Fore.YELLOW + "Goodbye!")
            break
        
        else:
            print(Fore.BLUE + "Please enter a valid input (Y/N)")
""""""


# the word guesser game

# the number guesser game

# rock,peper,scissors game

# 