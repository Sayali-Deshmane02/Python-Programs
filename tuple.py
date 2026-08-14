# 1. Create a tuple of five integers and display it.

tup = (90, 23, 45, 56, 78)
print(tup)


# 2. Create a tuple containing five city names.
# Display first city, last city and third city.

tup1 = ("Latur", "Pune", "Satara", "Kolhapur", "Mumbai")

print(tup1)
print("First city:", tup1[0])
print("Last city:", tup1[-1])
print("Third city:", tup1[2])


# 3. Create a tuple of student names and display
# the total number of students using len().

tup2 = ("Rahul", "Riya", "Siya", "Lucky")

print(tup2)
print("Total students:", len(tup2))


# 4. Create a tuple of colors.
# Check whether a given color exists in the tuple.

t1 = ("Red", "Blue", "Orange", "Black")

color = input("Enter color: ")

if color in t1:
    print("Color found")
else:
    print("Color not found")


# 5. Create a tuple of fruits and display each fruit using a loop.

t1 = ("Mango", "Orange", "Blueberry", "Chikoo")

print("Fruits are:")

for i in t1:
    print(i)


# 6. Create a tuple with repeated numbers and count
# how many times a particular number appears.

t1 = (2, 4, 2, 6, 8)

num = int(input("Enter number: "))

print("Count:", t1.count(num))


# 7. Create a tuple of employee IDs and find
# the index of a given ID.

t1 = (101, 102, 109, 678)

id = int(input("Enter ID: "))

if id in t1:
    print("Index is:", t1.index(id))
else:
    print("ID not found")


# 8. Create two tuples of numbers and concatenate
# them into a single tuple.

t1 = (90, 78)
t2 = (78, 56)

t3 = t1 + t2

print("Concatenated tuple:", t3)


# 9. Create a tuple containing three elements
# and repeat it four times.

tup = (90, 78, 56)

ans = tup * 4

print(ans)


# 10. Create a tuple of 10 numbers and display:
# First five elements
# Last five elements
# Middle four elements
# Alternate elements
# Reverse tuple

tup = (90, 78, 56, 45, 34, 22, 19, 76, 3, 9)

print("Tuple:", tup)

print("First five elements:", tup[:5])
print("Last five elements:", tup[5:])
print("Middle four elements:", tup[3:7])
print("Alternate elements:", tup[::2])
print("Reverse tuple:", tup[::-1])


# 11. Convert a tuple into a list and add a new element.

tup = ("Sayali", "Riya", "Shyam")

ans = list(tup)

print("Original list:", ans)

ans.append("Dipali")

print("After adding element:", ans)


# 12. Accept five numbers from the user,
# store them in a list and convert the list into a tuple.

ans = []

for i in range(5):
    n = int(input("Enter a number: "))
    ans.append(n)

t = tuple(ans)

print("Tuple:", t)


# 13. Modify a tuple by converting it into a list
# and then back into a tuple.

t1 = (89, 67, 55)

l1 = list(t1)

print("List is:", l1)

l1[1] = 100

t2 = tuple(l1)

print("Modified tuple:", t2)


# 14. Create a tuple and delete it completely.

tup = (90, 89, 66, 45)

print("Tuple:", tup)

del tup

print("Tuple deleted successfully")


# 15. Create a nested tuple containing student details
# and display each record.

tupp = (
    (101, "Shreya"),
    (102, "Riya"),
    (103, "Shyam")
)

for i in tupp:
    print(i)


# 16. Store ten numbers in a tuple and calculate their sum.

tup2 = (9, 8, 6, 7, 4, 3, 2, 88, 45, 16)

total = 0

for i in tup2:
    total = total + i

print("Sum:", total)


# 17. Find the largest and smallest number in a tuple
# without using max() and min().

tuple1 = (56, 78, 90, 43, 32, 78)

large = tuple1[0]

for i in range(1, len(tuple1)):
    if large < tuple1[i]:
        large = tuple1[i]

print("Largest number:", large)


