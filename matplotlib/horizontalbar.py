
import matplotlib.pyplot as plt

students = ["Sayali", "Anushka", "Sanika", "Payal", "Punam"]
marks = [85, 90, 78, 88, 75]


plt.barh(students, marks, color="skyblue", edgecolor="black")


plt.title("Students' Marks")
plt.xlabel("Marks")
plt.ylabel("Students")


plt.show()
