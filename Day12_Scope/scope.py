# my_health = 20
# def change_health():
#     new_health =my_health*2
#     def deeper_function():
#         my_eyesight ="veryGood"
#         print(my_eyesight)
#     deeper_function()
#     print(f"health inside function become {new_health}")
# change_health()
# print(f"health outside my function become {my_health+10}")

# change_health()

enemies = "zombies"

def change_enemies():
    # enemies +='abc' 
    # this will not work as it thinks as you are trying to something you created inside the function
    global enemies
    enemies+='_bosss' # now this will work as we mentioned that we are referring to global variable
    
    print(enemies)

change_enemies()