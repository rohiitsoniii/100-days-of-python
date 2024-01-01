import random
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?']
number=['1', '2', '3', '4', '5', '6', '7', '8', '9']
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T','U','V','X','Y','Z']

print("Welcome to password genretor")
nr_letter=int(input("how many letters would you like in your password?  "))
nr_symbol=int(input("how many symbol you want in your password\n"))
nr_number=int(input("how many you in in password\n"))

password=""
# easy-level
for let in range(1,nr_letter+1):
    rand= random.randint(0,len(letters)-1)
    password+=letters[rand]

for num in range(1,nr_number+1):
    rand= random.randint(0,len(number)-1)
    password+=number[rand]

for sym in range(1,nr_symbol+1):
    rand= random.randint(0,len(symbols)-1)
    password+=symbols[rand]
print(password)

# hard-level

password2=[]
for let in range(1,nr_letter+1):
    rand= random.randint(0,len(letters)-1)
    password2+=letters[rand]

for num in range(1,nr_number+1):
    rand= random.randint(0,len(number)-1)
    password2+=number[rand]

for sym in range(1,nr_symbol+1):
    rand= random.randint(0,len(symbols)-1)
    password2+=symbols[rand]

random.shuffle(password2)
password3=""
for char in password2:
    password3+=char

print(f"your password is : {password3}")

#my-way-of solving problem
password4=""
length=int(input("lenght of your password"))
total=[letters,number,symbols]
for le in range(0,length):
    rand_list=random.choice(total)
    password4+=random.choice(rand_list)

print(password4)