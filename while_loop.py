#while loop
#Program to print natural numbers upto n
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1
    
#write a program to print even and odd nums upto n accept n from user
num = int(input("Enter a number: "))

print("Even numbers:")
i = 2
while i <= num:
    print(i)
    i += 2

print("Odd numbers:")
i = 1
while i <= num:
    print(i)
    i += 2
    
    
    
#write a prog to print sum of natural nums upto n
num1=int(input("enter  num:"))
add=0
i=1
while i<=num1:
     add=add+i
     i=i+1
     
#write a prog to print sum of even nums upto n
n = int(input("Enter a number: "))
i = 2
sum1 = 0
while i <= n:
    sum1 = sum1 + i
    i += 2

print("Sum of even numbers =", sum1)


        
#write  prog to print natural nums upto n in reverse order
n3 = int(input("Enter a number: "))

while n3 >= 1:
    print(n3)
    n3 -= 1
    
#write a prog to print the fibonacci series
n4 = int(input("Enter the number of terms: "))
a = 0
b = 1
i = 1
while i <= n4:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1
    
#write a prog to check entered num is prime or not
number = int(input("Enter a number: "))
if number <= 1:
    print("Not a Prime Number")
else:
    i = 2
    while i < number:
        if number % i == 0:
            print("Not a Prime Number")
            break
        i += 1
    else:
        print("Prime Number")
        
#write a prog to print sum of digits of entered number
number = int(input("Enter a number: "))
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print("Sum of digits =", sum)

#write a prog to check num is palindrome or not
number = int(input("Enter a number: "))
temp=number
rev = 0
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#write a prog to print the multiplication table
n=int(input("enter a num:"))
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

#write a prog to print largest and smallest number from n  numbers
n = int(input("Enter how many numbers: "))

i = 1
largest = None
smallest = None
while i <= n:
    num = int(input("Enter number: "))

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

    i += 1

print("Largest number =", largest)
print("Smallest number =", smallest)


    
