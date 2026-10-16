
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.subplot(2, 2, 1)
plt.plot(x, y, marker="o")
plt.title("Line Chart")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.subplot(2, 2, 4)
plt.hist(y, bins=5, edgecolor="black")
plt.title("Histogram")

plt.tight_layout()

plt.show()
