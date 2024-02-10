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

# Task 3: Replace any grade below 80 with the value Failed

grades = ["Failed" if grade < 80 else grade for grade in grades]

# Question 2: Advanced List Methods and Identity Operators:

print(" ")

# Task 1: Find out which students both submitted their assignments and attended the class

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if submitted is attended:
    print("all students attended class and submitted assignments")
else:
    print("Not all students attended class and submitted assignments")