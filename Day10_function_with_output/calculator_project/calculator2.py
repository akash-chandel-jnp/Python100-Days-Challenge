def add(n1 , n2):
    ans= n1 +n2;
    print(f" {n1} + {n2} = {ans}")
    return ans

def subtract(n1 , n2):
    ans= n1 - n2;
    print(f" {n1} - {n2} = {ans}")
    return ans

def multiply(n1 , n2):
    ans= n1 * n2;
    print(f" {n1} * {n2} = {ans}")
    return ans

def divide(n1 , n2):
    ans= n1 / n2;
    print(f" {n1} / {n2} = {ans}")
    return ans

operations = {
    '+' : add , 
    '-' : subtract , 
    '*' : multiply ,
    '/' : divide
}

num1 = int(input("Enter first number : "))
should_continue = True;
while should_continue :

    for key in operations:
        print(f"{key}") 

    operator = input("Choose one of the operator from the above: ")
    num2 = int(input("Enter second number : "))

    func_operator = operations[operator]

    answer = (func_operator(num1 , num2))
    
    continue_or_not = input("type 'Y' to continue | or type 'N' to exit : ")
    
    if continue_or_not == 'Y' :
        new_operator = input("Select operator : ")
        num3 = int(input("Enter next number : "))
        func_operator = operations[new_operator]

        answer = func_operator(answer,num3)
        
    
    else:
        should_continue = False;
