# cook your dish here
import random

item_list = ["Rock", "Paper", "Scissor"]

# Welcome message outside the loop
print("--- Welcome to Rock, Paper, Scissor! ---")
print("(Type 'Quit' at any time to exit the game)\n")

while True:
    # 1. Ask user for input
    user_choice = input("Enter your move (Rock, Paper, Scissor) = ").strip().capitalize()
    
    # 2. Check if the user wants to exit
    if user_choice == "Quit":
        print("Thanks for playing! Goodbye.")
        break # This exits the while loop immediately
        
    # 3. Check if the user typed an invalid move
    if user_choice not in item_list:
        print("❌ Invalid move! Please choose Rock, Paper, Scissor, or type Quit.\n")
        continue # This skips the rest of the loop and goes right back to the start
        
    # 4. Computer chooses randomly 
    comp_choice = random.choice(item_list)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    # 5. Determine the winner
    if user_choice == comp_choice:
        print("Both players chose same: Match Tie")
        
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock = Computer wins")
        else:
            print("Rock smashes Scissor = You Win")
            
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper = Computer wins")
        else:
            print("Paper covers Rock = You Win")
        
    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissor Cuts Paper = You Win")
        else:
            print("Rock smashes Scissor = Computer Win")
            
    print() # Prints an empty line to make the next round look clean