import random
wrong_stat="You have entered a wrong choice"

while True:
    #Getting choice of computer
    lst=["Rock", "Paper", "Scissor"]
    choice=random.choice(lst)

    #Getting choice of iser
    print("The game will be total of 10 rounds\n-Rock\n-Paper\n-Scissor")
    n=input("\nEnter your choice: ").lower()

    # Computer chooses Rock
    if choice=="Rock":
        if n=="rock":
            print(f"Computer's choice: {choice}\nYou & Computer both selected same!!!\nRound Draw!!!")
        elif n=="paper":
            print(f"Computer's choice: {choice}\nPaper wraps Rock!!!\nYou have won this round!!!")
        elif n=="scissor":
            print(f"Computer's choice: {choice}\nRock breaks Scissor!!!\nYou have lost this round!!!")
        else:
            print(wrong_stat)

    # Computer chooses Paper
    elif choice=="Paper":
        if n=="paper":
            print(f"Computer's choice: {choice}\nYou & Computer both selected same!!!!\nRound Draw!!!")
        elif n=="scissor":
            print(f"Computer's choice: {choice}\nScissor cuts Papaer!!!\nYou have won this round!!!")
        elif n=="rock":
            print(f"Computer's choice: {choice}\nPaper wraps Rock!!!\nYou have lost this round!!!")
        else:
            print(wrong_stat)

    # Computer chooses Scissor
    else:
        if n=="scissor":
            print(f"Computer's choice: {choice}\nYou & Computer both selected same!!!!\nRound Draw!!!")
        elif n=="rock":
            print(f"Computer's choice: {choice}\nRock breaks Scissor!!!\nYou have won this round!!!")
        elif n=="paper":
            print(f"Computer's choice: {choice}\nScissor cuts Papaer!!!\nYou have lost this round!!!")
        else:
            print(wrong_stat)

        #Continuing/breaking the game
        play=input("Do you want to play again? (y/n): ").lower()
        if play=="y":
            continue
        else:
            break