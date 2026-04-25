import random

def menu():
    print("\n===== STONE PAPER SCISSORS =====")
    print("1. Play Game")
    print("2. Exit")

def get_user_choice():
    print("\nChoose:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter choice: ")

    choices = {"1": "Stone", "2": "Paper", "3": "Scissors"}
    return choices.get(choice, None)

def get_computer_choice():
    return random.choice(["Stone", "Paper", "Scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "Stone" and computer == "Scissors") or \
         (user == "Paper" and computer == "Stone") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win"
    else:
        return "Computer Wins"

def play():
    user = get_user_choice()
    if not user:
        print("Invalid choice!")
        return

    computer = get_computer_choice()

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    result = decide_winner(user, computer)
    print(f"Result: {result}")

# main loop
while True:
    menu()
    ch = input("Enter your choice: ")

    if ch == "1":
        play()
    elif ch == "2":
        print("Exiting Game...")
        break
    else:
        print("Invalid choice! Try again.")