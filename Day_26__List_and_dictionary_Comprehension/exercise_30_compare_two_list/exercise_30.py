'''
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3]
IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

First, you will need to read from the files and create a list using the lines in the files.

This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp

Remember you can use the int() method in python to convert a string into an integer.

'''

# ================================= SOLUTION ========================================

with open("file1.txt") as file1:
    list1 = file1.readlines()
    new_list1 = [int(num.replace('\n', '')) for num in list1]
    print(new_list1)

with open("file2.txt") as file2:
    list2 = file2.readlines()
    new_list2 = [int(num.replace('\n', '')) for num in list2]
    print(new_list2)

result = [num for num in new_list1 if num in new_list2]   # ie take num from list1 only if it is in list2 also
print(result)

# Write your code above 👆
# print(result)
