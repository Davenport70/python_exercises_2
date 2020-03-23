# # functions
# # practice using, defining and calling functions
#
# # Build a basic object functional
# # phase 1: build function containing add, subtract, multiply, divide.
#
# #  calculate the area of a circle
# def area_of_circle(radius):
#     pie = 3.14
#     area = pie * (radius ** 2)
#     return area
#
# radius = int(input("What is the radius?: "))
#
# print(area_of_circle(radius))
#
# #  calculate the area of a square
# def area_of_square(length, width):
#     return length * width
#
# print(area_of_square(20, 30))
#
# #  calculate the area of a triangle (just find the easiest way)
# def area_of_triangle(length, width):
#     return (length / 2) * width
#
# print(area_of_triangle(10, 20))

# ####
#
# def add_funtion(arg1, arg2):
#     return arg1 + arg2

# As a user I want to have a add_funtion()
# that takes in two arguments and add them.
# print("calling the add_function() with 290 and 10, expect 300 to be the result ")
# print(add_funtion(290, 10) == 300)
# print('got:', add_funtion(290, 10) )
#
# print("calling the add_function() with 270 and 5, expect 275 to be the result ")
# print(add_funtion(270, 5) == 275)
# print('got:', add_funtion(270, 5) )

# defining area of a square
def area_of_square(arg1, arg2):
    return arg1 * arg2

# print calling the area of a square with length == 10 multiplied by width == 10
print(area_of_square(10, 10) == 100)
# print calling the area of a square with length == 20 multiplied by width == 30
print(area_of_square(20, 30) == 600)

