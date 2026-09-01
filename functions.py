#functions
#1.Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
        fact=1
        for i in range(1,n+1):
            
            fact=fact*i
        print("Factorial is:",fact)
factorial(5)

#2.Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n%2==0:
        print("Given value is Even")
    else:
        print("Given value is Odd")
check_even_odd(8)

#3.Define a function that accepts two numbers and returns the greater number.
def largest(n1,n2):
    if n1>n2:
        print(n1,"is greater")
    else:
        print(n2,"is greater")
n1=int(input("enter no1:"))
n2=int(input("enter no2:"))
largest(n1,n2)


#4.Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p,r,t):
    si=(p*r*t)/100
    print("Simple interest is:",si)
p=int(input("Enter priciple:"))
r=int(input("Enter rate:"))
t=int(input("Enter Time:"))
simple_interest(p,r,t)
    
#5.Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input("enter a num:"))
if is_prime(num):
    print(num,"is prime")
else:
    print(num,"is not prime")

#6.Define a function to calculate the area of a circle using its radius.
def area_circle(r):
    area=3.14*r*r
    print("Area is:",area)
radius=int(input("Enter radius:"))
area_circle(radius)

#7.Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_natural(n):
    summ=0
    for i in range(1,n):
        summ=summ+i
    print("sum is:",summ)
num=int(input("Enter range:"))
sum_natural(num)
    
#8.Create a function power(base, exponent) to calculate the value of base raised to exponent
def power(p,e):
    ans=p**e
    print("Answer is:",ans)
base=int(input("Enter base:"))
exponent=int(input("enter exponent:"))
power(base,exponent)

#9.Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def num():
    r=int(input("enter how many items you want:"))
    list=[]
    for i in range(r):
        num=int(input("Enter a num:"))
        list.append(num)
    print(list)
    large=list[0]
    for i in range(r):
        if large<list[i]:
            large=list[i]
    print("Largest element:",large)
            
num()
        


#10.Define a function that accepts a string and returns the number of vowels present in it.
def vowel(str1):
    vowel=0
    for i in str1:
        if i in ("a","e","i","o","u","A","E","I","O","U"):
            vowel+=1
    print("Vowel count is:",vowel)
str2=input("enter a string:")
vowel(str2)
    
#11.Write a function that accepts a string and returns its reverse.
def rev(string1):
        rev=string1[::-1]
        print("Reverse string is:",rev)
str1=input("Enter string:")
rev(str1)

#12.Create a function that checks whether a given string or number is a palindrome.
def check_palin(str2):
        rev=""
        for i in str2:
                rev=i+rev
        if rev==str2:
                print("Palindrome")
        else:
                print("not palindrome")
string2=input("Enter a string:")
check_palin(string2)

#13.Write a function that accepts a list of numbers and returns their average.
def acpt_list():
        r=int(input("enter how many no you want:"))
        list1=[]
        for i in range(r):
                i=int(input("enter  a no:"))
                list1.append(i)
        print(list1)
        sum=0
        
        for i in list1: 
                
                sum=sum+i
                
        avg=sum/len(list1)
        print("Sum is:",sum)
        print("avg is:",avg)

acpt_list()
                
#14.Define a function that accepts a list and an element and returns the number of times that element occurs.
def list1():
        r=int(input("Enter how many no you want?"))
        list2=[]
        for i in range(r):
                i=int(input("Enter no:"))
                
                list2.append(i)
        print(list2)
        ele=int(input("enter elementto count:"))
        count=0
        for i in range(len(list2)):
                
                        if list2[i]==ele:
                                count+=1
        if count>0:
                print(ele,"Occurs:",count,"times")
        else:
                print(ele,"not in list")
list1()
                
#15.Write a function that accepts a list and returns a new list containing only unique elements.
def unique_ele():
        r=int(input("enter how many no you want:"))
        list3=[]
        for i in range(r):
                list3.append(i)
        print(list3)
        dup=[]
        for i in list3:
                if i not in dup:
                        dup.append(i)
        print("Unique Elements:",dup)
