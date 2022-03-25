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
    ["Factorial with class", classy. facttester],
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
