student = int(input("Enter the number of students: "))
subject = int(input("Enter the amount of subjects: "))
total = 0

for x in range(1, student + 1):
    print(f'Student {x}' )
    student_total = 0
    for y in range(1, subject + 1):
        score = int(input(f'Enter score {y}: '))
        total = total + score
        student_total += score
    average = student_total / subject
    print(f'\nAverage score for Student {x}: {average}\n')
total = total / student
print("\n\nThe average score for the class is:", total)
