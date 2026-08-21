#1.Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
student = {
    "roll_no": 101,
    "name": "Sayali",
    "department": "Computer",
    "marks": 89
}

for key, value in student.items():
    print(key, ":", value)

#2.Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 50000
}
key = input("Enter key: ")
if key in employee:
    print("Value:", employee[key])
else:
    print("Key does not exist")

#3.Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 10000,
    "Printer": 7000
}
print("Original dictionary:", products)
products["Headphones"] = 1500
print("After adding:", products)

#4.Create a dictionary containing student marks. Update the marks of a specified student.
student = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92
}
name = input("Enter student name: ")
marks = int(input("Enter new marks: "))
if name in student:
    student[name] = marks
    print("Updated dictionary:", student)
else:
    print("Student not found")
    
#5.Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Nagpur": 3000000,
    "Kolhapur": 500000
}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found")
    
#6.Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees = {
    101: "Rahul",
    102: "Priya",
    103: "Rajesh",
    104: "Sayali"
}
emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")

#7.Create a dictionary containing student records and find the total number of key-value pairs.
student = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92,
    "Sanika": 85
}
print("Total key-value pairs:", len(student))

#8.Create a dictionary and display:
#All keys 
#All values 
#All key-value pairs
student = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Key-value pairs:", student.items())

#9.Create a dictionary of programming languages and their creators. Display each key and value using a loop.
languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}
for key, value in languages.items():
    print(key, ":", value)
    
#10.Accept five student names and their marks from the user and store them in a dictionary.
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student dictionary:", students)

#11.Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
students = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92,
    "Sanika": 85
}

highest = max(students.values())
for name, marks in students.items():
    if marks == highest:
        print("Highest marks:", name, marks)
#12.Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92,
    "Sanika": 85
}

lowest = min(students.values())
for name, marks in students.items():
    if marks == lowest:
        print("Lowest marks:", name, marks)
        
#13.Create a dictionary containing student names and marks. Calculate the average marks of all students.
students = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92,
    "Sanika": 85
}

total = sum(students.values())
average = total / len(students)

print("Average marks:", average)
#14.Accept a string from the user and create a dictionary containing each character and its frequency.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:", frequency)

#15.Accept a sentence and create a dictionary containing each word and the number of times it occurs.
sentence = input("Enter a sentence: ")
frequency = {}
for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)

#16.Create two dictionaries and merge them into a single dictionary.
d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}

d1.update(d2)

print("Merged dictionary:", d1)

#17.Given two dictionaries, find the keys that are common to both dictionaries.
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 40, "c": 50, "d": 60}
common = set(d1.keys()).intersection(d2.keys())
print("Common keys:", common)

#18.Given two dictionaries, identify the values that are common to both dictionaries.
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"x": 30, "y": 40, "z": 20}
common = set(d1.values()).intersection(d2.values())
print("Common values:", common)

#19.Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
d = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
result = {}
for key, value in d.items():
    if value not in result.values():
        result[key] = value
print("After removing duplicates:", result)

#20.Create a dictionary and display its elements in ascending order of keys.
d = {
    4: "D",
    2: "B",
    1: "A",
    3: "C"
}
for key in sorted(d):
    print(key, ":", d[key])

#21.Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2

print(squares)

#22.Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2

print(squares)

#23.Given a list of numbers, create a dictionary containing each unique number and its frequency.
numbers = [2, 4, 2, 5, 4, 2, 6, 5]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)

#24.	Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3

print(cubes)

#25.Create a dictionary containing student names and marks. Develop a program to:
#•Add a student 
#•Update marks 
#•Delete a student 
#•Search for a student 
#•Display all students 
#•Find the highest marks 
#•Calculate the average
students = {
    "Sayali": 89,
    "Shreya": 78,
    "Anushka": 92
}


name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks


name = input("Enter student name to update: ")
if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks


name = input("Enter student name to delete: ")
if name in students:
    del students[name]


name = input("Enter student name to search: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

print("All students:", students)


if students:
    highest = max(students.values())
    print("Highest marks:", highest)


if students:
    average = sum(students.values()) / len(students)
    print("Average:", average)
    
#26.Create a dictionary containing employee names and salaries. Find:
#•Highest salary 
#•Lowest salary 
#•Average salary 
#•Employees earning more than ₹50,000
employees = {
    "Rahul": 45000,
    "Priya": 60000,
    "Rajesh": 75000,
    "Sayali": 55000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)
        
#27.Create a dictionary containing product names and quantities.
#Perform:
#•Add a product 
#•Update quantity 
#•Delete a product 
#•Search for a product 
#•Display products with quantity below 10
products = {
    "Laptop": 15,
    "Mouse": 8,
    "Keyboard": 12,
    "Printer": 5
}


name = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity


name = input("Enter product to update: ")
if name in products:
    quantity = int(input("Enter new quantity: "))
    products[name] = quantity


name = input("Enter product to delete: ")
if name in products:
    del products[name]


name = input("Enter product to search: ")
if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")


print("Products with quantity below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)
        
#28.Create a dictionary containing names and phone numbers.
#Implement:
#•Add contact 
#•Search contact 
#•Update contact 
#•Delete contact 
#•Display all contacts
contacts = {
    "Sayali": "9876543210",
    "Shreya": "9876501234"
}


name = input("Enter contact name: ")
phone = input("Enter phone number: ")
contacts[name] = phone


name = input("Enter name to search: ")
if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found")


name = input("Enter name to update: ")
if name in contacts:
    phone = input("Enter new phone number: ")
    contacts[name] = phone


name = input("Enter name to delete: ")
if name in contacts:
    del contacts[name]


print("All contacts:", contacts)

#29.	Create a dictionary containing book IDs and book names.
#Implement:
#•Add a book 
#•Search a book 
#•Remove a book 
#•Display all books 
#•Count total books
books = {
    101: "Python",
    102: "Java",
    103: "C++"
}


book_id = int(input("Enter book ID: "))
book_name = input("Enter book name: ")
books[book_id] = book_name


book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")


book_id = int(input("Enter book ID to remove: "))

if book_id in books:
    del books[book_id]


print("All books:", books)


print("Total books:", len(books))
#30.Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
students = {
    "Sayali": "Computer",
    "Shreya": "IT",
    "Anushka": "Computer",
    "Sanika": "ENTC"
}

grouped = {}
for name, department in students.items():
    if department not in grouped:
        grouped[department] = []

    grouped[department].append(name)

print("Students grouped by department:")
print(grouped)

#31.Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.
words = ["cat", "dog", "apple", "bat", "mango", "hi"]
result = {}
for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)
#32.Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
numbers = [2, 7, 11, 15]
target = 9
seen = {}
for num in numbers:
    required = target - num

    if required in seen:
        print("Numbers:", required, num)
        break

    seen[num] = True
    
#33.Take a string, use a dictionary to find the first character that occurs only once.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break
#34.Take a string, use a dictionary to find the first character that occurs more than once.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break
    
#35.Accept a paragraph and create a dictionary where:
#•Key = word length 
#•Value = number of words having that length.
paragraph = input("Enter a paragraph: ")
result = {}
for word in paragraph.split():
    length = len(word)

    if length in result:
        result[length] += 1
    else:
        result[length] = 1

print("Word length frequency:", result)

