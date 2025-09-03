sales = [1200, 3400, 560, 4500, 2100]

total_sales = sum(sales)

average_sales = total_sales / len(sales)

highest_sale = max(sales)
lowest_sale = min(sales)

print("Total Sales: " + str(total_sales))
print("Average Sales: " + str(average_sales))
print("Highest Sale: " + str(highest_sale))
print("Lowest Sale: " + str(lowest_sale))