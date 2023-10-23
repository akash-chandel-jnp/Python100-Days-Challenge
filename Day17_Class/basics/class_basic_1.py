class User:
    pass


# although while create class of car , we did not def any attribute but still while creating obj from the class we can pass attribute that we want ..
# but this is not a good way as it may create irregularity as well as repetitive work

user_1 = User()
user_1.id = "A26"
user_1.name = "Amit"
user_1.plan = "Golden"

user_2 = User()
user_2.id = "A29"
user_2.name = "Sumit"
user_2.plan = "Basic"

print(user_2.id)
