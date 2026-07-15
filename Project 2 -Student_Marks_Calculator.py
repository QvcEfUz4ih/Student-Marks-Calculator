print("===========================")
print(" Student Marks Calculator ")
print("===========================")


student_name = input("Enter student's name: ")


mark1 = float(input("Enter Mathematics mark: "))
mark2 = float(input("Enter English mark: "))
mark3 = float(input("Enter Science mark: "))


average = (mark1 + mark2 + mark3) / 3


if average >= 75:
    grade = "Distinction"
    

elif average >= 50:
    grade = "Pass"
    

else:
    grade = "Fail"


print()
print("======= RESULTS ==========")
print("Student:", student_name)
print(f"average: {average:.2f}%")
print("Grade:", grade)


if grade == "Distinction":
    print("Excellent work! keep it up!")
    
elif grade == "Pass":
     print("Well done! You passed.")

else:
    print("Don't give up. Keep studying!")
    
     




















