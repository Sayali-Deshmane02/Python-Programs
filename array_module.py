#signed int
from array import array
elements=list(map(int,input("Enter numbers:").split()))
arr=array('i',elements)
print(arr)

#float
from array import array
ele=array('f',[8.9,5.6,3.4])
print(ele)

#double
from array import array
ele=list(map(float,input("Enter nums:").split()))
arr1=array('d',ele)
print(arr1)

#Unicode
from array import array
ele=array('u',['A','B','C','D'])
print(ele)

from array import array


# Signed Character
a = array('b', [10, -20, 30])
print("Signed Character:", a)

# Unsigned Character
b = array('B', [10, 20, 30])
print("Unsigned Character:", b)

# Signed Short Integer
c = array('h', [-1000, 2000])
print("Signed Short:", c)

# Unsigned Short Integer
d = array('H', [1000, 2000])
print("Unsigned Short:", d)

# Signed Integer
e = array('i', [-100000, 200000])
print("Signed Integer:", e)

# Unsigned Integer
f = array('I', [100000, 200000])
print("Unsigned Integer:", f)

# Signed Long Integer
g = array('l', [-1234567, 1234567])
print("Signed Long:", g)

# Unsigned Long Integer
h = array('L', [1234567, 7654321])
print("Unsigned Long:", h)

# Signed Long Long Integer
i = array('q', [-1234567890123, 1234567890123])
print("Signed Long Long:", i)

# Unsigned Long Long Integer
j = array('Q', [1234567890123, 9876543210123])
print("Unsigned Long Long:", j)

