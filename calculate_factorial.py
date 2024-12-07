user_input = int(input("Enter number: "))
fact = 1
i = user_input
while i > 1:
    fact *= i
    i -= 1
print(f"The factorial of {user_input} is: {fact}")