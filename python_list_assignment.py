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
    
# Task 2: Check if both lists are identical regardless of content or order

if submitted == attended:
    print("Both lists are identical")
else:
    print("Both lists are not identical")
    
# Task 3: Remove any student from the attended list who did not submit their assignment:

attended.remove("Eve")
attended.remove("Frank")
print("these studentes attended the class and submitted their assignment", attended)

# Question 3: Advanced Slicing Techniques:

print(" ")

# Task 1: Extract temperatures for the second week (7 days) of the month.

temperatures = [72, 75, 78, 7, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures [7:14]
print("Temperatures in the second week of the month are", second_week)

# Task 2: Extract all temperatures above 100

temperatures = [temp for temp in temperatures if temp <= 100]
print("Temperatures after removing those above 100:", temperatures)

# Task 3: Reverse the list and extract temperatures from teh 5th to the 10th day of the reversed list

temperatures.reverse
print(temperatures)

fifth_to_tenth = temperatures [4:10]
print("The fifth day to the tenth day of the week, temperatures will be", fifth_to_tenth)

# Question 4 List Comprehension and Membership Operators
print(" ")

# Task 1: use a list comprehension to create a new list containing only even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [ num for num in numbers if num % 2 == 0]
print("These numbers in the list are even:", even)

# Task 2: use a list comprehension to create a new list containing numbers greater than 5

new_numbers = [new for new in numbers if new > 5]
print("Numbers greater than 5:", new_numbers)

# Task 3: check to see if 7 is in the original numbers list

seven = 7 in numbers

if seven == True:
    print("Seven is in the original numbers list")
else: 
    print("Seven is not in the original numbers list")

# Question 5 Deep Dive in to Lists
    
# Task 1: Given the List:
# Create a new list from OG list where each element is ia dictionary with keys: name, grade, and activity
# and the corresponding values from the provided lists.
    
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

