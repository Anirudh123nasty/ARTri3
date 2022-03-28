{% include navigation.html %}
# Week 0

# Data Structures Project

## Code snippets

### Code for animation

```python 
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
BASEBALL_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    # print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    ____   ")
    print(sp + "  .'    '.  ")
    print(BASEBALL_COLOR, end="")
    print(sp + " /'-....-'\ ")
    print(RESET_COLOR, end="")
    print(sp + " |        |  ")
    print(BASEBALL_COLOR, end="")
    print(sp + " \.-''''-./  ")
    print(RESET_COLOR, end="")
    print(sp + "  '.____.'  ")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)
```
# Code for keypad
```python
def write(matrix):
    length = len(matrix)
    for i in range(length):
        row = len(matrix[i])
        for order in range(row):
            print(matrix[i][order], end='')
        print()

def tester():
  a = [[1,2,3],[4,5,6],[7,8,9]]
  write(a)
  ```
 # Code for swap
 ```python
 def swap(age1, age2):
  if age1 > age2:
      temp1 = age1
      temp2 = age2
      age1 = temp2
      age2 = temp1
      return age1, age2
  if age1 < age2:
      return age1, age2

def testSwap():
  firstAge = int(input("Enter a number for age 1:"))
  secondAge = int(input("Enter a number for age 2:"))
  x, y = swap(firstAge, secondAge)
  print(x, y)
  ```
# Code for menu and submenu
```python
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import baseball
import swap
import matrix
import pattern



# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Baseball Animation", baseball.ship],
    ["Swap", swap.testSwap],
    ["Matrix", matrix.tester]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Christmas Tree", pattern.testPattern],
]

# patterns_sub_menu = [
#     ["Patterns", "patterns.py"],
#     ["PreFuncy", "wipy/prefuncy.py"],
#     ["Funcy", funcy.ship],
# ]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Pattern", submenu])
    # menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
    #menuc()

```
# Code for Christmas Tree Pattern
```python
def christmaspattern(n):
    for i in range(n):
        for c in range(n-i):
            print(' ', end=' ')
        for c in range(2*i+1):
            print('*',end=' ')
        print()

def testPattern():
  row = int(input('How many rows: '))
  christmaspattern(row)
```

# Week 1

# Data Structures Project

## Code snippets

### Code for Fibonacci (Hack 3)

```python 
def fibo(n):
    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibo(n-1) + fibo(n-2)


def fibotester():
  try:
    n = int(input("Enter the term number: "))
    if n < 0:
      print("Please enter positive number!")
    else: 
      for i in range(n):
                print(fibo(i), end=', ')
      print ("are the fibonacci terms!")
  except: 
    print("Please enter number!")

# fibotester()
```
### Code for Hack 1 and 2
```python
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
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
  
def TT1tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

# TT1tester()
```
### Code for Updated Christmas Tree with Stump
```python
def christmaspattern(n):
    for i in range(n):
        for c in range(n-i):
            print(' ', end=' ')
        for c in range(2*i+1):
            print('*',end=' ')
        print()
    for i in range(int(n/2)):
        for c in range(int(n-1)):
            print(' ', end=' ')
        for c in range (int(n/2)-1):
            print ('*',end=' ')
        print()
  

def testPattern():
  row = int(input('How many rows: '))
  christmaspattern(row)
```
# Week 2

# Data Structures Project

## Code snippets

### Code for Factorial with class and call
``` python
class Factorial:
    def __init__(self):
        self.factSeq = [1]
    def __call__(self, n):
        if n < len(self.factSeq):
            return self.factSeq[n]
        else:
            # Compute the requested Fibonacci number
            fact_number = n * self(n - 1) # two recursive calls to self (__call__(self, n))
            self.factSeq.append(fact_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factSeq[n]
def facttester():
  fact_of = Factorial() # object instantiation and run __init__ method
  l = int(input('What number: '))
  print(fact_of(l)) # object running __call__ method
```
### Code for Own Math Function Imperative
```python
#this is the imperative form of determining if a function is even or odd 
def imperative():
  num = int(input('Enter a number: '))
  
  if(num % 2 == 0):
    print(num)
    print("is an even number")
  else:
    print(num)
    print("is an odd number")
```
### Code for Own Math Function OOP
```python
class OddorEven:
  def __init__(self):
    print("The number is", end=" ")
  def __call__(self, n):
    if(n % 2 == 0):
      print(n)
      print("which is even!")
    else:
      print(n)
      print("which is odd!")

def OddorEvenfinder():
  print("Odd or Even")
  n = int(input("Enter any Number to determine if it is even or odd: "))
  oddoreven = OddorEven()
  oddoreven(n)

# OddorEvenfinder()
```
### SS for Reorganized Files
![image](https://user-images.githubusercontent.com/89223726/160330022-e08e9dcd-b1b3-4aa5-a684-ffc55f4d0842.png)

### Code for Reorganized Files
```python
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from TT0 import baseball
from TT0 import swap
from TT0 import matrix
from TT0 import pattern
from TT1 import fibo
from TT1 import loop
from APython import factorial
from TT2 import classy
from TT2 import imperative
from TT2 import OOP



# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# # 2. function references will be executed directly file.function()
# main_menu = [
#     ["Baseball Animation", baseball.ship],
#     ["Swap", swap.testSwap],
#     ["Matrix", matrix.tester],
#     ["Loop", loop.looptester],
#     ["Fibonacci", fibo.fibotester],
#     ["Factorial", factorial.factorialtester],
# ]

main_menu = []



# Submenu list of [Prompt, Action]
# Works similarly to main_menu
# sub_menu = [
#     ["Christmas Tree", pattern.testPattern],
# ]

math_sub_menu = [
    ["Matrix", matrix.tester],
    ["Fibonacci", fibo.fibotester],
    ["Factorial", factorial.factorialtester],
    ["Factorial with class", classy.facttester],
    ["Odd or Even (Imperative Method)", imperative.imperative],
    ["Odd or Even (OOP Method)", OOP.OddorEvenfinder],
]

adventure_sub_menu = [
    ["Baseball Animation", baseball.ship],
    ["Swap", swap.testSwap],
    ["Christmas Tree", pattern.testPattern],
]

data_sub_menu = [
    ["Loops", loop.looptester],
]
# patterns_sub_menu = [
#     ["Patterns", "patterns.py"],
#     ["PreFuncy", "wipy/prefuncy.py"],
#     ["Funcy", funcy.ship],
# ]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Adventure", adventure_submenu])
    menu_list.append(["Data", data_submenu])

  

    # menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def math_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, math_sub_menu)
def adventure_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, adventure_sub_menu)

def data_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, data_sub_menu)
```

## Github Links 
* [Issue for organizing files](https://github.com/Anirudh123nasty/ARTri3/projects/1#card-79745861)
* [Issue for factorial with class](https://github.com/Anirudh123nasty/ARTri3/projects/1#card-79745845)
* [Issue for individual math function (OOP and Imperative)](https://github.com/Anirudh123nasty/ARTri3/projects/1#card-79745832)

## Replit links
* [Commit for math function](https://github.com/Anirudh123nasty/ARTri3/commit/4336f4aa990607a14b0d2a7f47c79885336e9c01)
* [Commit for organization](https://github.com/Anirudh123nasty/ARTri3/commit/f760793147b1d4753c90b40061f2a56f52d8ca6b)
* [Commit for factorial](https://github.com/Anirudh123nasty/ARTri3/commit/fcfe875e811c02248ef12cb0b29f3e341303c36f)
* [Replit](https://replit.com/@AnirudhR8/ARTri3#.replit)
