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

#task7
s2=input("Enter a string:")
count1={}
for ch in s2:
    count1[ch]=count1.get(ch,0)+1
for key,value in count1.items():
    print(key,":",value)
    
#task8
s3=input("entera string:")
print("first characre",s3[0])
print("last character",s3[-1])

#task9
s4=input("Enter a string:")
for ch in s4:
    print("ASCii values:",ord(ch))

#task9
s5=input("Enter a sentence:")
count=0
for ch in s5:
    if ch ==" ":
        count+=1
print("Counts:",count)

#task10
string = input("Enter a sentence: ")
words = string.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word is:", longest)

#task11
string = input("Enter a sentence: ")
words = string.split()
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word is:", shortest)

#task12
s5=input("entera string:")
print(s5.title())

#task13
s5=input("Enter a string:")
dup=""
for ch in s5:
    if ch not in dup:
        dup+=ch
print(dup)

#task13
s1=input("Enter a string:")
s2=input("enter a string:")
count1={}
count2={}
for ch in s1:
    count1[ch]=count1.getch(ch,0)+1
for ch in s2:
    count2[ch]=count2.getch(ch,0)+1
if count1==count2:
    print("Anagram")
else:
    print("not an anagram") 
    
    



    

    


        
        
        
    

