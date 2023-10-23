def calculator(num1,num2,operator):
    should_continue =True;
    while should_continue ==True:
        if operator == '+':
            result =num1 +num2;
        elif operator=='-':
            result = num1 - num2;
        elif operator == '/':
            result = num1 / num2
        elif operator == '*':
            result = num1 * num2
        else:
            result = "Invalid Operator selected"
        print(result)
        continue_or_not = input(f"Do you want to continue the result {result} for further calulation , select 'Y' else select 'N'")

        if continue_or_not == 'Y':
            calculator(result , num2= int(input("enter 2nd operand")) , operator= input("enter operator"))
        else:
            print(f"Result is {result}")
            should_continue = False
    
    return result
    


(calculator(23,10,'*'))


