# largest of 3 numbers

# input of 3 numbers from user
n1 = float(input("enter first number: "))
n2 = float(input("enter second number: "))
n3 = float(input("enter third number: "))

if (n1 >= n2) and (n1 >= n3):
    largest = n1
elif (n2 >= n1) and (n2 >= n3):
    largest = n2
else:
    largest = n3

print("The largest number is:", largest)