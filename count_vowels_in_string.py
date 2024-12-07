user_input = input("Enter a string: ")

vowel_count = 0

for char in user_input:
    if char.lower() in 'aeiou':
        vowel_count += 1

print("Total number of vowels in the string:", vowel_count)
