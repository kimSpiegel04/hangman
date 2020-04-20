import random

# check to see if guess is in the string (allows for multiple matches)
def isGuessCorrect(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

#check to see if game has been won
def isGameWon(a):
    if '_' not in a:
        return('Congrats! You won the game!')

# ask user if they'd like to play
def gameTime():
    print('Would you like to play hangman?')
    ans = input()
    if ans == 'yes':
        playGame()
    else: 
        print('Maybe next time!')
        exit()

def playGame():

    lines = open('./words.txt').readlines()
    line = lines[0]

    words = line.split(';')
    comp_word = random.choice(words)
    # print(comp_word)

    letters = list(comp_word)

    game_array = []

    for char in letters:
        if char.isalpha():
            game_array.append('_')
        else: 
            game_array.append(char)

    # initial display, keeps it pretty for the game
    game_display = ' '.join([str(char) for char in game_array])
    print(game_display)

    count = 7
    guesses = []

    while count > 0:

        print('\nGuess a letter! You have', count, 'lives left.')
        x = input().upper()

        if len(x) == 1 and x.isalpha():

            guess = isGuessCorrect(comp_word.upper(), x)

            if x in guesses:

                print('You guessed that already! Try again.')
            
            else: 

                guesses.append(x)

                if len(guess) > 0:
                    print('Your guesses so far:', guesses)
                    for i in guess:
                        game_array[i] = x
                    game_display = ' '.join([str(char) for char in game_array])
                    print(game_display)
                    
                    if isGameWon(game_display):
                        print('Congrats! You won the game!')
                        gameTime()

                else:
                    print('That letter was wrong! Try again.')
                    count = count - 1
        
        else: 
            print('Please choose just one letter at a time.')

    else:
        print('Game over! The phrase was', comp_word)
        gameTime()

gameTime()