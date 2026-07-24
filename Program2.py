#Program for the for loop
string="Sayali"
for i in string:
    print(i,end=" ")
print("----------------")
#program for the while loop
i=1
while i<5:
    print(i,end=" ")
    i=i+1
print("----------------------")
#if-else
age=int(input("\nEnter age"))
if age>=18:
    print("People are eligible to vote")
else:
    print("not eligible to vote")
print("-------------------")


#task1
no=int(input("Enter a num"))
if no==0:
       print("Value is zero")
else:
    print("non zero")
print("----------------------")

#task2
no1=int(input("enter a first num:"))
no2=int(input("enter a second num:"))
if no1>no2:
        print("no1 is greatest")
else:
    print("no2 is greatest")
print("-----------------------------------")

#task3
digit=int(input("enter a number:"))
if digit>0:
    print("digit is positive")
else:
    print("digit is negative")
print("-------------------------------------")

#task4
character="a"
if character in ("a","e","i","o","u"):
      print("Vowel")
else:
    print("Consonant")
print("-------------------")

#task5
marks=int(input("Enter students's marks:"))
if marks>=90:
     print("Excellent Performance")
elif marks>=80:
    print("Very good")
elif marks>=70:
    print("good")
elif marks>=60:
    print("average Performance")
else:
    print("Poor Performance")
print("---------------------------------------")

#task6
a=int(input("Enter first no."))
b=int(input("enter second no."))
c=int(input("enter third no."))
if a>b and a>c:
      print(a,"is gretaest")
elif b>a and b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")
print("----------------------------------------")

#task6
a1=int(input("Enter first no."))
b1=int(input("enter second no."))
c1=int(input("enter third no."))
if a1<b1 and a1<c1:
      print(a1,"is smallest")
elif b1<a1 and b1<c1:
    print(b1,"is smallest")
else:
    print(c1,"is smallest")
print("----------------------------------------")

#task7
year=int(input("Enter year:"))
if (year%4==0) or (year%400==0 and year%100!=0):
    print("Leap year")
else:
    print("not a leap year")

print("-------------------------------------------")


#task8
num=int(input("enter num:"))
if num%2==0:
    print("Even")
else:
    print("odd")
print("----------------------------------------")

#task9
status=input("enter status[Married or not married]:")
gender=input("enter gender[Male or Female]:")
age=int(input("enter age:"))

if status=="married":
    print("driver insured")
elif status=="unmarried" and gender=="Male" and age>30:
    print("driver insured")
elif status=="unmarried" and gender=="Women" and age>25:
    print("driver insured")
else:
    print("driver not insured")
