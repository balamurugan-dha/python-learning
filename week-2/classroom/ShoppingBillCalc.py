def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount 
    return total


if __name__ == "__main__":
    print("Using ShoppingBillCalc functions directly")
    # Only positional 
    print("Bill 1:", calculate_bill(500, 2)) 
    # With custom tax 
    print("Bill 2:", calculate_bill(500, 2, tax=0.1)) 
    # With custom discount 
    print("Bill 3:", calculate_bill(500, 2, discount=50)) 
    # With custom tax and discount 
    print("Bill 4:", calculate_bill(500, 2, tax=0.08, discount=100)) 