import random



rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
player_choice=int(input("what you want to choose? type 0 for rock,1 for paper,2 for scissor "))
rps=[rock,paper,scissor]
print(rps[player_choice])

computer_choice=random.randint(0,2)
print(rps[computer_choice])

if player_choice==0 and computer_choice==2:
    print("you Wins")
elif player_choice==2 and computer_choice==0:
    print("you Lose")
elif computer_choice>player_choice:
    print("you Lose")
elif computer_choice<player_choice:
    print("you Wins")
elif computer_choice==player_choice:
    print("tie")
else:
    print("you typed an invalid number")

