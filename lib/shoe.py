#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        
        


    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")
        
    def get_color(self):
        return self._color
        
    def set_color(self, value):
        self._color = value

    color = property(get_color, set_color)
    
    def get_size(self):
        return self._size
        
    def set_size(self, value):
        if(isinstance(value, int)):
            self._size = value
        else:
            print("sized must be an integer")

    size = property(get_size, set_size)

    def get_material(self):
        return self._material
        
    def set_material(self, value):
        self._material = value
        
    material = property(get_material, set_material)

    def get_condition(self):
        return self._condition
        
    def set_condition(self, value):
        self._condition = value 

    condition = property(get_condition, set_condition)