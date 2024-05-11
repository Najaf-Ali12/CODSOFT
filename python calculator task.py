try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    operation=input(f"enter the operation(+,-,*,%,//,/,**) between {num1} and {num2}:")
    list=["/","//","*","%","-","+","**"]
    if operation in list:
        if operation=="+":
            print("The addition is",num1+num2)
        elif operation=="-":
            print("The subtraction is",num1-num2)
        elif operation=="/":
            if num2==0:
                print(f"{num1} divided by zero will be infinite")
            else:
                print("The divison is",num1/num2)
        elif operation=="*":
            print("The multiplication is",num1*num2)
        elif operation=="**":
            print(f"{num1} raise to {num2} is {num1**num2}")
        elif operation=="//":
            if num2==0:
                print("for divison num2 should be greater than 0")
            print("The floor divison is",num1//num2)
        elif operation=="%":
            print("The remainder obtained after divison is",num1%num2)
    else:
        print("select any one only from above operations")
except:
    print("you should enter only the numbers")
