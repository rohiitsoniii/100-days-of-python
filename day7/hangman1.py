import random

word_list = ["ardvark","babboon","camel"]
rand_word = random.choice(word_list)
char = input("enter a char").lower() 
for charr in rand_word:
    if char==charr:
        print("right")
    else:
        print("wrong")
