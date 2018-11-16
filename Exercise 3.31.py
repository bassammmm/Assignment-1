print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.31\n\n")

radius = 8
co_x = float(input("Please enter the x-coordinate: "))
co_y = float(input("\nPlease enter the y-coordinate: "))
import math
boole = math.sqrt((co_x*co_x)+(co_y*co_y)) < radius
if boole==True:
    print("\nAre these coordinates within the dart? Yes It Is In!")
else:
    print("\nAre these coordinates within the dart? NO It Is In!")

