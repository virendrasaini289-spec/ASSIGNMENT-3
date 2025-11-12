# Task 1: Calculate Factorial Using a Function 
a = int(input("enter number :-  "))
def factorial(n):
   
    a = 1
    while n > 1:
         a *= n
         n-= 1
    print(a)

factorial(a)

