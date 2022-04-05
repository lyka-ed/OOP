# --------------------------------------------------------
""" 
TASK 1
Create a car class with 2 instance attributes:

.color which stores the name of the car's color as a string
.mileage which stores the number of miles on the car as an integer
The instantiate two car - objects, a blue car with 20,000 miles and a red car 
with 30,000 miles and print out their colors and mileage."""


class Car:
    def __init__(self,clr, mlg):
        self.color = clr
        self.mileage = mlg

    def drove(self):
        print(f"Alex drove a {self.color} covering over {self.mileage} miles. ")
           
blue_car = Car("blue car",20000)
blue_car.drove()

print()

red_car1 = Car("red car", 30000)
red_car1.drove()



"""  
TASK 2
 
Create a citizen class with 5 instance attribute:
name, age, state_Of_origin, BVN and phone number.
Then instantiate citizen object and 
print out the value of every new object instantiated
"""

class Citizen:
    def __init__(self, name, age, s_Of_o, BVN, phone_number):
        self.name = name
        self.age = age
        self.state_Of_origin = s_Of_o
        self.bvn = BVN
        self.phone_number = phone_number

    def citizen_profile(self):
        print(f"{self.name} is {self.age} years old and hails from {self.state_Of_origin}. She can be contacted via {self.phone_number}. Bank verofication number: {self.bvn}")    

 
print()       
profile_1 = Citizen("Chidera Ezike", 25, "Anambra state", 1000023185, +2348155002377)
profile_1.citizen_profile()

print(profile_1.name)
print(profile_1.age)
print(profile_1.state_Of_origin)
print(profile_1.bvn)
print(profile_1.phone_number)
