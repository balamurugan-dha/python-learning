amount = int(input("Enter withdrawal amount (Rs): "))

if amount % 100 == 0:
    print("Dispensing Rs. " + str(amount))
else:
    print("Invalid amount entered. Please enter multiples of 100.")