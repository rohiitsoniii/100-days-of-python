row1 =["1","1","1"]
row2=["1","1","1"]
row3=["1","1","1"]
map =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do you want to put the treasure? ")
map[int(position[1])-1][int(position[0])-1]="X"
print(f"{row1}\n{row2}\n{row3}")