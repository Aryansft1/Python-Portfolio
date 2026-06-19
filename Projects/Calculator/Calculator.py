Number1 = float(input())
Number2 = float(input())
Operator = input()

if Operator in ['+', '-', '/', '*']:
    if Operator == '+':
        result = Number1 + Number2
        print(result)
    elif Operator == '-':
        result = Number1 - Number2
        print(result)    
    elif Operator == '/':
        if Number1!=0 and Number2!=0:
            result = Number1 / Number2
            print(result)
        else :
            print("Numbers Cant Be Zero (0)")
    elif Operator == '*':
        result = Number1 * Number2
        print(result)
else :
    print("Invalid Operator")       
