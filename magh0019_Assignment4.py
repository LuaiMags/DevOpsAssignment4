#Luai Maghur Assignment 4 Rock, Paper, Scissors game
import random


def getComputerChoice():
    return random.choice(["r", "p", "s"])


def determineWinner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "It's a tie!"
    elif (playerChoice == "r" and computerChoice == "s") or \
            (playerChoice == "s" and computerChoice == "p") or \
            (playerChoice == "p" and computerChoice == "r"):
        return "You win!"
    else:
        return "Computer wins!"


def playGame():     #Can Create Loop to continue, keeping it simple
    print("Welcome to Rock, Paper, Scissors!")
    print("Options:")
    print("  r: Rock")
    print("  p: Paper")
    print("  s: Scissors")

    playerChoice = input("Enter your choice (r, p, s): ").lower()
    if playerChoice not in ["r", "p", "s"]:
        print("Invalid choice. Please choose r, p, or s.")
        return

    computerChoice = getComputerChoice()
    choicesMap = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    print(f"You chose: {choicesMap[playerChoice]}")
    print(f"Computer chose: {choicesMap[computerChoice]}")

    result = determineWinner(playerChoice, computerChoice)
    print(result)


# Play the game
playGame()
