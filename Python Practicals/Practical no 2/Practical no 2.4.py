#2.4. Write a program to accept a student’s roll number, name, and five subject marks. Print the student’s result like roll number, name, five subject marks, subject total, percentage, and grade using an if-else statement.

Roll_no = int(input("Enter a Roll No: "))
Name = input("Enter a Name: ")

Marks = []
for i in range(5):
    while True:
        mark = int(input("Enter marks of subject: "))
        if 0 <= mark <= 100:
            Marks.append(mark)
            break
        else:
            print("Invalid input. Marks should be between 0 and 100. Try again.")

Total_marks = sum(Marks)
print("Roll No: ", Roll_no)
print("Name: ", Name)
print("Subject_Marks: ", Marks)
print("Total marks of student are :", Total_marks)

Percentage = (Total_marks / 500) * 100
print("Percentage: ", Percentage, "%")

if Percentage > 80:
    print("Grade A+")
elif 70 <= Percentage < 80:
    print("Grade A")
elif 60 <= Percentage < 70:
    print("Grade B+")
elif 50 <= Percentage < 60:
    print("Grade C")
elif 40 <= Percentage < 50:
    print("Grade D")
else:
    print("Fail")
