# Question 1 :Python List Transformation
# Task set 1: Grades: Set the grades in decending order and display the sorted list:
print(" ")

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

# Task 2: Find the average

average = sum(grades) // len(grades)
print("The average grade is,", average)