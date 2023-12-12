from utils import load_data, normalize, denormalize, model, signal_handler
import os

# Load thetas
if not os.path.exists('theta.txt'):
    print("theta.txt doesn't exist.")
    exit()
with open('theta.txt', 'r') as file:
    lines = file.readlines()
    theta0 = float(lines[0])
    theta1 = float(lines[1])

# Load and normalize data
mileages, prices = load_data('data.csv')
min_mileage, max_mileage = min(mileages), max(mileages)

# Interactive prompt
while True:
    mileage = input("Enter a mileage: ")
    try:
        mileage = float(mileage)
        if mileage < 0:
            print("Please enter a positive mileage.")
            continue
    except ValueError:
        print("Please enter a valid mileage.")
        continue

    price_norm = model(mileage, theta0, theta1)

    print(f"The estimated price for a car with {mileage} km is {price_norm} euros.")
