import csv
import matplotlib.pyplot as plt

# Read data from csv file
mileages = []
prices = []

with open('data.csv', 'r') as file:
    dataset = csv.reader(file)
    next(dataset)
    for row in dataset:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))

# Initialize parameters
theta0 = 0
theta1 = 0
learning_rate = 0.1
iterations = 1000
m = len(mileages)

# Normalize data
mileages = [(m - min(mileages)) / (max(mileages) - min(mileages)) for m in mileages]
prices = [(p - min(prices)) / (max(prices) - min(prices)) for p in prices]

# Model function
def model(mileage):
    return theta0 + theta1 * mileage

# Gradient descent
for _ in range(iterations):
    tmp_theta0 = (1 / m) * sum(model(mileages[i]) - prices[i] for i in range(m))
    tmp_theta1 = (1 / m) * sum((model(mileages[i]) - prices[i]) * mileages[i] for i in range(m))
    
    theta0 -= learning_rate * tmp_theta0
    theta1 -= learning_rate * tmp_theta1

# Save parameters
with open('theta.txt', 'w') as file:
    file.write(str(theta0) + '\n')
    file.write(str(theta1))

# Bonus stuff
plt.scatter(mileages, prices, label='Actual Data')
plt.plot(mileages, [model(m) for m in mileages], color='red', label='Linear Regression')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.legend()
plt.show()
