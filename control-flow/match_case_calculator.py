num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Choose the operation (+, -, *, /):")
if operation=="+":
    result=num1+num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
else:
    if num2!=0:
        result=num1/num2
    else :
        print("Cannot divide by zero")
print(result)
