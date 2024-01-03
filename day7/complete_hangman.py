import random


stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

end_game =False
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
choosen_word =random.choice(words)
# print(choosen_word)
word_length=len(choosen_word)
lives = 0

blank =[]
for let in choosen_word:
    blank+="_"
print(blank)

while not end_game:
    guess = input("guess a lettr: ").lower()
    
    if guess in blank:
        print("you already have guseed",guess)
    for num in range(0,len(choosen_word)):
        if guess==choosen_word[num]:
            blank[num]=guess

    if guess not in choosen_word:
        print(f"you gussed {guess}, that is not in the word.you lose a life")
        lives+=1
        if lives==6:
            end_game=True
            print("you lose")
    print(blank)
    if "_" not in blank:
        end_game=True
        print("you win")  

    print(stages[lives])