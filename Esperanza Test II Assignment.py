import random

print("Welcome to rock, paper, scissor game!\n1. Rock\n2. Paper\n3. Scissor")
while True:
    player1 = int(input("Player 1 (You): "))
    if player1 not in [1,2,3]:
        print("Invalid input, please try again.")
        continue
    player2 = random.randint(1,3)
    print("Player 2 (Computer): ", player2)
    if player1 == 1 and player2 == 2:
        print("You win!")
    elif player1 == 1 and player2 == 3:
        print("You lost! Better luck next time!")
    elif player1 == 2 and player2 == 1:
        print("You lose! Better luck next time!")
    elif player1 == 2 and player2 == 3:
        print("You win!")
    elif player1 == 3 and player2 == 1:
        print("You lose! Better luck next time!")
    elif player1 == 3 and player2 == 2:
        print("You win!")
    else:
        print("It's a tie!")
    stop = input("Do you want to play again? (Y/N): ").lower()
    if stop == 'y':
        continue
    elif stop == 'n':
        break
    else:
        print("Invalid input, please try again.")
        continue