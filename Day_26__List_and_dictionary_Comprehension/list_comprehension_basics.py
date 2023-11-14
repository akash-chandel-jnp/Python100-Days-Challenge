# Python  Sequences are : list , range , strings, tuple

# List comprehension

# Example 1:
numbers = [1, 5, 8]
new_numbers = [n * 2 for n in numbers]  # [new_item for n in sequence]

print(new_numbers)

# Example 2:
name = 'Akash'  # string is also a sequence in python
letters_in_name = [letter for letter in name]
print(letters_in_name)

# Example 3:
square_first_10_nums = [n ** 2 for n in range(1, 11)]
print(square_first_10_nums)


# Conditional list comprehension
# [new_item for n in sequence if test]

# example: find the list of all the number from 1 to 100 but only for the numbers which are divisible by 4 and 5
req_nums = [num for num in range(1, 101) if num % 4 == 0 and num % 5 == 0]
print(req_nums)

# Example 4: Convert all the name having more than 5 letters into Uppercase
name_list = ['Akash', 'Ashraf', 'Priyanshu', 'arun']
uppercase_names = [name.upper() for name in name_list if len(name) > 5]
print(uppercase_names)
