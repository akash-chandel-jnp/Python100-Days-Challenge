# Write your code below this line 👇

def prime_checker(number):
    isPrime = True;
    if number==1:
        isPrime = False;
    
    else:
        for n in range(2,int(number/2)):
            if number % n ==0:
                isPrime = False;
        if isPrime :
            print(f"It's a prime number.")
        else:
            print(f"It's not a prime number.")





# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Enter a number \n")) # Check this number
prime_checker(number=n)