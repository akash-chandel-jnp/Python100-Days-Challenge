class Car:
    # constructor function
    def __init__(self, no_of_seats, category):  # the paramenter passed in the contructor gvnh
        self.count_of_seat = no_of_seats
        self.category = category
        self.count_of_tyres = 4 # this is the default value for all the objects and need not be passed as an argument while creating the object


car_1 = Car(5, "sports")
print(f"no. of seats in the car is : {car_1.count_of_seat} and it belongs to : {car_1.category} category.")
car_1.max_speed = 120
print(f"Max speed of the car1 is : {car_1.max_speed}")

car_2 = Car()
car_2.category = "luxury"
print(car_2.category)
