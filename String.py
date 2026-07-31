#String tasks
string=input("enter a string:")
count=0
for ch in string:
    count+=1
print("Charcater count is:",count)

#task2
str2=input("Enter a string:")
vowel=consonant=digit=space=sp=0

for c in str2:
    if c in ("a","e","i","o","u"):
        vowel+=1
    else:
        consonant+=1
print("Vowels:",vowel)
print("Consonants:",consonant)
for a in str2:
    if a==" ":
        space+=1
    
print("Spaces:",space)
for b in str2:
    if b.isdigit():
        digit+=1
print("digits:",digit)
for p in str2:
    if p in ("!,@,#,$,%,^,&,*,{,}"):
        sp+=1

print("Symbols:",sp)

#task3
str3=input("Enter a string:")
rev=""
for ch in str3:
    rev=ch+rev
print("reverse string is:",rev)

#task4
str4=input("enter a string")
if str4==str4[::-1]:
    print("Palindrome")
else:
    print("not palindrome")

#task5
str5=input("enter a string:")
upper=0
lower=0
for ch in str5:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print("Upper letters:",upper)
print("Lower letters:",lower)

#task6
str6="sayali"
print(str6.replace("a","y"))

#task7
s1=input("enter a string:")
s1=s1.strip()
print(s1)

#task8
s2=input("Enter a string:")
count1={}
for ch in s2:
    count1[ch]=count1.get(ch,0)+1
for key,value in count1.items():
    print(key,":",value)
    
#task9
s3=input("entera string:")
print("first characre",s3[0])
print("last character",s3[-1])

#task10
s4=input("Enter a string:")
for ch in s4:
    print("ASCii values:",ord(ch))

#task11
s5=input("Enter a sentence:")
count=0
for ch in s5:
    if ch ==" ":
        count+=1
print("Counts:",count)

#task12
string = input("Enter a sentence: ")
words = string.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word is:", longest)

#task13
string = input("Enter a sentence: ")
words = string.split()
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word is:", shortest)

#task14
s5=input("enter a string:")
print(s5.title())


#task15
s6="saylee"
dup=""
for ch in s6:
    if s6.count(ch)>1 and ch not in dup:
        dup+=ch
print("duplicate characters:",dup)


#task16(frequency of character)
str3=input("enter a string:")
count={}
for ch in str3:
    count[ch]=count.get(ch,0)+1
for key,value in count.items():
    print(key,":",value)
    
    
       

#task17
s1=input("Enter a string:")
s2=input("enter a string:")
count1={}
count2={}
for ch in s1:
    count1[ch]=count1.get(ch,0)+1
for ch in s2:
    count2[ch]=count2.get(ch,0)+1
if count1==count2:
    print("Anagram")
else:
    print("not an anagram")
    
#task18
s5=input("Enter a string:")
dup=""
for ch in s5:
    if ch not in dup:
        dup+=ch
print(dup)

#task19
string=input("enter a sentence:")
sub=input("enter a substring:")
#for word in string:
if sub in string:
    print("Search successful")
else:
    print("substring is not available")


#task20
sentence=input("enter a sentence:")
sp_word=input("enter a word:")
words=sentence.split()
count=0

for word in words:
    if sp_word==word:
        count+=1
print("countof word:",count)

#task21
password = input("Enter password:")
upper = lower = digit = special = 0
for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")
    

#task22
s = input("Enter string:")
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        print(s[i], count, end="")
        count = 1

print(s[-1], count)

#task23
s = input("Enter string:")
new = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        new = new + s[i] + str(count)
        count = 1

new = new + s[-1] + str(count)
if len(new) < len(s):
    print(new)
else:
    print(s)

#task24
s = input("Enter string:")
count = {}
for ch in s:
    count[ch] = count.get(ch,0) + 1
maxi = 0
char = ""
for key,value in count.items():
    if value > maxi:
        maxi = value
        char = key

print(char)

#task25
s = input("Enter string:")
count = {}
for ch in s:
    count[ch] = count.get(ch,0) + 1
first = 0
second = 0
fchar = ""
schar = ""
for key,value in count.items():
    if value > first:
        second = first
        schar = fchar
        first = value
        fchar = key
    elif value > second and value != first:
        second = value
        schar = key
print(schar)


#task26
s = input("Enter string:")
shift = int(input("Enter shift:"))
new = ""

for ch in s:
    if ch.isalpha():
        new = new + chr(ord(ch)+shift)
    else:
        new = new + ch

print(new)


#task27
email = input("Enter email:")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

#task28
s = input("Enter sentence:")
words = s.split()
count = {}

for word in words:
    count[word] = count.get(word,0)+1

for key,value in count.items():
    print(key,":",value)

#task29
s = input("Enter sentence:")
words = s.split()
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")

#task30
s1 = input("Enter first string:")
s2 = input("Enter second string:")
if len(s1) == len(s2) and s2 in s1+s1:
    print("Yes")
else:
    print("No")
    


    



    

    


        
        
        
    

