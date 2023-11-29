# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:33:13 2023

@author: ziegl
"""

import random

class Dog(object):
    def __init__(self, name):
        self.name = name
        # Randomize initial hunger level and location
        self.hungry = random.randint(0, 100)
        self.x = random.randint(0, 100)
        self.y = random.randint(0, 100)

    def eat(self):
        # Set plane
        self.hungry = max(0, self.hungry - 10)

    def play_fetch(self, stick_x, stick_y):
        # If hunger > 50, dont play fetch
        if self.hungry > 50:
            print("nope! Too tired!")
            #Random location within the parameters if < 50 hunger
        else:
            self.x += random.randint(1, 10) - 5
            self.y += random.randint(1, 10) - 5
            # Calculate distance using disdance equation
            distance = ((self.x - stick_x) ** 2 + (self.y - stick_y) ** 2) ** 0.5
            # Get stick if within 3 points for x and y, then random location
            if distance <= 3:
                print("got it! Here's your stick!")
                self.x = random.randint(0, 100)
                self.y = random.randint(0, 100)
                #else, report location and distance to stick then add 10 hunger
            else:
                print(f"location {self.x},{self.y}. Distance to stick: {distance:.2f}")
                self.hungry += 10

    def __str__(self):
        # If hunger is > 50 status = very hungry
        if self.hungry > 50:
            adj = "very "
            # If hunger is < 50 status = a little bit
        else:
            adj = "a little bit "

        status = f"I am {adj}hungry! ({self.hungry}) location: {self.x},{self.y}"
        return status

# Instantiate a dog with a given name
dog_name = "Sport"
my_dog = Dog(dog_name)

# Check how hungry the dog is and have it eat until it is ready to play fetch
print(f"Initial status of {dog_name}: {my_dog}")
while my_dog.hungry > 30:
    my_dog.eat()
    print(f"{dog_name} is eating... Current status: {my_dog}")

# Have the dog play fetch until it refuses because it's too hungry or finds the stick
stick_coordinates = (75, 75)
while my_dog.hungry <= 50:
    my_dog.play_fetch(*stick_coordinates)
    print(f"{dog_name} is playing fetch... Current status: {my_dog}")

# Feed the dog again and have it play fetch again
while my_dog.hungry > 30:
    my_dog.eat()
    print(f"{dog_name} is eating... Current status: {my_dog}")

while my_dog.hungry <= 50:
    my_dog.play_fetch(*stick_coordinates)
    print(f"{dog_name} is playing fetch... Current status: {my_dog}")
