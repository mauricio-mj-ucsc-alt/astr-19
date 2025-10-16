# Write a Python program that declares a class describing your favorite animal. 
# Have the data members of the class represent the following physical parameters 
# of the animal: length of the arms (float), length of the legs (float), number of eyes (int),
# does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets 
# the values of the data members when an instance of the class is created. Write a member function
# of the class to print out and describe the data members representing the physical characteristics
# of the animal.


class Dog:
    def __init__(self, arm_length: float, leg_length: float, num_eyes: int, has_tail: bool, is_furry: bool):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("\nDog's Physical Characteristics:")
        print(f"Length of arms: {self.arm_length} inches")
        print(f"Length of legs: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'}")
def main():
    perrito = Dog(arm_length=8.0, leg_length=15.0, num_eyes=2, has_tail=True, is_furry=True)
    perrito.describe()

if __name__ == "__main__":
    main()

