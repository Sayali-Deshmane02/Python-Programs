#1.Write a Python program to create a set containing five integers and display all its elements.
s1={89,67,55,45,12}
print(s1)
print(type(s1))

#2.Create a list containing duplicate values. Convert the list into a set and display the resulting set.
li=[4,55,78,55,23]
print("List:",li)
s2=set(li)
print("Result:",s2)

#3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
set1={"Apple","Banana","cherry","Watermelon","Strawberry"}
print("Original set:",set1)
set1.add("Chickoo")
set1.add("Blueberry")

print("After adding:",set1)

#4.Create a set of numbers and remove a specified number from the set.
s3={78,66,54,3,9}
print("Original set:",s3)
s3.remove(54)
print("after removing:",s3)

#5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
s = int(input("Enter how many students you want: "))
set1 = set()
for i in range(s):
    name = input("Enter student name: ")
    set1.add(name)

print("Students:", set1)

search= input("Enter a name to check: ")
if search in set1:
    print("Student exists in the set")
else:
    print("Student does not exist in the set")

#6.Create a set of cities and determine the total number of cities using an appropriate function.
set2={"Mumbai","Kolhapur","Chennai","Mathura"}
print("Total no of cities:", len(set2))

#7.Create a set of programming languages and display each language using a for loop.
lang={"C","C++","Python","Java","SQL"}
print("Programming languages:")
for i in lang:
    print(i,end=" ")

#8.Create a list containing duplicate numbers, use a set to remove the duplicates.
list2=[78,90,78,45]
print("\nOriginal List:",list2)
s=set(list2)
print("\nAfter removing duplicates:",s)

#9.Create two sets of integers and find their union
s1={23,67}
s2={89,99}
u=s1.union(s2)
print("Union:",u)

#10.Create two sets and find the elements common to both sets.
s1={23,67,90}
s2={67,90}
c=s1.intersection(s2)
print("\nCommon element:",c)

#11.Create two sets and find:
#Elements present in the first set but not the second 
#Elements present in the second set but not the first
s4={4,5}
s5={6,7}
i=s4.difference(s5)
print("Elements in s4:",i)
j=s5.difference(s4)
print("Elements in s5:",j)

#12.Create two sets of numbers and find the elements that are present in either set but not in both.
s1={90,78,67}
s2={55,34,12}
s3=s1.symmetric_difference(s2) #we also can use s1^s2
print("result:",s3)

#13.Create two sets and determine whether the first set is a subset of the second set.
sett={23,33,45,67}
sett1={45,67}
res=False
if len(sett1)<=len(sett):
        if sett1.issubset(sett):
            res=True
             
print("result is:",res)

#14.Create two sets and determine whether the first set is a superset of the second set.
s1={90,78,67}
s2={90,67,55}
res=False
if len(s1)>=len(s2):
    if s1.issuperset(s2):
        res=True
print("Result is:",res)

#15.Write a program to determine whether two sets have no elements in common.
s1={90,78,67}
s2={55,34,12}
common=False
for i in s1:
    if i in s2:
        common=True
        break
if common:
    print("There are common elements:")
else:
    print("There is no common element")

#16.Create two sets and check whether they are equal.
s1={55,66,77}
s2={66,55,77}
if s1==s2:
    print("Both sets are equal")
else:
    print("Both sets are different")

#17.Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
stud1 = {"Maths", "Science", "Marathi"}
stud2 = {"Maths", "Marathi", "Sanskrit"}
common = stud1.intersection(stud2)

print("Subjects studied by both students:", common)

#18.Accept a sentence from the user and use a set to display all unique words.
sentence="Sayali is a beautiful girl is"
word=set()
for i in sentence.split():
    word.add(i)
print("Unique Words",word)

#19.Create two sets:
#•Students present in the morning session 
#•Students present in the afternoon session 
#Find:
#Students present in both sessions 
#Students present only in the morning 
#Students present only in the afternoon 
#Students present in at least one session
mrng={"Rahul","Priya","Rajesh"}
aftn={"Sayali","Shreya","Dipali","Priya"}
print("Students present in mrng session:",mrng)
print("Students present in afternoon session:",aftn)
print("Student present in both sessions:",mrng.intersection(aftn))
print("Student only in mrng") 

for stud in mrng:
    if stud not in aftn:
        print(stud,end=" ")
print("\nstudents only in afternoon:")
for stud in aftn:
    if stud not in mrng:
        print(stud,end=" ")
print("\nStudents in at least one session:",mrng.union(aftn))

#20.Create sets representing students enrolled in:
#Python 
#Java
p={"Sayali","Dipali"}
J={"Shreya","Minal","Sayali"}
print("Students belongs to Python:")
for i in p:
    print(i)
print("Students belongs to Java:")
for i in J:
    print(i)

#21.Find students enrolled in both courses and students enrolled in only one course.
print("\nEnrolled in both courses:",p.intersection(J))
print("\nEnrolled in only one course:",p.symmetric_difference(J))


#22.Create two sets representing technical skills of two employees. Find:
#	Common skills 
#	Skills unique to Employee 1 
#	Skills unique to Employee 2 
#	All available skills
emp1={"C","C++","Java"}
emp2={"SQl","Hash","C++"}
print("Common skills:", emp1.intersection(emp2))
print("Skills unique to Employee 1:", emp1.difference(emp2))
print("Skills unique to Employee 2:", emp2.difference(emp1))
print("All available skills:", emp1.union(emp2))

#23.Create a set containing available books and another set containing requested books. Determine which requested books are available.
avb_books={"gfyuu","cgffyguygu"}
req_books={"gfyuu","cfdtdtd","cgtyt"}
avb=set()
for i in req_books:
    if i in avb_books:
        avb.add(i)
print("Available books:",avb)

#24.	Store visitor IDs from two different days in separate sets. Determine:
#	Unique visitors across both days 
#	Returning visitors 
#	Visitors who came only on the first day 
#	Visitors who came only on the second day
#	Create sets representing products belonging to different categories. Find products that belong to both categories.
day1 = {101, 102, 103}
day2 = {201, 202, 102}
print("Unique visitors:", day1.union(day2))
print("Returning visitors:", day1.intersection(day2))
print("Visitors who came only on first day:", day1.difference(day2))
print("Visitors who came only on second day:", day2.difference(day1))

products1 = {"Laptop", "Mouse", "Keyboard"}
products2 = {"Mouse", "Printer", "Keyboard"}
print("Products belonging to both categories:",
      products1.intersection(products2))

#25.	Represent the friends of two users using sets. Find:
#	Mutual friends 
#	Friends unique to User 1 
#	Friends unique to User 2 
#	Total unique friends
user1={"Sayali","Shreya"}
user2={"Anushka","Sanika","Sayali"}
print("Mutual friends:",user1.intersection(user2))
print("Unique friends of user1:",user1.difference(user2))
print("Unique friends of user2:",user2.difference(user1))
print("Total unique friends:",user1.union(user2))


        
    