unique_ele()

#16.Create a function to find the second-largest number in a list.
def second_l(num1,num2,num3,num4):
        listt=[num1,num2,num3,num4]
        large=listt[0]
        second=listt[1]
        print(listt)        
        for i in range(len(listt)):
                if large<listt[i]:
                        second=large
                        large=listt[i]
                elif listt[i] > second and listt[i] != large:
                        second=listt[i]

        print("Largest element:",large)
        print("Second largest:",second)
second_l(90,89,67,44)
                     
       
        
#17.Write a function that accepts n and returns the first n Fibonacci numbers.
def fib(n):
        a=0
        b=1
        c=a+b
        list=[]
        for i in range(n):
                list.append(a)
                a=b
                b=c
                c=a+b
        print(list)
fib(4)

                
#18.Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def marks():
        r=int(input("Enter five marks:"))
        list1=[]
        for i in range(r):
                i=int(input("Enter sub marks:"))
                list1.append(i)

        print(list1)

        sum=0
        for i in list1:
                sum=sum+i

        per=sum/5

        if per>=75:
                grade="Grade A"
        elif per>=55:
                grade="Grade B"
        else:
                grade="Grade C"

        return per, grade

per, grade = marks()

print("Percentage is:", per)
print("Grade:", grade)

                
#19.Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def electricity_bill(units):
        if units<=100:
                bill=units*5
        elif units<=200:
                bill=100*5+(units-100)*7
        else:
                bill=100*5+100*7+(units-200)*10

        return bill

units=int(input("Enter units consumed:"))
print("Electricity bill:",electricity_bill(units))

#20.Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
def salary(basic):
        hra=basic*20/100
        da=basic*10/100
        gross=basic+hra+da
        return gross

basic=int(input("Enter basic salary:"))
print("Gross salary:",salary(basic))

#21.Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def bill(price, quantity):
        total=price*quantity

        if total>=5000:
                discount=total*20/100
        elif total>=2000:
                discount=total*10/100
        else:
                discount=0

        final=total-discount
        return final
price=int(input("Enter item price:"))
quantity=int(input("Enter quantity:"))
print("Total bill:",bill(price,quantity))

#22.Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def calculate(list1):
        minimum=min(list1)
        maximum=max(list1)

        sum=0
        for i in list1:
                sum=sum+i

        average=sum/len(list1)

        return minimum,maximum,sum,average

list1=[10,20,30,40,50]
minimum,maximum,sum,average=calculate(list1)
print("Minimum:",minimum)
print("Maximum:",maximum)
print("Sum:",sum)
print("Average:",average)

#23.Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def total(marks):
        sum=0
        for i in marks:
                sum=sum+i
        return sum

def percentage(total):
        return total/5

def grade(per):
        if per>=75:
                return "A"
        elif per>=55:
                return "B"
        elif per>=35:
                return "C"
        else:
                return "F"

students=[]

n=int(input("Enter number of students:"))

for i in range(n):
        name=input("Enter name:")
        roll=int(input("Enter roll number:"))

        marks=[]
        for j in range(5):
                m=int(input("Enter marks:"))
                marks.append(m)

        t=total(marks)
        p=percentage(t)
        g=grade(p)

        students.append([name,roll,marks,t,p,g])

for s in students:
        print(s[0],s[1],"Total:",s[3],"Percentage:",s[4],"Grade:",s[5])

class_average=sum(s[4] for s in students)/n
highest=max(students,key=lambda x:x[4])
lowest=min(students,key=lambda x:x[4])
print("Class average:",class_average)
print("Highest scorer:",highest[0])
print("Lowest scorer:",lowest[0])

#24.Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.
balance=0
history=[]

def deposit(amount):
        global balance
        balance=balance+amount
        history.append("Deposited "+str(amount))

def withdrawal(amount):
        global balance

        if amount<=balance:
                balance=balance-amount
                history.append("Withdrawn "+str(amount))
                print("Withdrawal successful")
        else:
                print("Insufficient balance")

