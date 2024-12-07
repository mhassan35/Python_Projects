palindrome_input = input("Enter any String or number: ")

if palindrome_input == palindrome_input[::-1]:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
