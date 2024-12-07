provide_input = int(input("Enter a number n: "))

sum_of_evens = 0

for num in range(1, provide_input + 1):
    if num % 2 == 0:
        sum_of_evens += num

print(f"The sum of all even numbers from 1 to {provide_input} is: {sum_of_evens}")
