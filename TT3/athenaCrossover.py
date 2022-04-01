import random
def game():
    # Print multiline instruction
    # performstring concatenation of string
    print()
    print("Rules of Rock Paper Scissors: \n"
          +"1. Paper > Rock \n"
          +"2. Rock > Scissors \n"
          +"3. Scissors > Paper \n")

    while True:
        print("Enter your choice: \n 1. Rock \n 2. paper \n 3. scissor \n")


        #user input
        choice = int(input("Make your choice: "))


        # does not allow the user to continue if the input is invalid
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))

        #print("your choice is: ", choice)

        # initialize value of choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'

        # print user choice
        print("user choice is: " + choice_name)