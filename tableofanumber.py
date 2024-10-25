#Python program to multiplication table of a number

num = int(input("Enter a number: "))

#input from user

print("multiplication table of: ",num)

#printing multiplication table
for i in range(1,11):
    print(num,'X',i,'=',num * i)
