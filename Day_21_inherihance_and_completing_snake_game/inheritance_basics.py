class Animals:
    def __init__(self):
        self.eyes_count = 2

    def breathe(self):
        print("inhale , exhale ")


class Fish(Animals):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breathe(self):                       # """ only if we wath to redefine or modify breathe function"""
        super().breathe()                    # to take the breathing functions as it is as already def
        print("Breathing under the water")   # add something to it


mr_fish = Fish()
mr_fish.swim()
mr_fish.breathe()
print(mr_fish.eyes_count)
