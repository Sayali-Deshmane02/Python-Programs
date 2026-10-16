
import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 35, 30, 45, 50, 65]

plt.plot(months, sales, marker="o", color="blue", linestyle="-")


plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