small = tuple1[0]

for i in range(1, len(tuple1)):
    if small > tuple1[i]:
        small = tuple1[i]

print("Smallest number:", small)


# 18. Calculate the average of elements stored in a tuple.

tuple1 = (56, 78, 90, 43, 32, 78)

total = 0

for i in tuple1:
    total = total + i

average = total / len(tuple1)

print("Sum:", total)
print("Average:", average)


# 19. Store 15 integers in a tuple and count
# even numbers and odd numbers.

tup = (11, 12, 13, 14, 16, 17, 18, 30, 89, 67,
       45, 122, 334, 345, 678)

even = 0
odd = 0

for i in tup:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 20. Accept a number from the user and determine
# whether it exists in the tuple.

tup = (90, 78, 56)

num = int(input("Enter a number: "))

if num in tup:
    print("Number exists")
else:
    print("Number does not exist in tuple")


# 21. Store student details in a tuple:
# Roll Number, Name, Department, Marks
# Display all details.

students = (
    (23, "Rahul", "CSE", 78),
    (34, "Riya", "Mech", 89)
)

for student in students:
    print(student)


# 22. Create tuples containing:
# Employee ID, Name, Salary
# Display all employee information.

tup = (
    (102, "Dipali", 40000),
    (103, "Sayali", 50000)
)

for employee in tup:
    print(employee)


# 23. Store item prices in a tuple and calculate:
# Total bill
# Average price
# Highest-priced item
# Lowest-priced item

price_tup = (90, 78, 50, 60)

total = 0

for i in price_tup:
    total = total + i

print("Total bill:", total)

average = total / len(price_tup)

print("Average price:", average)


high = price_tup[0]

for i in price_tup:
    if i > high:
        high = i

print("Highest price:", high)


low = price_tup[0]

for i in price_tup:
    if i < low:
        low = i

print("Lowest price:", low)


# 24. Store temperatures of seven days in a tuple
# and determine maximum, minimum and average temperature.

temp = (46, 37, 39, 36, 35, 41, 38)

print("Temperatures:", temp)

print("Maximum temperature:", max(temp))
print("Minimum temperature:", min(temp))
print("Average temperature:", sum(temp) / len(temp))


# 25. Store runs scored in 10 matches and calculate:
# Total runs
# Highest score
# Lowest score
# Average score

runs = (46, 37, 89, 66, 54, 102, 78, 45, 91, 63)

print("Runs:", runs)

print("Total runs:", sum(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", sum(runs) / len(runs))

#26.Create two tuples and find the common elements between them.
t1=(90,67,88)
t2=(88,78,23,90)
for i in t1:
    for j in t2:
        if i==j:
            print(i)

#27.Merge two tuples and remove duplicate elements.
t1=(90,67,88)
t2=(88,78,23,90)
merge=tuple(set(t1+t2))
print("Merged:",merge)

#28.Count the frequency of each element in a tuple.
tup = (2, 4, 2, 6, 8, 4, 2, 6)
freq = {}

for i in tup:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Tuple:", tup)
print("Frequency:", freq)

#29.
tup = (56, 23, 89, 12, 45, 67)

ascending = tuple(sorted(tup))
descending = tuple(sorted(tup, reverse=True))

print("Original tuple:", tup)
print("Ascending order:", ascending)
print("Descending order:", descending)

#30
patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Riya", 30, "B+"),
    (103, "Shreya", 22, "O+"),
    (104, "Amit", 35, "A+"),
    (105, "Priya", 28, "O-")
)

print("Patient Records:")

for patient in patients:
    print(patient)



id = int(input("\nEnter patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == id:
        print("Patient found:", patient)
        found = True
        break

if found == False:
    print("Patient not found")


print("\nTotal number of patients:", len(patients))



blood = input("\nEnter blood group: ")
print("Patients with blood group", blood, ":")
found = False
for patient in patients:
    if patient[3] == blood:
        print(patient)
        found = True

if found == False:
    print("No patient found with this blood group")


            







    
