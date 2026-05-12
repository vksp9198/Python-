import math

def circle_states(radius):
    area_circle =int(math.pi * radius * radius)
    circumference_circle = int(2 * math.pi *radius)
    return area_circle , circumference_circle
a , c = circle_states(6)
print("Area of circle = " , a , "Circumference of circle = ", c)
    
