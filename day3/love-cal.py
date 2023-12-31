print("Welcome to the Love Calculator")
name1 = input("what is your name ? \n").lower()
name2 = input("what is thier name ? \n").lower()
total = name1+name2
t=total.count("t")
r=total.count("r")
u=total.count("u")
e=total.count("e")
true = str(t+r+u+e)
l=total.count("l")
o=total.count("o")
v=total.count("v")

love =str(l+o+v+e)
love_total =int(true+love)

if love_total<10 or love_total>90:
    print(f'Your score is {love_total} ,you go together like coke and mentos')
if 40<love_total<60:
    print(f"your score is {love_total},you are alright together")
else:
    print(f"your score is {love_total}")
