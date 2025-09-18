def calculate_salary(basic, hra, da, bonus=0):
    salary = basic + hra + da + bonus
    if (bonus == 0):
        salary = basic + hra + da
        print("Salary (without bonus): ", str(salary))
    else:
        salary = basic + hra + da + bonus
        print("Salary (with bonus): ", str(salary))

# Calling without bonus 
calculate_salary(30000, 8000, 5000) 
# Calling with bonus 
calculate_salary(30000, 8000, 5000, 2000) 