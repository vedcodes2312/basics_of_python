#Python program to calculate distance between two coordinates
import math
print("enter first coordinate(x1,y1: )")
x1 = float(input("enter value of abscissa x1: "))
y1 = float(input("enter value of ordinate y1: "))

print("enter second coordinate(x2,y2: )")
x2 = float(input("enter value of abscissa x2: "))
y2 = float(input("enter value of ordinate y2: "))

distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print("distance between two points is: ",distance)

