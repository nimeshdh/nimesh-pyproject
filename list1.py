l1=[1,8,7,2,21,15]

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# l1.append(8)
# print(l1)

# l1.insert(3,8)
# print(l1)

# l1.pop()
# print(l1)


# l1.append(8)
# last_items=l1.pop()
# print(last_items)
# print(l1)

# third_items=l1.pop(2)
# print(third_items)
# print(l1)


# l1.remove(7)
# print(l1)

# wap to store 7 fruits in alist enter by user 


fruits = []
for i in range(7):
    fruit = input(f"Enter fruit= {i+1}: ")
    fruits.append(fruit)
print("fruits  are:", fruits)


#wap to accept the marks of 6 student and display them in sorted order
student = []

for i in range(6):
    marks = int(input(f"Enter the marks of student {i+1}: "))
    student.append(marks)
student.sort()

print("Sorted marks of students:", student)
