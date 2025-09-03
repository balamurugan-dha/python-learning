correct_password = "openAI123"

for attempt in range(1, 4):
    password = input("Enter password (attempt " + str(attempt) + "/3): ")
    
    if password == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")