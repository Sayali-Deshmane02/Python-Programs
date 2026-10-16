#1.	Write a Python program using regular expressions to extract all digits from a given string.
import re
s = input("Enter a string: ")
digits = re.findall(r'\d', s)
print("Digits in the string:", digits)
#2.	Accept a sentence and display all words beginning with the letter A or a.
import re
s = input("Enter a sentence: ")
words = re.findall(r'\b[Aa]\w*', s)
print("Words beginning with A or a:", words)

#3.	Write a program to count the occurrences of vowels in a given string using regular expressions.
import re

s = input("Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', s)
print("Vowels:", vowels)
print("Total number of vowels:", len(vowels))

#4.	Write a program to extract all uppercase letters from a given string.

s = input("Enter a string: ")
letters = re.findall(r'[A-Z]', s)
print("Uppercase letters:", letters)

#5.	Write a program to identify all spaces, tabs, and newline characters in a text.

s = input("Enter text: ")
characters = re.findall(r'[ \t\n]', s)
print("Spaces, tabs, and newlines:", characters)
print("Total occurrences:", len(characters))

#6.	Write a program to replace multiple consecutive spaces with a single space.

s = input("Enter a string: ")
result = re.sub(r' +', ' ', s)
print("Result:", result)

#7.	Accept a sentence and display all words containing exactly five characters.


s = input("Enter a sentence: ")
words = re.findall(r'\b\w{5}\b', s)
print("Five-character words:"), words
      
#8.	Write a program to identify all words ending with the letter s.

s = input("Enter a sentence: ")
words = re.findall(r'\b\w*s\b', s, re.IGNORECASE)
print("Words ending with s:", words)
      
#9.	Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.


s = input("Enter a string: ")

result = re.sub(r'[^a-zA-Z0-9 ]', '', s)

print("Result:", result)
#10.	Write a program to count the number of words in a sentence using regular expressions.
import re

s = input("Enter a sentence: ")

words = re.findall(r'\b\w+\b', s)

print("Number of words:", len(words))
#11.	Write a program to validate a 10-digit Indian mobile number using a regular expression.
import re

num = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', num):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
#12.	Accept an email address and check whether it follows a reasonable email format.
import re

email = input("Enter email address: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.fullmatch(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")
#13.	Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
import re

s = input("Enter a paragraph: ")

dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s)

print("Dates:", dates)
#14.	Write a program to identify web addresses beginning with http:// or https://.
import re

s = input("Enter text: ")

urls = re.findall(r'https?://\S+', s)

print("Web addresses:", urls)
#15.	Write a program to extract all hashtags from a social media post.
import re

s = input("Enter a social media post: ")

hashtags = re.findall(r'#[a-zA-Z0-9_]+', s)

print("Hashtags:", hashtags)

#16.	Write a program to check whether a password contains at least eight characters, one uppercase letter, one lowercase letter, one digit, and one special character.
import re

password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9\s]).{8,}$'
if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")
    
#17.	Write a program to identify consecutive repeated words in a sentence, ignoring case differences.
s = input("Enter a sentence: ")
words = re.findall(r'\b(\w+)\s+\1\b', s, re.IGNORECASE)
print("Repeated words:", words)

#18.	Write a program to extract six-digit Indian PIN codes from a paragraph.
s = input("Enter a paragraph: ")
pins = re.findall(r'\b[1-9]\d{5}\b', s)
print("PIN codes:", pins)

#19.	Write a program to check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.

number = input("Enter vehicle number: ")
pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'

if re.fullmatch(pattern, number):
    print("Valid registration format")
else:
    print("Invalid registration format")

#20.	Write a program to extract file extensions from filenames in a given string.
s = input("Enter filenames: ")
extensions = re.findall(r'\.([a-zA-Z0-9]+)\b', s)
print("File extensions:", extensions)

#21.	Write a program to remove HTML tags, extra whitespace, and unwanted punctuation from a text document.
text = input("Enter text: ")
text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'[^\w\s.,!?]', '', text)
text = re.sub(r'\s+', ' ', text)

print("Cleaned text:", text.strip())

#22.	Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions.
text = input("Enter invoice text: ")
invoice = re.findall(r'INV-\d+', text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'₹\s?\d+(?:,\d{3})*(?:\.\d{2})?', text)

print("Invoice Numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)

#23.	Write a program to identify single-line comments in Python source code. Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
code = input("Enter Python code: ")
comments = re.findall(r'#.*', code)
print("Single-line comments:", comments)

#24.	Validate product codes following the pattern ABC-1234-XY, where letters and digits must appear in the specified positions.
code = input("Enter product code: ")

pattern = r'^[A-Z]{3}-\d{4}-[A-Z]{2}$'

if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")
    
#25.	Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions.
text = input("Enter student details: ")
pattern = r'Name:\s*(\w+)\s+Roll:\s*(\d+)\s+Marks:\s*(\d+)'
students = re.findall(pattern, text)

for name, roll, marks in students:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    
#26.	Extract DOI identifiers, pimport re

text = input("Enter research paper references: ")
doi = re.findall(r'\b10\.\d{4,9}/[^\s]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b', text)
urls = re.findall(r'https?://[^\s]+', text)

print("DOI:", doi)
print("Publication Years:", years)
print("Email Addresses:", emails)
print("URLs:", urls)
