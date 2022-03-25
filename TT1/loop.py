# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with length greater than 3; placed in a personalized list about tennis attributes in the player
InfoDb.append({  
               "Name": "Sahil Lamar Jackson Jr.",  
               "UTR": "6.9",  
               "Height": "4 foot 20 inches",  
               "Dominance": "Left Handed",  
               "Preferred surface": "Your Mom's House!",  
               "Owns_Trophies":["4 Australian Opens","20 Wimbledon Trophies ","6 French Open Trophies","9 US Opens", "0 Keys to Your Mom's House."]  
              })  

InfoDb.append({  
               "Name": "Ethan Slow",  
               "UTR": "3.14",  
               "Height": "6.022 * 10^23 feet",  
               "Dominance": "Right Handed",  
               "Preferred surface": "Mort's Classroom",  
               "Owns_Trophies":["0 Keys to Your Mom's House","Possibly 1 CIF Championship","0 Maidens"] 
              })  

def print_data(n):
    print(InfoDb[n]["Name"], InfoDb[n]["UTR"])  # using comma puts space between values
    print("\t", "Trophies: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Trophies"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)


def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition


# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling for invalid input
#this is in fibo.py- it is recursive since it calls the function again and again to run and print all the values
  
def looptester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

# TT1tester()
