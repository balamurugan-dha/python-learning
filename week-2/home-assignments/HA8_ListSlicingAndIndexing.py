prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print("Middle three prime numbers:", prime_numbers[3:8])
print("Every second prime number:", prime_numbers[1::2])
print("Last three prime numbers:", prime_numbers[-3:])
print("Last three prime numbers in reverse order:", prime_numbers[-1:-4:-1])
print("Prime numbers in reverse order:", prime_numbers[::-1])
print("Sort the prime numbers in descending order:", sorted(prime_numbers)[::-1])
print("Sort the prime numbers in descending order:", sorted(prime_numbers, reverse=True))