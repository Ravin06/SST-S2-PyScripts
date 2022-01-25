play_again = "y"
while play_again == "y":
    NOT = int(input("How many times would you like to play? "))
    for x in range(NOT):

        from random import randint

        print("Scissors, Paper, Stone")
        print("Choice 1: Scissors Choice 2: Paper, Choice 3: Stone")
        human = int(input(">"))
        com = randint(1, 3)

    #Draws
        if human == 1 and com == 1 or human == 2 and com == 2 or human == 3 and com == 3:
            print("Com chose same as you")
            print("Draw")

    #Wins
        #Scissors beats Paper
        elif human == 1 and com == 2:
            print("You chose Scissors and Com chose Paper")
            print("You Win, Com loses")
        #Paper beats Stone
        elif human == 2 and com == 3:
            print("You chose Paper and Com chose Stone")
            print("You Win, Com loses")
        #Stone beats scissors
        elif human == 3 and com == 1:
            print("You chose Stone and Com chose Scissors")
            print("You Win, Com loses")
        
    #Losses

        #Paper loses to Scissors
        elif human == 2 and com == 1:
            print("You chose Paper and Com chose Scissors")
            print("You Lose, Com Wins")
        #Stone loses to Paper
        elif human == 3 and com == 2:
            print("You chose Stone and Com chose Paper")
            print("You Lose, Com Wins")
        #Scissors loses to Stone
        elif human == 1 and com == 3:
            print("You chose Scissors and Com chose Stone")
            print("You Lose, Com Wins")

    play_again = input("Want to play again(y/n): ")

    
    
