#change 80 to 89
students_marks= [60, 80, 90, 98]
students_marks [1] = 89
print(students_marks)

#add a new item 55(append a new list)
students_marks=[60, 80, 90, 98]
students_marks.append(55)
print(students_marks)

#find the size of the list having appended 55
print(len(students_marks))

#write a python program to sum all the items in that list
students_marks=[60, 80, 90, 98, 55]
import math
students_marks= math.fsum([60, 80, 90, 98,55])
print(students_marks)

#write a python function that takes two lists and returns true if they have one common member
A = input("Enter items:")
F = input("Enter items:")
print("True, there is a common member in A and F")