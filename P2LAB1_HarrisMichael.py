#Michael Harris
#September 12, 2025
#P2_Lab1
#Variables_and_Expressions

import math
PI = float(f"{math.pi:.4f}")

radius = input(f"What is the radius of the circle? ")
radius = float(radius)

diameter = radius + radius
print("The diameter of the circle is", f"{diameter:.1f}")

circumference = radius*PI*2
print("The circumference of the circle is", f"{circumference:.2f}")

area = radius**2*PI
print("The area of the circle is", f"{area:.3f}")