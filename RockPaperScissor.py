
import random 

user_win = 0
computer_win = 0

option = ["rock","paper","scissor"]

while True:
    user_input = input("Type rock/paper/scissor or Q to quit:  ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue

    random_no = random.randint(0, 2)
    #0-rock 1-paper 2-scissor
    computer_choice = option[random_no]
    print("computer picked", computer_choice )

    if user_input == "rock" and computer_choice == "scissor":
        print("you won")
        continue
    
    elif user_input == "paper" and computer_choice == "rock":
        print("you won")
        continue

    elif user_input == "scissor" and computer_choice == "paper":
        print("you won")
        continue

    else:
        print("you lose")

print("Bye See u again")







