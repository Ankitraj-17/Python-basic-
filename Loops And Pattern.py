# 1.Print a right-angle star pattern.
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2.Print a pyramid pattern.
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# 3.Sum of digits of a number using a loop.
number = 12345
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

print(f"Sum of digits: {digit_sum}")



# 4.Find factorial of a number using a loop.
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number}: {factorial}")


# 5.Print numbers from 1 to 100 skipping multiples of 3.
for i in range(1, 101):
    if i % 3 != 0:
        print(i, end=" ")


# 6.Find prime numbers between 1 and 100.
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")



# 7.Print Fibonacci series up to n terms.
n = 10
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 8.Count how many digits are in a number (no string conversion).
number = 12345
count = 0
temp = number

while temp > 0:
    count += 1
    temp //= 10

print(f"Number of digits in {number}: {count}")

