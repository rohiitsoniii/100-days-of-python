import random

test_seed = int(input("create a seed number :  "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, see who gonna pay today?  ")
names= nameAsCSV.split(", ")
#ramdom.choice([names]) it is used to choice rando item from a list 

n= random.randint(0,(len(names)-1))
print(f"{names[n]} is gonna pay today bill") 