def balance_enquiry():
        print("Balance:",balance)

def transaction_history():
        print(history)
deposit(5000)
withdrawal(1000)
balance_enquiry()
transaction_history()

#25.Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
books={}

def add_book(book):
        books[book]=True

def issue_book(book):
        if book in books and books[book]==True:
                books[book]=False
                print("Book issued")
        else:
                print("Book not available")

def return_book(book):
        if book in books:
                books[book]=True
                print("Book returned")

def search_book(book):
        if book in books:
                print("Book found")
        else:
                print("Book not found")

def display_books():
        for book in books:
                if books[book]==True:
                        print(book)

add_book("Python")
add_book("Java")
add_book("C")

issue_book("Python")
search_book("Java")
display_books()

#26.Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.
def calculate_bill(units):
        if units<=100:
                bill=units*5
        elif units<=200:
                bill=500+(units-100)*7
        else:
                bill=1200+(units-200)*10

        fixed=100
        bill=bill+fixed

        tax=bill*5/100
        bill=bill+tax

        if bill>=3000:
                discount=bill*10/100
                bill=bill-discount

        return bill

units=int(input("Enter units:"))
print("Final bill:",calculate_bill(units))

#27.Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.
def consultation(charges):
        return charges

def laboratory(charges):
        return charges

def medicine(charges):
        return charges

def room(charges):
        return charges

def final_bill(category,c,l,m,r):
        total=c+l+m+r

        if category=="senior":
                discount=total*20/100
        elif category=="regular":
                discount=total*5/100
        else:
                discount=0

        return total-discount

c=int(input("Consultation charges:"))
l=int(input("Laboratory charges:"))
m=int(input("Medicine charges:"))
r=int(input("Room charges:"))
category=input("Enter patient category:")
print("Final bill:",final_bill(category,c,l,m,r))

#28.Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
products=[]

def add_product(price,quantity):
        products.append([price,quantity])

def remove_product(price):
        for i in products:
                if i[0]==price:
                        products.remove(i)

def subtotal():
        total=0
        for i in products:
                total=total+i[0]*i[1]
        return total

def coupon_discount(total):
        return total*10/100

def gst(total):
        return total*18/100

def invoice():
        sub=subtotal()
        discount=coupon_discount(sub)
        amount=sub-discount
        tax=gst(amount)
        final=amount+tax

        print("Subtotal:",sub)
        print("Discount:",discount)
        print("GST:",tax)
        print("Final invoice:",final)

add_product(500,2)
add_product(1000,1)
invoice()

#29.Write a recursive function to search for an element in a sorted list using binary search.
def binary_search(list1,low,high,element):
        if low>high:
                return -1

        mid=(low+high)//2

        if list1[mid]==element:
                return mid
        elif element<list1[mid]:
                return binary_search(list1,low,mid-1,element)
        else:
                return binary_search(list1,mid+1,high,element)

list1=[10,20,30,40,50]

element=int(input("Enter element:"))

result=binary_search(list1,0,len(list1)-1,element)

if result==-1:
        print("Element not found")
else:
        print("Element found at index:",result)

#30.Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
def binary(n):
        if n==0:
                return ""

        return binary(n//2)+str(n%2)

n=int(input("Enter decimal number:"))
if n==0:
        print("Binary: 0")
else:
        print("Binary:",binary(n))
        
#31.Check whether a string is a palindrome using recursion.
def palindrome(string):
        if len(string)<=1:
                return True

        if string[0]!=string[-1]:
                return False

        return palindrome(string[1:-1])

string=input("Enter string:")
if palindrome(string):
        print("Palindrome")
else:
        print("Not palindrome")

#32.Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
def addition(a,b):
        return a+b

def subtraction(a,b):
        return a-b

def multiplication(a,b):
        return a*b

def division(a,b):
        return a/b

def calculate(operation,a,b):
        return operation(a,b)

print(calculate(addition,10,5))
print(calculate(subtraction,10,5))
print(calculate(multiplication,10,5))
print(calculate(division,10,5))
