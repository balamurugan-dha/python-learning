try:
    with open("report.txt", "w") as file:
        file.write("TestCase1 - Passed\n")
        file.write("TestCase2 - Failed\n")
        file.write("TestCase3 - Passed\n")
except IOError as e:
    print(f"Error writing to file: {e}")

try:
    with open("report.txt", "a") as file:
        file.write("TestCase4 - Passed\n")
        file.write("TestCase5 - Failed\n")
except IOError as e:
    print(f"Error appending to file: {e}")

try:
    print("\nFinal file content:")
    print("-----------------------")
    with open("report.txt", "r") as file:
        for line in file:
            print(line.strip())
except IOError as e:
    print(f"Error reading file: {e}")


passed_count = 0
failed_count = 0
total_tests = 0

try:
    with open("report.txt", "r") as file:
        for line in file:
            total_tests += 1
            if "Passed" in line:
                passed_count += 1
            elif "Failed" in line:
                failed_count += 1
    
    print("\nTest Summary:")
    print("---------------")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")

    print("\nFile Attributes:")
    print("------------------")
    print(f"File name: {file.name}")
    print(f"Is file closed: {file.closed}")
    print(f"Is file writable: {file.writable()}")
except IOError as e:
    print(f"Error processing file for summary: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")