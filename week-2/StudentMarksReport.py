marks = [78, 85, 62, 90, 55, 88]

print("Highest:" + str(max(marks)))
print("Lowest:" + str(min(marks)))
print("Average" + str(sum(marks)/len(marks)))

print("Distinction:")
for mark in marks:
    if mark >= 75:
        print(mark)

marks.append(95)
print("Updated Marks List: " + str(marks))

marks.remove(55)
print("After Removing 55: " + str(marks))

marks.sort()
print("Sorted Marks: " + str(marks))