import random

def menu():
    print("\n===== DICE GAME =====")
    print("1. Roll Dice")
    print("2. Exit")

def roll_dice():
    return random.randint(1, 6)

def decide_winner(player, computer):
    if player > computer:
        return "You Win"
    elif player < computer:
        return "Computer Wins"
    else:
        return "Draw"

def play():
    input("\nPress Enter to roll the dice...")

    player = roll_dice()
    computer = roll_dice()

    print(f"\nYou rolled: {player}")
    print(f"Computer rolled: {computer}")

    result = decide_winner(player, computer)
    print(f"Result: {result}")

# main loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        play()
    elif choice == "2":
        print("Exiting Game...")
        break
    else:
        print("Invalid choice! Try again.")