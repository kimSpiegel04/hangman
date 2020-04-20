import random

lines = open('./words.txt').readlines()
line = lines[0]

words = line.split(';')
comp_word = random.choice(words)

print(comp_word)

letters = list(comp_word)
# print(letters)

game_array = []

for char in letters:
    if char.isalpha():
        game_array.append('_')
    else: 
        game_array.append(char)

#string of game_array
replace_str = ''.join([str(char) for char in game_array])

# this display keeps it pretty for the game
game_display = ' '.join(replace_str)
print(game_display)

guesses = []

def isGuessCorrect(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

count = 7

while count > 0:

    print('\nGuess a letter! You have', count, 'lives left.')
    x = input().upper()
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

        else:
            print('That letter was wrong! Try again.')
            count = count - 1

else:
    print('Game over! The phrase was', comp_word)




# while count > 0:
#     print('\nGuess a letter! You have', count, 'guesses left.')
#     x = input()
#     print(x, guess_array)
#     if len(guess_array) == 0:
#         guess_array.append(x)
#     else: 
#         if x: 
#             guess_array.append(x)
#             print(guess_array)
#             count = count - 1
#         else:
#             print('You already guessed that letter!')
#             print(guess_array)