import csv

def model(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

def denormalize(value, min_value, max_value):
    return value * (max_value - min_value) + min_value

# Load parameters
with open('theta.txt', 'r') as file:
    lines = file.readlines()
    theta0 = float(lines[0])
    theta1 = float(lines[1])

# Read data from csv file
mileages = []
prices = []

with open('data.csv', 'r') as file:
    dataset = csv.reader(file)
    next(dataset)
    for row in dataset:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))

min_mileage = min(mileages)
max_mileage = max(mileages)

# Interactive prompt
while True:
    mileage = input("Enter a mileage: ")
    try:
        mileage = float(mileage)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Normalize input
    mileage_norm = normalize(mileage, min_mileage, max_mileage)

    # Predict price
    price_norm = model(mileage_norm, theta0, theta1)

    # Denormalize output
    price = denormalize(price_norm, min(prices), max(prices))

    print(f"The estimated price for a car with {mileage} km is {price} euros.")
