# Factorial of a number using recursion
def recur_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recur_factorial(num-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def factorialtester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
    recur_factorial(num)