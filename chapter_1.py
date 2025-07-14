# invented python -- Guido van Rossum, 1991

#add two integers number
num1=34
num2=76
print(num1+num2)

#find the number is even or odd by taking user input
num=int(input("Enter the number : "))
if num%2==0:
    print("this is Even")
else:
    print("it is odd number")

# Write the program to print only add numbers
for i in range(0,16):
    if(i%2!=0):
        print(i, " ")

# find the dataType of the variables
a="Sharath"
print(type(a))


# compare and print greater number
a=34
b=67
if(a>b):
    print("A is greater than B",a)
else:
    print("B is greater than A",b)


# fidn the Average of 2 numbers
num1=23
num2=45
result=(num1+num2)/2
print(result)

# find the squre of the number without is using builtin
number =45
print(number**2)  #number^number this is not valid ^