"""practice different math expressions calculations"""
#declare num_a and num_b
num_a = 5
num_b = 2

a = 3
b = 4
c = 5
#1. Sum and difference
sum = num_a + num_b
print(f"{num_a} +{num_b} = {sum}")
difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

#2. float devision
devision = num_a / num_b
print(f"{num_a} / {num_b} = {devision}")

#3. integer division
division = num_a // num_b
print(f"{num_a} // {num_b} = {devision}")

#4. powerful operations
multiply_numbers = num_a * num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")

#5. find avarage
avarage = (num_a + num_b) / 2
print(f"{num_a} + {num_b} /2 = {avarage}")

#6. area of the circle
radius = 10
import math
math.pi * radius ** 2

#7. Area of an equilateral triangle
side_length = 2
mid_length = 3
triangle_area = (side_length * mid_length) /2
triangle_area = round(triangle_area, 3)

#8. Calculate discriminant
a = 3
b = 4
c = 5
discriminant = b**2 - 4 * a * c

#9. Calculate hypotenuse length
a = 3
b = 4
c = 5
# hypotenuse_length = a**2 + b**2 = c**2

#10. Calculate cathetus length
b = math.sqrt(a**2+c**2)
print(b)

#11. Time converter
seconds =  3689
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(hours, minutes, seconds)

#12. Student helper
angle =

