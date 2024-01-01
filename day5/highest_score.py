student_score=input("Input a list of studnet").split()
for n in range(0, len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)
max1=0
for score in student_score:
    if score>max1:
        max1=score
print(max1)