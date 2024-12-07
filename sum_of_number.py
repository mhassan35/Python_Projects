num_input = input("Enter a number: ")
digit_sum = 0

for digit in num_input:
    digit_sum += int(digit)

print("Sum of digits:", digit_sum)