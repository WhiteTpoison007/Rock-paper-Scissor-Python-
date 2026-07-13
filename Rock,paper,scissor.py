import random

# Game setup
item_list = ["Rock", "Paper", "Scissor"]
player_score = 0
computer_score = 0

print("🎮 WELCOME TO THE ROCK, PAPER, SCISSORS GAME! 🎮")
print("👉 Type Rock, Paper, or Scissor to begin, or type 'Q' to QUIT.\n")

while True:
    # 1. Get user input
    user_choice = input("Enter your move (or 'Q' to quit) = ").strip().capitalize()
    
    # 2. Check for quit condition
    if user_choice == "Q":
        print("\n👋 Thanks for playing! Goodbye.")
        break

    # 3. Validate user input
    if user_choice not in item_list:
        print("❌ Invalid move! Please select Rock, Paper, or Scissor.\n")
        continue
    
    # 4. Computer makes a random choice
    comp_choice = random.choice(item_list)
    print(f"\n👤 Your move = {user_choice} | 🤖 Computer move = {comp_choice}")
    
    # 5. Determine the round results
    if comp_choice == user_choice:
        print("🤝 It's a DRAW!")
        
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("📄 Paper covers Rock! COMPUTER WINS!")
            computer_score = computer_score + 1
        else:
            print("💥 Rock smashes Scissors! YOU WIN!")
            player_score = player_score + 1
            
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("✂️ Scissors cut Paper! COMPUTER WINS!")
            computer_score = computer_score + 1
        else:
            print("📄 Paper covers Rock! YOU WIN!")
            player_score = player_score + 1
            
    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            print("💥 Rock smashes Scissors! COMPUTER WINS!")
            computer_score = computer_score + 1
        else:
            print("✂️ Scissors cut Paper! YOU WIN!")
            player_score = player_score + 1
            
    # 6. Display the ongoing scoreboard at the bottom of the loop highway
    print(f"🏆 SCORE BOARD -> You: {player_score} | Computer: {computer_score}")
    print("-" * 40)  # Adds a clean dividing line between rounds
