
import matplotlib.pyplot as plt

marks = [45, 56, 67, 78, 89, 56, 67, 45, 90, 76,
         65, 78, 88, 92, 56, 72, 81, 69, 74, 85]


plt.hist(marks, bins=5, edgecolor="black")


plt.title("Histogram of Students' Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")


plt.show()
