# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:51:58 2023

@author: ziegl
"""

# Establish a class ("person") that contains self and a location
class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create the class dancer that has a specific movement pattern that is a subclass of person
class Dancer(Person):
    def __init__(self, x, y):
        #call super class to format when printed
        super().__init__(x, y)
        # Start program with no last move
        self.last_move = None

    def step(self):
        if self.last_move == 'L':
            self.x += 1  # If last move is L, move one R
            self.last_move = 'R'
        elif self.last_move == 'R':
            self.y += 1  # If last move is R, move one F
            self.last_move = 'F'
        elif self.last_move == 'F':
            self.x -= 1  # If last move is F, move one B
            self.last_move = 'L'
        elif self.last_move == 'B':
            self.y -= 1  # If last move is B, move one L
            self.last_move = 'B'
        else:
            # start with a left step when program begins
            self.x -= 1
            self.last_move = 'L'

# Set dancer starting point
dancer = Dancer(0, 0)

# create a for loop that terminates the program after 10 moves. 
for _ in range(10):
    dancer.step()
    # Format the position and last move
    print(f"Now at: ({dancer.x}, {dancer.y}), Last move: {dancer.last_move}")