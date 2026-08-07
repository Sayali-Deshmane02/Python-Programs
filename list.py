#task1
fruits=["Apple","Banana","Cherry","Strawberry"]
print(fruits)

#task2
list1=[5,9,34,23]
print(list1)
print("First element:",list1[0])
print("Third element:",list1[2])
print("Last element:",list1[-1])

#task3
color=["Red","Green","Orange","Blue"]
print(color)
color[2]="Black"
print("Updated list",color)

#task4
l2=[34,36,78,98]
print("Original list:",l2)
l2.append(99)
print("After insertion:",l2)
l2.insert(0,78)
print("Insertion at the begining:",l2)
l2.insert(4,90)
print("Insertion at specific postion:",l2)

#task5
names=["Riya","Sayali","Rahul","anushka"]
print("Original list:",names)
names.pop(0)
print("List after removing first student:",names)
names.pop()
print("Deletion of last student:",names)
names.remove("Rahul")
print("Deletion of specified student:",names)
print("Updated list:",names)

#task6
list3=[56,78,66,45]
print("Original list:",list3)
large=list3[0]
for ele in range(len(list3)):
    if list3[ele]>large:
        large=list3[ele]
print("largest ele:",large)
small=list3[0]
for ele in range(len(list3)):
    if small>list3[ele]:
        small=list3[ele]
print("smallest ele:",small)

#task7
numbers=[]
for i in range(10):
    num=int(input("Enter 10 numbers{}:".format(i+1)))
    numbers.append(num)
total=sum(numbers)
avg=total/len(numbers)
print("Numbers:",numbers)
print("Total:",total)
print("Average:",avg)

#task8
integers=[23,45,66,77,89,98,90,76,43,12,13,87,72,92,15]
even=0
odd=0

for i in integers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even numbers are:",even)
print("odd numbers are:",odd)

#task9
#Check whether a city exists in a list
cities = ["Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur"]

city = input("Enter city: ")

if city in cities:
    print("City exists")
else:
    print("City does not exist")
#task10 Reverse a list without using reverse()
numbers = [10, 20, 30, 40, 50]

rev = []

for i in range(len(numbers) - 1, -1, -1):
    rev.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", rev)
#task11 Display first 5, last 5, middle 4, alternate elements and reverse using slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5:", numbers[:5])
print("Last 5:", numbers[-5:])
print("Middle 4:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse:", numbers[::-1])
#task12 Display elements present at even indexes
numbers = [10, 20, 30, 40, 50, 60]

for i in range(0, len(numbers), 2):
    print(numbers[i])
#task13 Sort 10 numbers in ascending and descending order
numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
#task14 Display only unique values
numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("Unique values:", unique)
#task15 Find the second largest element
numbers = [10, 50, 20, 40, 30]

numbers = list(set(numbers))
numbers.sort()

print("Second largest:", numbers[-2])
#task16 Nested list storing student name, roll number and marks
students = [
    ["Sayali", 1, 85],
    ["Anushka", 2, 90],
    ["Shreya", 3, 78]
]

for student in students:
    print("Name:", student[0])
    print("Roll No:", student[1])
    print("Marks:", student[2])
    print()
#task17 Create a 3 × 3 matrix and perform addition
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Addition of matrices:")

for row in result:
    print(row)
#task18 Shopping cart operations
cart = []

cart.append("Milk")
cart.append("Bread")
cart.append("Rice")

print("Cart:", cart)

item = input("Enter item to search: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")

item = input("Enter item to remove: ")

if item in cart:
    cart.remove(item)
    print("Item removed")
else:
    print("Item not found")

print("Final cart:", cart)
print("Total items:", len(cart))
#task 19 Student attendance list
students = ["Sayali", "Anushka", "Shreya", "Meenal"]

print("Total students:", len(students))

name = input("Enter student to search: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

name = input("Enter new student: ")
students.append(name)

name = input("Enter absent student to remove: ")

if name in students:
    students.remove(name)

print("Updated student list:", students)
#task 20 Book list operations
books = ["Python", "Java", "C", "HTML"]

books.append("SQL")

book = input("Enter book to search: ")

if book in books:
    print("Book found")
else:
    print("Book not found")

book = input("Enter book to remove: ")

if book in books:
    books.remove(book)

print("All books:", books)
print("Total books:", len(books))
#task 21 Merge two lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]

list3 = list1 + list2

print("Merged list:", list3)
14. Find common elements between two lists
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for n in list1:
    if n in list2:
        common.append(n)

print("Common elements:", common)
#task 22 Count frequency of each element
numbers = [10, 20, 10, 30, 20, 10]

frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print(frequency)
#task 23 Rotate list left and right by 1 position
numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Left rotation:", left)
print("Right rotation:", right)
#task 24 Remove duplicates while preserving original order
numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("List after removing duplicates:", unique)
#task 25 Marks of 20 students — highest, lowest, average
marks = []

for i in range(20):
    m = int(input("Enter marks: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above)
print("Students below average:", below)

#task 26 Employee salaries
salaries = []

for i in range(5):
    salary = int(input("Enter salary: "))
    salaries.append(salary)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50 = 0
below_30 = 0

for salary in salaries:
    if salary > 50000:
        above_50 += 1
    if salary < 30000:
        below_30 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above 50000:", above_50)
print("Employees earning below 30000:", below_30)

#task 27 Batsman's scores in 10 matches
scores = []

for i in range(10):
    score = int(input("Enter score: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half centuries:", half_centuries)



#task 28 Temperature of 30 days
temperatures = []

for i in range(30):
    temp = float(input("Enter temperature: "))
    temperatures.append(temp)

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)

#task 29 Patient management using list

Here, each patient is stored as [name, age].

patients = [
    ["Sayali", 20],
    ["Anushka", 21],
    ["Shreya", 22]
]


name = input("Enter patient name to add: ")
age = int(input("Enter patient age: "))

patients.append([name, age])


name = input("Enter patient name to search: ")

found = False

for patient in patients:
    if patient[0] == name:
        print("Patient found")
        print("Name:", patient[0])
        print("Age:", patient[1])
        found = True
        break

if not found:
    print("Patient not found")


name = input("Enter patient name to delete: ")

for patient in patients:
    if patient[0] == name:
        patients.remove(patient)
        print("Patient deleted")
        break
else:
    print("Patient not found")

print("All patients:")

for patient in patients:
    print("Name:", patient[0], "Age:", patient[1])

print("Total patients:", len(patients))










