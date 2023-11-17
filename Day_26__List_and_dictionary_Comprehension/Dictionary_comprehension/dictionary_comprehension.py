# new_dict  = { new_key:new_value  for  (key:value) in dict.items() }
import random

names = ['akash', 'aman', 'ankit', 'abhishek', 'anurag', 'ankita', 'gargi', 'shobhit']
student_data = {student: random.randint(0, 100) for student in names}
print(student_data)

# creating a dictionary for only students getting more than 50 marks:
# passed_student = {student:student_data[student] for student in student_data if student_data[student] > 50}
passed_student = {student: score for (student, score) in student_data.items() if score > 50}

print(passed_student)
