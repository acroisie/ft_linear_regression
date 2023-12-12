import csv
import signal
import sys
import os

# signal handler
def signal_handler(sig, frame):
    print('\nMy job here is done.')
    sys.exit(0)

# set signal handler
signal.signal(signal.SIGINT, signal_handler)

# load data from csv file
def load_data(file_name):
    if not os.path.exists(file_name):
        print(f"{file_name} doesn't exist.")
        exit()
    mileages = []
    prices = []
    with open(file_name, 'r') as file:
        dataset = csv.reader(file)
        next(dataset)
        for row in dataset:
            mileages.append(float(row[0]))
            prices.append(float(row[1]))
    return mileages, prices

# normalize and denormalize data
def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

def denormalize(value, min_value, max_value):
    return value * ((max_value - min_value) + min_value)

# model
def model(mileage, theta0, theta1):
    return theta0 + theta1 * mileage
