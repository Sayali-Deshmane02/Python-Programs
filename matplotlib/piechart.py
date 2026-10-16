
import matplotlib.pyplot as plt


subjects = ["Python", "DBMS", "Maths", "AI", "Cloud Computing"]
marks = [85, 90, 75, 80, 70]
plt.pie(marks, labels=subjects, autopct="%1.1f%%", startangle=90)
plt.title("Marks Distribution by Subject")
plt.show()
