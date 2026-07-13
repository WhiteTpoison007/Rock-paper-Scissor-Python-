# Rock-paper-Scissor-Python-
# 🎮 Interactive Rock, Paper, Scissors with Score Tracker

A polished, terminal-based Rock, Paper, Scissors game built with Python 3. This project features continuous gameplay, automated input cleaning, random AI opponent moves, and a persistent live score counter.

---

## 🛠️ How It Works (The Code Flow)

The diagram below shows how the program runs using a `while True` loop. The score tracker updates inside the game rooms and always funnels down to the **Main Highway** to print the scores at the end of every round.

```text
    [ START GAME ]
          │
          ▼
   Initialize Scores
 (Player: 0 | Comp: 0)
          │
          ▼
┌────────────────────────────────────────┐
│        🔄 WHILE TRUE LOOP              │
│                                        │
│  Get Input ──► Is it 'Q'? ──► [QUIT]   │
│       │                                │
│       ▼                                │
│  Is it Valid? ──► No ───► [CONTINUE]   │
│       │                                │
│       ▼ (Valid Move)                   │
│  AI Random Choice                      │
│       │                                │
│       ▼                                │
│  ┌──────────────────────────────────┐  │
│  │     IF / ELIF / ELSE ROOMS       │  │
│  │                                  │  │
│  │ 🤝 DRAW    💥 USER +1   📄 COMP +1│  │
│  └────────────────┬─────────────────┘  │
│                   │                    │
│                   ▼                    │
│  ⚡ THE MAIN HIGHWAY                   │
│  Print Live Scoreboard 🏆              │
│                                        │
└────────────────────────────────────────┘


## 🎮 Game Rules & Logic Hierarchy


The game evaluates matches using a strict logical conditional flow:
┌───────────────┐
               │  YOUR CHOICE  │
               └───────┬───────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
      [ ROCK ]      [ PAPER ]    [ SCISSOR ]
      ─┬────┬─      ─┬─────┬─    ─┬──────┬─
       │    │        │     │      │      │
       ▼    ▼        ▼     ▼      ▼      ▼
    📄Paper ✂️Scis   ✂️Scis  💥Rock 💥Rock  📄Paper
     (Lose)  (Win)  (Lose)  (Win) (Lose)  (Win)

##✨ Features
Persistent Scoreboard: Tracks and displays ongoing human vs. computer scores dynamically after every single round.

Input Normalization: Uses .strip().capitalize() to seamlessly clean user inputs (e.g., typing rock,  rock, or ROCK will all process successfully).

Robust Error Handling: Detects invalid inputs instantly, warns the user, and skips cleanly back to the prompt using continue.

Clean Terminal UI: Styled with clear text spacing and arcade emojis for a satisfying user experience.

##🚀 How to Run
Make sure you have Python 3 installed on your computer.

Download or copy the rock_paper_scissors.py script.

Open your terminal or command prompt, navigate to the folder, and run:

Bash
python rock_paper_scissors.py

##📝 Concepts Learned
Building this project helped reinforce foundational programming concepts:

State Management: Tracking variables (player_score, computer_score) over time across multiple game loops.

Horizontal Indentation: Understanding Python's strict block hierarchy and how lines execute when grouped inside nested code environments.

Loop Control Statements: Controlling execution flow via break (exit doors) and continue (skipping lines).

