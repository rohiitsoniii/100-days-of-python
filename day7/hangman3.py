import random

word_list = ["ardvark","babboon","camel"]
choosen_word =random.choice(word_list)
word_length=len(choosen_word)

print("choosen word is",choosen_word)

blank =[]
for let in choosen_word:
    blank+="_"
print(blank)

end_game=False
while not end_game:
    guess = input("guess a lettr: ").lower()

    for num in range(0,len(choosen_word)):
        if guess==choosen_word[num]:
            blank[num]=guess
    print(blank)
    if "_" not in blank:
        end_game=True
        print("you win")