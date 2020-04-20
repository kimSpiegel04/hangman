import random

lines = open('./words.txt').readlines()
line = lines[0]

words = line.split(';')
comp_word = random.choice(words)

print(comp_word)