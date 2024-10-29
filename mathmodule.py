#learning the math module

import math

print("value of pi=",math.pi)

print("value of e=",math.e)

n = float(input ("Enter a number: "))

print("square root of n",math.sqrt(n)) #square root

print("power of n raised to two,ie squared",math.pow(n,2)) #power

a = float(input("enter a negative number: "))

if a>0 or  a==0:

    print("error")

print ("absoulte value",math.fabs(a))  #absolute value 

b = float(input("enter a decimal number,positive or negative: "))

print("floor ",math.floor(b)) #floor function ,greatest integer function

print("ceil",math.ceil(b)) #ceiling function ,least integer function

c = float(input ("Enter a number: "))

if c<0 or c==0:
    print("error")

print("natural log",math.log(c)) #natural logarithm,base e

print("common log",math.log10(c)) #common logarithm,base 10

print("binary log",math.log2(c)) #binary logarithm,base 2,used in  computer science and information theory,etc.

angle1 = float(input("enter angle in radians : "))

print("angle in degree=",math.degrees(angle1))

angle2 = float(input("enter angle in degree : "))

print("angle in radian =",math.radians(angle2))   # pi radian = 180 degrees

print(math.degrees(math.pi),"degrees =",math.radians(180),"radians")


#end of code


