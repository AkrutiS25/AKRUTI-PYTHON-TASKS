def addition(a,b):
    return a + b
    
def subtraction(a,b):
    return a - b
    
def multiplication(a,b):
    return a * b
    
def division(a,b):
    return a / b
    
    
print("THIS IS A CALCULATOR")

print("List of Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


while True:
    choice=input("ENTER CHOICE OF THE OPERATION YOU WNAT TO DO : ")
    
    if(choice=="1"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The addition of num1 and num2 is : " , addition(num1,num2))
    elif(choice=="2"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The subtraction of num1 and num2 is : " , subtraction(num1,num2))
    elif(choice=="3"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The multiplication of num1 and num2 is : " , multiplication(num1,num2))
    elif(choice=="4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if(num2 == 0):
            print("Error: Division by zero is not allowed.")
        else:
            print("The division of num1 and num2 is : " , division(num1,num2))
    else:
        print("INVALID CHOICE AS THE NUMBER DOESN'T EXIST IN THE LIST")
        
    next_calculation = input("Let's do next calculation? (YES OR NO): ")
    if next_calculation == "NO":
        break  

        
    


