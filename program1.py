def simple_calculator(num1, num2, choice):
    match choice:
        case '1':
            print(f"The addition of {num1} and {num2} is : ",num1+num2)
        case '2' : 
            print(f"The substraction of {num1} and {num2} is : ",num1-num2)
        case '3' :
            print(f"The Multiplication of {num1} and {num2} is : ",num1*num2)
        case '4' :
            print(f"The remonnder of {num1} and {num2} is : ",num1%num2) 
        case _:
            print("Enter the valid choice")


number1=int(input("Enter the Number 1 : "))
numner2=int(input("Enter the number 2 : "))

choice=input("Enter the Choice u want to :\n 1. add \n 2.sub \n 3.mul \n 4.module \n")
simple_calculator(number1,numner2, choice)


            