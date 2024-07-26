#divide by zero exception 
a = 10
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(f"Error reported: {e}")   
    
    
# print User for Integer and Raise ValueError for Invalid Input
try:
    user_input = int(input("Enter a number: "))
    print(f"You entered value is: {user_input}")
except ValueError as e:
    print(f"Error reported: {e}")   
    
    
# FileNotFoundError Exception
try:
    open("poiuhukijuhyg.txt" ) 
except FileNotFoundError as e:    
    print(f"Error reported: {e}")     


# prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
try:
    user_input_1 = int(input("Enter 1st number: "))
    print(f"You entered value is: {user_input_1}")
    user_input_2 = int(input("Enter 2nd number: "))
    print(f"You entered value is: {user_input_2}")
    
except ValueError as e:
    print(f"Error reported: {e}") 

    

    