
class Dog:
    # Contructor
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
d1  = Dog("Tiger", "Woof!")

print(d1.sound)

# use method instead of contructor output or hardcode data

class Dog:
    def bark(self):
        print("Woof!")  # Method instead of constructor attribute

d1 = Dog()
d1.bark()  # Output: "Woof!"