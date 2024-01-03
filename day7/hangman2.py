import random

word_list = ["ardvark","babboon","camel"]
choosen_word = random.choice(word_list)

print("your choosen word is",choosen_word)
guess = input("Guess a letter: ").lower()

blank =[]
for let in choosen_word:
    blank+="_"
print(blank)

for num in range(0,len(choosen_word)):
    if guess==choosen_word[num]:
        blank[num]=guess
print(blank)