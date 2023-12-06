import train.py

with open('theta.txt', 'r') as file:
	theta0 = float(file.readline())
	theta1 = float(file.readline())

print('Theta0: ' + str(theta0))
print('Theta1: ' + str(theta1))

while True:
	mileage = input('Enter a mileage: ')
	if mileage == 'exit':
		break
	print('Price: ' + str(theta0 + theta1 * float(mileage)))

