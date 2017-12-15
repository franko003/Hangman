import random

def hangman():
    # Random list of words to play the game with
    words = ["apple", "wolverine", "rose", "stuff", "trade",
             "python", "cement", "baby", "chicken", "awesome"]
    word_index = random.randint(0, len(words) - 1)
    word = words[word_index]

    # Initialize variable for number of wrong guesses and game graphic
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "]
    
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    # Continue to play the game while the graphic is not fully printed
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose, it was {}.".format(word))

hangman()

    
