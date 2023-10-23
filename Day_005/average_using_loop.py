# Input a Python list of student heights
student_heights = input().split()
total_height = 0
number_of_student = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆
    total_height += student_heights[n]
    number_of_student += 1

average_height = round(total_height / number_of_student)
print(f"total height = {total_height}")
print(f"number of students = {number_of_student}")
print(f"average height = {average_height}")

# Write your code below this row 👇

# total height = 857
# number of students = 5
# average height = 171

# input 151 145 179
