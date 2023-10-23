def greet(f_name,l_name):
    print(f"Hello {f_name} {l_name} ! \nHow are you.")

# below is a example of calling a function with positional argument as order of input is very important.
print("This is the output from POSITIONAL argument type calling of function with CORRECT order")

greet("Akash", "Chandel")

print("This is the output from POSITIONAL argument type calling of function with INCORRECT  order")

greet("Chandel", "AKash")

# below is the example of calling the function with keyword argument as order of argument is not relevant.
print("This is the output from KEYWORD argument type calling of function with CORRECT order")
greet(f_name= 'Akash' , l_name= 'Chandel')

print("This is the output from KEYWORD argument type calling of function with INCORRECT order")

greet(l_name= 'Chandel' , f_name= 'Akash');

    


