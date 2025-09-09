import ShoppingBillCalc

print("Using ShoppingBillCalc module via import")

# Only positional 
print("Bill 1:", ShoppingBillCalc.calculate_bill(500, 2))
# With custom tax 
print("Bill 2:", ShoppingBillCalc.calculate_bill(500, 2, tax=0.1)) 
# With custom discount 
print("Bill 3:", ShoppingBillCalc.calculate_bill(500, 2, discount=50)) 
# With custom tax and discount 
print("Bill 4:", ShoppingBillCalc.calculate_bill(500, 2, tax=0.08, discount=100)) 