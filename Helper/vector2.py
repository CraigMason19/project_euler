# Vector2.py
# Declaration and implementation of a 2D vector classes for python

import math

class Vector2:
    def __init__(self, x, y):
        self.mX = x
        self.mY = y

    def __str__(self):
        return "(" + str(self.mX) + ", " + str(self.mY) + ")"

    def __repr__(self):
        return "Vector2(" + str(self.mX) + ", " + str(self.mY) + ")"
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.mX + other.mX, self.mY + other.mY)
                    
    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.mX - other.mX, self.mY - other.mY)
        
    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.mX * other.mX, self.mY * other.mY)
        
    def __div__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.mX / other.mX, self.mY / other.mY)
        
    def calculate_length(self):
        length = math.sqrt(self.mX * self.mX + self.mY * self.mY)
        return math.fabs(length)

    def normalise(self):
        l = self.calculate_length()
        try:
            1.0 / l
        except ZeroDivisionError:
            return
        self.mX = self.mX / l
        self.mY = self.mY / l

    def dot(self, other):        
        if isinstance(other, Vector2):
        	return self.mX * other.mX + self.mY * other.mY;

def dot(v1, v2):        
    return v1.mX * v2.mX + v1.mY * v2.mY;        
