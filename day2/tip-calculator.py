print("welcome to tip calculator")
total_bill = int(input("what is the total bill? "))
tip_per = int(input("what percentage tip you would like to give ? 10,12 or 15? "))
num_people = int(input("How many people to split the bill? "))
result = round((total_bill*((100+tip_per)/100))/num_people)
print(result)