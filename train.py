import matplotlib
import matplotlib.pyplot as plt
from utils import load_data, normalize, denormalize, model

matplotlib.use("webagg")

# Load and normalize data
mileages, prices = load_data('data.csv')
min_mileage, max_mileage = min(mileages), max(mileages)
min_price, max_price = min(prices), max(prices)

mileages_norm = [normalize(m, min_mileage, max_mileage) for m in mileages]
prices_norm = [normalize(p, min_price, max_price) for p in prices]

# Initialize parameters
theta0 = 0
theta1 = 0
learning_rate = 0.01
iterations = 5000
m = len(mileages_norm)
costs_history = []

# Cost function
def cost():
    return (1 / (2 * m)) * sum((model(mileages_norm[i], theta0, theta1) - prices_norm[i]) ** 2 for i in range(m))

# Gradient descent
for _ in range(iterations):
    tmp_theta0 = (1 / m) * sum(model(mileages_norm[i], theta0, theta1) - prices_norm[i] for i in range(m))
    tmp_theta1 = (1 / m) * sum((model(mileages_norm[i], theta0, theta1) - prices_norm[i]) * mileages_norm[i] for i in range(m))
    
    theta0 -= learning_rate * tmp_theta0
    theta1 -= learning_rate * tmp_theta1

    costs_history.append(cost())

theta0_denorm = (
        theta0 * (max(prices) - min(prices))
        + min(prices)
        - theta1
        * min(mileages)
        * (max(prices) - min(prices))
        / (max(mileages) - min(mileages))
    )
theta1_denorm = (
    theta1
    * (max(prices) - min(prices))
    / (max(mileages) - min(mileages))
)

# Save parameters
with open('theta.txt', 'w') as file:
    file.write(str(theta0_denorm) + '\n')
    file.write(str(theta1_denorm))

# Bonus stuff
plt.subplot(1, 2, 1)
plt.scatter(mileages, prices, label='Actual Data')
plt.plot(mileages, [denormalize(model(normalize(m, min_mileage, max_mileage), theta0, theta1), min_price, max_price) for m in mileages], color='red', label='Linear Regression')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(range(iterations), costs_history, label='Cost History')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.legend()

plt.tight_layout()
plt.show()
